"""Run all five foundational experiments and report pass/fail."""
import importlib
import sys

EXPERIMENTS = [
    "experiments.exp1_epsilon_identity",
    "experiments.exp2_selectivity",
    "experiments.exp3_hub_hijacking",
    "experiments.exp4_contraction",
    "experiments.exp5_als_disjoint",
]


def main():
    results = {}
    for name in EXPERIMENTS:
        print("=" * 70)
        mod = importlib.import_module(name)
        results[name] = bool(mod.main())
        print()
    print("=" * 70)
    print("SUMMARY")
    for name, ok in results.items():
        short = name.split(".")[-1]
        print(f"  {short:24s} {'PASS' if ok else 'FAIL'}")
    all_ok = all(results.values())
    print("=" * 70)
    print("ALL EXPERIMENTS PASSED" if all_ok else "SOME EXPERIMENTS FAILED")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
