"""
Experiment 3 — Hub-hijacking: the Emergent Asymmetry of receiver normalization
(paper §9 and the discussion of J = D_M^+ W as the concentrating mechanism).

Claim under test:
    With RECEIVER normalization  J = D_M^+ W, a small genuine source survives
    and high-degree background "hubs" do NOT hijack the observable field.
    With the counterfactual SENDER normalization  J = W D_M^+, the same hubs
    broadcast and capture the field, expelling the source.
    Crucially, both couplings are built to share (approximately) the same
    spectral radius, so the difference is an effect of CONCENTRATION, not of
    divergence / instability.

Construction:
    N nodes split into a small "source" cluster and several "hub" nodes that
    are densely connected to a large background. We drive a focused source on
    the source cluster, run the field to its fixed point under each coupling,
    and count how many of the H hubs end up dominating the field
    (their activation exceeds the source's). Receiver -> 0/H, Sender -> H/H.
"""

from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from tssc_core import (
    receiver_coupling, sender_coupling, clip_interaction_invariant, run_field,
)

FIG_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")


def build_scene(n_hubs=5, n_background=80, seed=0):
    """Return (M, W, source_idx, hub_idx).

    Geometry that exhibits the phenomenon: a single source node connected to
    every hub (so energy can propagate), and hubs each connected to ~95% of a
    large background (so hubs have very high topological degree). It is this
    degree that receiver normalization divides away and sender normalization
    does not.
    """
    rng = np.random.default_rng(seed)
    n = 1 + n_hubs + n_background
    source_idx = np.array([0])
    hub_idx = np.arange(1, 1 + n_hubs)
    bg_idx = np.arange(1 + n_hubs, n)

    M = np.zeros((n, n))
    # source -> every hub (a propagation path into the hub region)
    for h in hub_idx:
        M[0, h] = 1.0
    # each hub -> ~95% of the background (high degree)
    for h in hub_idx:
        targets = rng.choice(bg_idx, size=int(0.95 * len(bg_idx)), replace=False)
        for t in targets:
            M[h, t] = 1.0

    M = np.triu(M, 1)
    M = M + M.T                               # symmetric, zero diagonal

    # signed interaction at the invariant ceiling: W = M (all excitatory, |w|<=m)
    W = clip_interaction_invariant(M, M.copy())
    return M, W, source_idx, hub_idx


def _match_spectral_radius(J_ref, J):
    """Scale J so that rho(J) == rho(J_ref). Returns the scaled J."""
    r_ref = np.max(np.abs(np.linalg.eigvals(J_ref)))
    r = np.max(np.abs(np.linalg.eigvals(J)))
    if r == 0:
        return J
    return J * (r_ref / r)


def run(seed=0):
    M, W, source_idx, hub_idx = build_scene(seed=seed)

    J_recv = receiver_coupling(M, W)
    J_send = sender_coupling(M, W)

    # equalize spectral radius so the comparison isolates concentration
    J_send = _match_spectral_radius(J_recv, J_send)
    rho_recv = float(np.max(np.abs(np.linalg.eigvals(J_recv))))
    rho_send = float(np.max(np.abs(np.linalg.eigvals(J_send))))

    # focused source on the source cluster only
    n = M.shape[0]
    S = np.zeros(n)
    S[source_idx] = 5.0

    gamma = 0.6
    beta = 0.95 * gamma           # below the L-inf contraction bound for receiver
    alpha = 1.0

    _, psi_recv, _ = run_field(S, J_recv, gamma, alpha, beta, steps=8000)
    _, psi_send, _ = run_field(S, J_send, gamma, alpha, beta, steps=8000)

    src_recv = psi_recv[source_idx].max()
    src_send = psi_send[source_idx].max()

    hubs_recv = int(np.sum(psi_recv[hub_idx] > src_recv))
    hubs_send = int(np.sum(psi_send[hub_idx] > src_send))

    return {
        "n_hubs": len(hub_idx),
        "hubs_hijacking_receiver": hubs_recv,
        "hubs_hijacking_sender": hubs_send,
        "rho_receiver": rho_recv,
        "rho_sender": rho_send,
        "psi_recv": psi_recv,
        "psi_send": psi_send,
        "source_idx": source_idx,
        "hub_idx": hub_idx,
    }


def make_figure(res, path):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
    for ax, key, title in [
        (axes[0], "psi_recv", "Receiver  J = $D_M^+ W$  (hubs sterilized)"),
        (axes[1], "psi_send", "Sender  J = $W D_M^+$  (hubs hijack)"),
    ]:
        psi = res[key]
        colors = np.array(["#bbbbbb"] * len(psi), dtype=object)
        colors[res["source_idx"]] = "#1f77b4"   # source = blue
        colors[res["hub_idx"]] = "#d62728"       # hubs = red
        ax.bar(np.arange(len(psi)), psi, color=list(colors))
        ax.set_title(title)
        ax.set_xlabel("node index")
    axes[0].set_ylabel(r"observable field $\Psi$")
    fig.suptitle("Exp. 3 — same spectral radius; only sender normalization lets hubs (red) hijack the field")
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def main():
    res = run()
    H = res["n_hubs"]
    print("Experiment 3 — hub-hijacking (receiver vs sender normalization)")
    print(f"  hubs hijacking, RECEIVER J=D_M^+W : {res['hubs_hijacking_receiver']}/{H}  (expected 0/{H})")
    print(f"  hubs hijacking, SENDER   J=WD_M^+ : {res['hubs_hijacking_sender']}/{H}  (expected {H}/{H})")
    print(f"  spectral radius receiver          : {res['rho_receiver']:.4f}")
    print(f"  spectral radius sender (matched)  : {res['rho_sender']:.4f}")
    ok = (res["hubs_hijacking_receiver"] == 0) and (res["hubs_hijacking_sender"] == H)
    print(f"  receiver 0/H and sender H/H       : {ok}")
    os.makedirs(FIG_DIR, exist_ok=True)
    out = os.path.join(FIG_DIR, "exp3_hub_hijacking.png")
    make_figure(res, out)
    print(f"  figure                            : {os.path.relpath(out)}")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
