"""
Experiment 2 — Selectivity of epsilon* as a function of the field morphology
(paper §5.7 and the "Multiscale Self-consistency" gate, §8.10).

Claim under test:
    The active support A*(X) = {x >= epsilon*(X)} is SELECTIVE for a focused
    field (it keeps the few peak nodes and cuts the dissipative tail) and only
    "floods" (keeps a large fraction of nodes) when the field is genuinely
    diffuse. This selectivity is robust across the whole dynamic regime
    r = beta / gamma, because epsilon* reads the field morphology, not the
    absolute scale.

Setup:
    We build fields with a controllable concentration (a few peaks over a
    uniform background), drive them through the field map at several values of
    r = beta/gamma, and measure the active-support fraction |A*| / N.
    A focused field should yield a SMALL fraction; a flat field a LARGE one.
"""

from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from tssc_core import (
    epsilon_star, active_support, receiver_coupling,
    clip_interaction_invariant, run_field,
)

FIG_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")


def _random_medium(n, density, seed):
    """Symmetric non-negative M (zero diagonal) and a compatible signed W."""
    rng = np.random.default_rng(seed)
    M = np.abs(rng.standard_normal((n, n)))
    mask = rng.random((n, n)) < density
    M = M * mask
    M = np.triu(M, 1)
    M = M + M.T                              # symmetric, zero diagonal
    W = rng.standard_normal((n, n))
    W = np.triu(W, 1)
    W = W + W.T
    W = clip_interaction_invariant(M, W)     # |w_ij| <= m_ij
    return M, W


def _focused_source(n, n_peaks, peak, background, rng):
    s = np.full(n, background, dtype=float)
    idx = rng.choice(n, size=n_peaks, replace=False)
    s[idx] = peak
    return s


def run(n=60, density=0.3, seed=0):
    """Return (r_values, frac_focused, frac_diffuse) active-support fractions."""
    rng = np.random.default_rng(seed)
    M, W = _random_medium(n, density, seed)
    J = receiver_coupling(M, W)

    gamma = 0.5
    r_values = np.linspace(0.05, 0.95, 19)   # r = beta/gamma  (beta < gamma)
    frac_focused = []
    frac_diffuse = []

    for r in r_values:
        beta = r * gamma
        alpha = 1.0
        # focused field: a few strong peaks over weak background
        s_focus = _focused_source(n, n_peaks=3, peak=10.0, background=0.1, rng=rng)
        _, psi_f, _ = run_field(s_focus, J, gamma, alpha, beta)
        frac_focused.append(active_support(psi_f).mean())

        # diffuse field: near-uniform input (CV -> 0)
        s_diff = np.ones(n) + 0.01 * rng.standard_normal(n)
        _, psi_d, _ = run_field(s_diff, J, gamma, alpha, beta)
        frac_diffuse.append(active_support(psi_d).mean())

    return r_values, np.array(frac_focused), np.array(frac_diffuse)


def make_figure(r, ff, fd, path):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(r, ff, "o-", label="focused field (few peaks)")
    ax.plot(r, fd, "s--", label="diffuse field (near-uniform)")
    ax.set_xlabel(r"$r = \beta / \gamma$")
    ax.set_ylabel(r"active-support fraction  $|A^*| / N$")
    ax.set_ylim(0, 1.05)
    ax.set_title("Exp. 2 — epsilon* stays selective for focused input, floods only when diffuse")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def main():
    r, ff, fd = run()
    print("Experiment 2 — selectivity of epsilon* across r = beta/gamma")
    print(f"  focused fraction  : min={ff.min():.3f}  max={ff.max():.3f}  mean={ff.mean():.3f}")
    print(f"  diffuse fraction  : min={fd.min():.3f}  max={fd.max():.3f}  mean={fd.mean():.3f}")
    # focused must stay clearly selective; diffuse must stay clearly broader
    ok = (ff.max() < 0.30) and (fd.mean() > ff.mean() + 0.30)
    print(f"  focused selective & diffuse broader: {ok}")
    os.makedirs(FIG_DIR, exist_ok=True)
    out = os.path.join(FIG_DIR, "exp2_selectivity.png")
    make_figure(r, ff, fd, out)
    print(f"  figure            : {os.path.relpath(out)}")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
