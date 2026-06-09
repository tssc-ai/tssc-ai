"""
tssc_core — minimal primitives for the foundational TSSC experiments.

This is NOT the full Toy Model (see paper §11.5, "the immediate next step").
It contains only the operators the five baseline experiments need, each one
a direct transcription of an equation in the paper:

  - epsilon_star          : canonical self-consistency operator  (paper §5.5–§5.7)
  - active_support        : A*(X) = {x >= epsilon_star(X)}        (paper §5.5)
  - mean_cv_form          : closed form  x_bar * (1 + CV^2)        (paper §5.7)
  - receiver_coupling     : J = D_M^+ W   (receiver normalization) (paper §9)
  - field_step / relu     : V^{t+1} = (1-g)V + a*S + b*J*Psi       (paper §9)
  - rank1_als_weighted    : weighted rank-1 NMF via ALS            (paper §8.2.4)

Reference: Filippo Cosci, "Il significato come evento di campo —
Teoria dello Spazio Semantico Continuo (TSSC)".
"""

from __future__ import annotations
import numpy as np

__all__ = [
    "epsilon_star",
    "mean_cv_form",
    "active_support",
    "relu",
    "generalized_inverse_degree",
    "receiver_coupling",
    "sender_coupling",
    "field_step",
    "run_field",
    "clip_interaction_invariant",
    "rank1_als_weighted",
]

# ---------------------------------------------------------------------------
# Self-consistency operator  (paper §5.5–§5.7)
# ---------------------------------------------------------------------------

def epsilon_star(x: np.ndarray) -> float:
    r"""Canonical self-consistency level (paper §5.5, eq. for varepsilon*_act).

    epsilon*(X) = sum_i x_i^2 / sum_i x_i  =  ||x||_2^2 / ||x||_1

    Belongs to the inverse-participation-ratio / Simpson-index family.
    Defined for a non-negative field x with sum(x) > 0; returns 0.0 for the
    all-zero field (generalized-inverse convention used elsewhere in the paper).
    """
    x = np.asarray(x, dtype=float)
    s1 = x.sum()
    if s1 <= 0.0:
        return 0.0
    s2 = (x * x).sum()
    return float(s2 / s1)


def mean_cv_form(x: np.ndarray) -> float:
    r"""Closed form of epsilon* via descriptive statistics (paper §5.7):

        epsilon*(X) = x_bar * (1 + CV^2),   CV = sigma / x_bar  (population sigma).

    Note: this identity requires the POPULATION standard deviation (ddof=0),
    because it derives from  E[X^2] = sigma^2 + mu^2  with mu = x_bar.
    Provided as an independent computation to cross-check `epsilon_star`.
    """
    x = np.asarray(x, dtype=float)
    mu = x.mean()
    if mu <= 0.0:
        return 0.0
    sigma = x.std(ddof=0)           # population std — required by the identity
    cv = sigma / mu
    return float(mu * (1.0 + cv * cv))


def active_support(x: np.ndarray) -> np.ndarray:
    r"""Active Support  A*(X) = { i : x_i >= epsilon*(X) }  (paper §5.5).

    Returns a boolean mask over the entries of x.
    """
    x = np.asarray(x, dtype=float)
    eps = epsilon_star(x)
    return x >= eps


# ---------------------------------------------------------------------------
# Field dynamics  (paper §9)
# ---------------------------------------------------------------------------

def relu(v: np.ndarray) -> np.ndarray:
    """Observable field  Psi = ReLU(V) = max(0, V)  (epistemic schism, §6/§9)."""
    return np.maximum(0.0, np.asarray(v, dtype=float))


def generalized_inverse_degree(M: np.ndarray) -> np.ndarray:
    r"""Diagonal of D_M^+ : reciprocal row-sum of M, 0 where the row-sum is 0.

    A node with no geometric degree produces no singularity and needs no
    artificial regularizer (paper §9): it simply has no channel to emit.
    """
    M = np.asarray(M, dtype=float)
    d = M.sum(axis=1)
    dinv = np.where(d > 0.0, 1.0 / d, 0.0)
    return dinv


def receiver_coupling(M: np.ndarray, W: np.ndarray) -> np.ndarray:
    r"""Canonical coupling  J = D_M^+ W   (RECEIVER normalization, paper §9).

    This is the load-bearing operator: dividing the incoming signal by the
    receiver's own topological degree turns hubs into dissipative sinks.
    """
    dinv = generalized_inverse_degree(M)
    return dinv[:, None] * np.asarray(W, dtype=float)


def sender_coupling(M: np.ndarray, W: np.ndarray) -> np.ndarray:
    r"""Counterfactual coupling  J = W D_M^+   (SENDER normalization).

    Used ONLY in the hub-hijacking experiment as the failing control: it lets
    high-degree nodes broadcast and hijack the field. Not part of the theory.
    """
    dinv = generalized_inverse_degree(M)
    return np.asarray(W, dtype=float) * dinv[None, :]


def field_step(V, S, J, gamma, alpha, beta):
    r"""One step of the field map (paper §9):

        V^{t+1} = (1 - gamma) V + alpha S + beta J Psi,   Psi = ReLU(V).
    """
    Psi = relu(V)
    return (1.0 - gamma) * np.asarray(V, dtype=float) \
        + alpha * np.asarray(S, dtype=float) \
        + beta * (J @ Psi)


def run_field(S, J, gamma, alpha, beta, steps=2000, V0=None, tol=1e-12):
    """Iterate the field map to its fixed point. Returns (V, Psi, n_iter)."""
    S = np.asarray(S, dtype=float)
    V = np.zeros_like(S) if V0 is None else np.array(V0, dtype=float)
    for k in range(1, steps + 1):
        V_new = field_step(V, S, J, gamma, alpha, beta)
        if np.max(np.abs(V_new - V)) < tol:
            V = V_new
            return V, relu(V), k
        V = V_new
    return V, relu(V), steps


def clip_interaction_invariant(M: np.ndarray, W: np.ndarray) -> np.ndarray:
    r"""Enforce the contraction invariant  |w_ij| <= m_ij  (paper, dual medium).

    Clipping after each consolidation is what keeps ||J||_inf <= 1.
    """
    M = np.asarray(M, dtype=float)
    W = np.asarray(W, dtype=float)
    return np.clip(W, -M, M)


# ---------------------------------------------------------------------------
# Weighted rank-1 NMF via ALS  (paper §8.2.4)
# ---------------------------------------------------------------------------

def rank1_als_weighted(A, beta, n_iter=200, eps=1e-12, seed=0):
    r"""Weighted rank-1 non-negative factorization by alternating least squares.

    Minimizes   sum_i beta_i * || a_i - rho_i * R ||^2   with  R >= 0, rho_i >= 0.

    Closed-form ALS updates with explicit denominators (paper §8.2.4):
        rho_i = max(0, <a_i, R> / <R, R>)
        R     = max(0, sum_i beta_i rho_i a_i / sum_i beta_i rho_i^2)

    Generalized-inverse convention: if sum_i beta_i rho_i^2 == 0 at init, the
    latent hypothesis is orthogonal to the evidence and the candidate is
    rejected natively (returns the current R unchanged) — a diagnostic failure,
    not a numerical error.

    Returns (R, rho, errors) where `errors` is the weighted SSE per iteration
    (length n_iter + 1, including the initial value).
    """
    rng = np.random.default_rng(seed)
    A = np.asarray(A, dtype=float)
    beta = np.asarray(beta, dtype=float)
    n_ep, n_nodes = A.shape

    R = np.abs(rng.standard_normal(n_nodes)) + 0.1
    rho = np.abs(rng.standard_normal(n_ep)) + 0.1

    def wsse(R, rho):
        diff = A - rho[:, None] * R[None, :]
        return float(np.sum(beta[:, None] * diff * diff))

    errors = [wsse(R, rho)]
    for _ in range(n_iter):
        # rho update
        rr = float(R @ R)
        if rr <= eps:
            errors.append(wsse(R, rho))
            continue
        rho = np.maximum(0.0, (A @ R) / rr)
        # R update
        den = float(np.sum(beta * rho * rho))
        if den <= eps:                      # orthogonal to evidence -> reject
            errors.append(wsse(R, rho))
            continue
        num = np.sum(beta[:, None] * rho[:, None] * A, axis=0)
        R = np.maximum(0.0, num / den)
        errors.append(wsse(R, rho))

    return R, rho, np.array(errors)
