"""
Experiment 5 — Weighted rank-1 ALS and the disjoint-support guarantee
(paper §8.2.4 and §8.2.6).

Two claims under test:

(a) MONOTONE DESCENT. The weighted rank-1 ALS that fits the latent cause's
    spatial profile minimizes  sum_i beta_i ||a_i - rho_i R||^2  without ever
    increasing the weighted error along the iteration (it converges to a
    stationary point of the LOCAL objective).

(b) DISJOINT-SUPPORT ZERO DIAGONAL. The double self-consistent cut produces a
    nucleus K_zeta and an antagonist set A_zeta with DISJOINT supports
    (K ∩ A = empty). The symmetrized cross template
        T = 1/2 (K A^T + A K^T)
    then has an EXACTLY zero diagonal, so migrating the rank-1 component into W
    needs no off-diagonal rectification. We verify diag(T) == 0 over many
    random disjoint pairs.
"""

from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from tssc_core import rank1_als_weighted

FIG_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")


def run_als(n_runs=200, seed=0):
    """Return (max_positive_jump, example_errors) for the ALS descent test."""
    rng = np.random.default_rng(seed)
    worst_jump = -np.inf
    example = None
    for k in range(n_runs):
        n_ep = int(rng.integers(4, 25))
        n_nodes = int(rng.integers(5, 40))
        A = np.abs(rng.standard_normal((n_ep, n_nodes))) * rng.random(n_ep)[:, None]
        beta = rng.random(n_ep)
        _, _, errors = rank1_als_weighted(A, beta, n_iter=120, seed=k)
        jumps = np.diff(errors)
        worst_jump = max(worst_jump, float(jumps.max()))
        if example is None:
            example = errors
    return worst_jump, example


def run_disjoint(n_trials=20000, seed=0):
    """Return the maximum absolute diagonal of the symmetrized cross template."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(n_trials):
        N = int(rng.integers(4, 30))
        perm = rng.permutation(N)
        n_k = int(rng.integers(1, max(2, N // 2)))
        n_a = int(rng.integers(1, max(2, N // 2)))
        k_idx = perm[:n_k]
        a_idx = perm[n_k:n_k + n_a]            # disjoint from k_idx by construction
        K = np.zeros(N); K[k_idx] = rng.random(n_k)
        Am = np.zeros(N); Am[a_idx] = rng.random(n_a)
        T = 0.5 * (np.outer(K, Am) + np.outer(Am, K))
        worst = max(worst, float(np.abs(np.diag(T)).max()))
    return worst


def make_figure(example_errors, path):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(example_errors, "o-", ms=3)
    ax.set_xlabel("ALS iteration")
    ax.set_ylabel("weighted SSE")
    ax.set_title("Exp. 5 — weighted rank-1 ALS: weighted error is non-increasing")
    ax.set_yscale("log")
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def main():
    worst_jump, example = run_als()
    worst_diag = run_disjoint()
    print("Experiment 5 — weighted rank-1 ALS & disjoint-support template")
    print(f"  (a) max positive error jump over all ALS steps : {worst_jump:.3e}")
    print(f"      (<= machine tolerance means monotone descent)")
    print(f"  (b) max |diag(T)| over disjoint pairs          : {worst_diag:.3e}")
    print(f"      (exactly 0 means no off-diagonal rectification needed)")
    ok = (worst_jump <= 1e-9) and (worst_diag == 0.0)
    print(f"  monotone descent & zero diagonal               : {ok}")
    os.makedirs(FIG_DIR, exist_ok=True)
    out = os.path.join(FIG_DIR, "exp5_als_descent.png")
    make_figure(example, out)
    print(f"  figure                                         : {os.path.relpath(out)}")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
