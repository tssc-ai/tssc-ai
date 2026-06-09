"""
Experiment 1 — The epsilon* closed-form identity (paper §5.7).

Claim under test:
    epsilon*(X) = ||X||_2^2 / ||X||_1  ==  x_bar * (1 + CV^2)
holds as an EXACT algebraic identity (agreement to machine precision) for
every non-negative field X with positive mass.

We verify it on thousands of random fields of varying size and scale, and
report the maximum absolute discrepancy between the two computations.
"""

from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from tssc_core import epsilon_star, mean_cv_form

FIG_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")


def run(n_trials: int = 5000, seed: int = 0):
    """Return the array of |epsilon_star - mean_cv_form| over random fields."""
    rng = np.random.default_rng(seed)
    diffs = np.empty(n_trials)
    for i in range(n_trials):
        n = int(rng.integers(2, 200))
        scale = float(rng.random() * 100.0 + 1e-3)
        x = rng.random(n) * scale
        diffs[i] = abs(epsilon_star(x) - mean_cv_form(x))
    return diffs


def make_figure(diffs: np.ndarray, path: str):
    fig, ax = plt.subplots(figsize=(7, 4))
    # diffs can contain exact zeros; clip to a tiny floor for the log axis
    floor = 1e-20
    ax.hist(np.maximum(diffs, floor), bins=40)
    ax.set_xscale("log")
    ax.set_xlabel(r"$|\varepsilon^*_{\mathrm{direct}} - \bar{x}(1+\mathrm{CV}^2)|$")
    ax.set_ylabel("count")
    ax.set_title("Exp. 1 — epsilon* identity holds to machine precision")
    ax.axvline(np.finfo(float).eps, color="k", ls="--", lw=1,
               label=f"machine epsilon = {np.finfo(float).eps:.1e}")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def main():
    diffs = run()
    print("Experiment 1 — epsilon* closed-form identity")
    print(f"  trials               : {len(diffs)}")
    print(f"  max |difference|     : {diffs.max():.3e}")
    print(f"  mean |difference|    : {diffs.mean():.3e}")
    print(f"  machine epsilon      : {np.finfo(float).eps:.3e}")
    ok = diffs.max() < 1e-9
    print(f"  identity holds (<1e-9): {ok}")
    os.makedirs(FIG_DIR, exist_ok=True)
    out = os.path.join(FIG_DIR, "exp1_epsilon_identity.png")
    make_figure(diffs, out)
    print(f"  figure               : {os.path.relpath(out)}")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
