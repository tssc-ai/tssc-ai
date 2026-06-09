"""
Experiment 4 — The L-infinity contraction bound (paper §9, §9.1).

Claim under test:
    For any non-negative symmetric M (zero diagonal) and any signed W with
    |w_ij| <= m_ij, the receiver coupling  J = D_M^+ W  satisfies
        ||J||_inf <= 1        (max absolute row sum)
    Consequently the field map is a contraction whenever  beta < gamma, since
        (1 - gamma) + beta * ||J||_inf <= 1 - (gamma - beta) < 1.

We test the inequality over thousands of random media, then confirm the
practical consequence: iterating the field with beta < gamma converges, while
beta > gamma can diverge.
"""

from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from tssc_core import (
    receiver_coupling, clip_interaction_invariant, run_field, field_step, relu,
)

FIG_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")


def inf_norm(J):
    return float(np.abs(J).sum(axis=1).max())


def run_bound(n_trials=4000, seed=0):
    """Return the array of ||J||_inf over random valid media."""
    rng = np.random.default_rng(seed)
    norms = np.empty(n_trials)
    for i in range(n_trials):
        n = int(rng.integers(2, 30))
        M = np.abs(rng.standard_normal((n, n)))
        M = np.triu(M, 1)
        M = M + M.T
        W = rng.standard_normal((n, n))
        W = np.triu(W, 1)
        W = W + W.T
        W = clip_interaction_invariant(M, W)
        J = receiver_coupling(M, W)
        norms[i] = inf_norm(J)
    return norms


def run_convergence(seed=0):
    """Field-norm trajectories for beta<gamma (stable) vs beta>gamma (unstable)."""
    rng = np.random.default_rng(seed)
    n = 40
    M = np.abs(rng.standard_normal((n, n)))
    M = np.triu(M, 1); M = M + M.T
    W = clip_interaction_invariant(M, M.copy())   # W = M, ||J||_inf = 1
    J = receiver_coupling(M, W)
    S = rng.random(n)

    gamma = 0.5
    steps = 120

    def trajectory(beta):
        V = np.zeros(n)
        norms = []
        for _ in range(steps):
            V = field_step(V, S, J, gamma, alpha=1.0, beta=beta)
            norms.append(np.linalg.norm(relu(V)))
        return np.array(norms)

    stable = trajectory(beta=0.45 * gamma)   # beta < gamma
    unstable = trajectory(beta=1.6 * gamma)   # beta > gamma (and > 1/||J||... )
    return stable, unstable, gamma


def make_figure(norms, stable, unstable, path):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))

    axes[0].hist(norms, bins=40)
    axes[0].axvline(1.0, color="r", ls="--", lw=1.5, label=r"bound $\|J\|_\infty = 1$")
    axes[0].set_xlabel(r"$\|J\|_\infty$ (max abs row sum)")
    axes[0].set_ylabel("count")
    axes[0].set_title(f"||J||_inf never exceeds 1\n(max observed = {norms.max():.4f})")
    axes[0].legend()

    axes[1].plot(stable, label=r"$\beta < \gamma$ (contraction)")
    axes[1].plot(unstable, label=r"$\beta > \gamma$ (divergence)")
    axes[1].set_yscale("log")
    axes[1].set_xlabel("iteration")
    axes[1].set_ylabel(r"$\|\Psi\|_2$")
    axes[1].set_title("Field converges iff beta < gamma")
    axes[1].legend()

    fig.suptitle("Exp. 4 — L-infinity contraction bound")
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def main():
    norms = run_bound()
    stable, unstable, gamma = run_convergence()
    violations = int(np.sum(norms > 1.0 + 1e-12))
    print("Experiment 4 — L-infinity contraction bound")
    print(f"  trials                         : {len(norms)}")
    print(f"  max ||J||_inf                  : {norms.max():.6f}")
    print(f"  violations of ||J||_inf <= 1   : {violations}")
    print(f"  stable run  (beta<gamma) final : {stable[-1]:.4e}")
    print(f"  unstable run (beta>gamma) final: {unstable[-1]:.4e}")
    ok = (violations == 0) and (stable[-1] < unstable[-1])
    print(f"  bound holds & stability matches: {ok}")
    os.makedirs(FIG_DIR, exist_ok=True)
    out = os.path.join(FIG_DIR, "exp4_contraction.png")
    make_figure(norms, stable, unstable, out)
    print(f"  figure                         : {os.path.relpath(out)}")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
