"""
Unit IV - Is 2Z (the even integers) a subgroup of (Z, +)?

Computational check over a finite window [-N, N] (a proof needs algebra; the
code verifies each property on every pair/element in the window, and a
counterexample test shows the checks can fail, e.g. for the odd integers).
Standard library only.
"""

N = 50  # window: integers from -N to N


def in_2Z(x):
    return x % 2 == 0


def check_subgroup(name, member, window):
    H = [x for x in window if member(x)]
    results = {}

    # Non-empty and contains identity 0
    results["non-empty"] = len(H) > 0
    results["identity 0 in H"] = member(0)

    # Closure under +  (only test pairs whose sum stays inside the window)
    closure_fail = [(a, b) for a in H for b in H
                    if abs(a + b) <= N and not member(a + b)]
    results["closure under +"] = not closure_fail

    # Inverses: -a in H for every a in H
    inverse_fail = [a for a in H if not member(-a)]
    results["inverses (-a in H)"] = not inverse_fail

    # One-step subgroup test: a - b in H for all a, b in H
    onestep_fail = [(a, b) for a in H for b in H
                    if abs(a - b) <= N and not member(a - b)]
    results["subgroup test (a - b in H)"] = not onestep_fail

    print(f"=== {name} ===")
    print(f"Elements tested in window [-{N}, {N}]: {len(H)}")
    for k, v in results.items():
        print(f"  {k:<30}: {v}")
    if closure_fail:
        print("  closure counterexample:", closure_fail[0])
    if inverse_fail:
        print("  inverse counterexample:", inverse_fail[0])
    print("  => SUBGROUP" if all(results.values()) else "  => NOT a subgroup")
    print()
    return all(results.values())


if __name__ == "__main__":
    window = range(-N, N + 1)

    # Sample demonstration
    a, b = 6, -14
    print(f"Example: a = {a}, b = {b}  ->  a - b = {a - b}, even? {in_2Z(a - b)}")
    print(f"Example: 2*k form: {a} = 2*{a // 2}, {b} = 2*{b // 2}, "
          f"a - b = 2*({a // 2} - ({b // 2})) = 2*{a // 2 - b // 2}")
    print()

    check_subgroup("2Z (even integers)", in_2Z, window)
    # Contrast: odd integers fail (no identity, not closed)
    check_subgroup("Odd integers (contrast)", lambda x: x % 2 != 0, window)
    # Contrast: 2Z union {1} style set fails closure
    check_subgroup("Evens plus the number 1 (contrast)",
                   lambda x: x % 2 == 0 or x == 1, window)
