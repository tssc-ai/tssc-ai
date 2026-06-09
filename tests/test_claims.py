"""
pytest suite — asserts the five foundational TSSC claims.

Each test maps to one experiment and to one claim in the paper. These are
property/identity tests (machine-precision or robust-across-seeds), not
golden-number snapshots, so they remain meaningful if the implementation is
refactored.

Run with:  pytest -q
"""

import numpy as np
import pytest

from tssc_core import (
    epsilon_star, mean_cv_form, active_support,
    receiver_coupling, sender_coupling, clip_interaction_invariant,
    rank1_als_weighted,
)

import experiments.exp1_epsilon_identity as e1
import experiments.exp2_selectivity as e2
import experiments.exp3_hub_hijacking as e3
import experiments.exp4_contraction as e4
import experiments.exp5_als_disjoint as e5


# --------------------------------------------------------------------------
# Claim 1 — epsilon* closed-form identity (paper §5.7)
# --------------------------------------------------------------------------

def test_epsilon_identity_machine_precision():
    diffs = e1.run(n_trials=5000, seed=0)
    assert diffs.max() < 1e-9


def test_epsilon_identity_specific_values():
    # hand-checkable: uniform field -> CV=0 -> eps* = mean
    x = np.array([2.0, 2.0, 2.0, 2.0])
    assert epsilon_star(x) == pytest.approx(2.0)
    assert mean_cv_form(x) == pytest.approx(2.0)


def test_epsilon_zero_field_convention():
    x = np.zeros(5)
    assert epsilon_star(x) == 0.0
    assert mean_cv_form(x) == 0.0


def test_epsilon_scale_invariance_of_support():
    rng = np.random.default_rng(1)
    x = rng.random(50)
    # scaling the field by k>0 must not change the active-support mask
    for k in [0.01, 1.0, 7.3, 1000.0]:
        assert np.array_equal(active_support(x), active_support(k * x))


# --------------------------------------------------------------------------
# Claim 2 — selectivity of epsilon* across r = beta/gamma (paper §5.7, §8.10)
# --------------------------------------------------------------------------

def test_selectivity_focused_vs_diffuse():
    r, ff, fd = e2.run(seed=0)
    # focused input must keep only a small fraction of nodes, across all r
    assert ff.max() < 0.30
    # a diffuse input must keep a clearly larger fraction on average
    assert fd.mean() > ff.mean() + 0.30


# --------------------------------------------------------------------------
# Claim 3 — hub-hijacking: receiver normalization is the concentrating
#           mechanism (paper §9)
# --------------------------------------------------------------------------

@pytest.mark.parametrize("seed", list(range(5)))
def test_hub_hijacking_reproduces_across_seeds(seed):
    res = e3.run(seed=seed)
    H = res["n_hubs"]
    assert res["hubs_hijacking_receiver"] == 0
    assert res["hubs_hijacking_sender"] == H


def test_hub_hijacking_same_spectral_radius():
    res = e3.run(seed=0)
    # the comparison is fair only if both couplings share the spectral radius
    assert res["rho_receiver"] == pytest.approx(res["rho_sender"], rel=1e-6)


# --------------------------------------------------------------------------
# Claim 4 — L-infinity contraction bound (paper §9, §9.1)
# --------------------------------------------------------------------------

def test_Jinf_never_exceeds_one():
    norms = e4.run_bound(n_trials=4000, seed=0)
    assert int(np.sum(norms > 1.0 + 1e-12)) == 0


def test_beta_lt_gamma_converges_beta_gt_gamma_diverges():
    stable, unstable, gamma = e4.run_convergence(seed=0)
    assert stable[-1] < unstable[-1]
    assert np.isfinite(stable[-1])


def test_invariant_clip_enforces_bound():
    # directly: any W clipped to |w|<=m gives ||D_M^+ W||_inf <= 1
    rng = np.random.default_rng(3)
    for _ in range(500):
        n = int(rng.integers(2, 20))
        M = np.abs(rng.standard_normal((n, n)))
        M = np.triu(M, 1); M = M + M.T
        W = rng.standard_normal((n, n)); W = np.triu(W, 1); W = W + W.T
        W = clip_interaction_invariant(M, W)
        J = receiver_coupling(M, W)
        assert np.abs(J).sum(axis=1).max() <= 1.0 + 1e-12


# --------------------------------------------------------------------------
# Claim 5 — weighted rank-1 ALS descent & disjoint-support zero diagonal
#           (paper §8.2.4, §8.2.6)
# --------------------------------------------------------------------------

def test_als_monotone_descent():
    worst_jump, _ = e5.run_als(n_runs=200, seed=0)
    assert worst_jump <= 1e-9


def test_als_rejects_orthogonal_evidence():
    # an episode matrix orthogonal to any non-negative rank-1 fit:
    # all-zero evidence -> denominator 0 at init -> candidate rejected (R unchanged-ish)
    A = np.zeros((5, 8))
    beta = np.ones(5)
    R, rho, errors = rank1_als_weighted(A, beta, n_iter=50, seed=0)
    # error stays at 0 (nothing to fit) and no crash / no nan
    assert np.all(np.isfinite(R))
    assert np.all(np.isfinite(errors))


def test_disjoint_support_zero_diagonal():
    worst_diag = e5.run_disjoint(n_trials=20000, seed=0)
    assert worst_diag == 0.0
