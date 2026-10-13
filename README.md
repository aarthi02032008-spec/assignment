# Subgroup Test: Is 2Z a Subgroup of (Z, +)? (Unit IV)

A small website and Python program showing that the set of even integers 2Z is a subgroup of the integers under addition.

## Problem Statement

Determine whether the set of even integers 2Z is a subgroup of (Z, +). Justify using the subgroup test and verify the relevant closure and inverse properties computationally.

## Answer

**Yes, 2Z is a subgroup of (Z, +).**

## Justification (One-Step Subgroup Test)

A non-empty subset H of a group G is a subgroup if a - b is in H for all a, b in H.

1. **Non-empty:** 0 = 2*0 is even, so 0 is in 2Z.
2. **Take a, b in 2Z:** a = 2m and b = 2n for some integers m, n.
3. **Apply the test:** a - b = 2m - 2n = 2(m - n), and m - n is an integer, so a - b is in 2Z.
4. **Conclusion:** 2Z is a subgroup of (Z, +).

Derived properties:

| Property | Reason |
|----------|--------|
| Closure | 2m + 2n = 2(m + n) |
| Identity | 0 = 2*0 is in 2Z |
| Inverses | -(2m) = 2(-m) is in 2Z |
| Associativity | Inherited from (Z, +) |

## Python Verification

`subgroup_verify.py` (standard library only) checks, over the window [-50, 50]:

- non-emptiness and the identity 0
- closure under addition
- inverses (-a is in the set for every a)
- the one-step subgroup test (a - b is in the set)

It also runs the same checks on the odd integers and on "evens plus 1", which both fail, to show the checks can detect non-subgroups.

Run it:

```bash
python subgroup_verify.py
```

A finite window only tests finitely many cases, so it supports the result while the algebraic proof above covers all integers.

## Website

Open `index.html` in any browser (no internet or installation needed). It includes the proof, an interactive subgroup-test calculator, a number line, the Python code with its output, and a table of non-examples.

## Project Structure

```
unit4-subgroup-website/
├── index.html           # the website
├── subgroup_verify.py   # Python verification script
└── README.md            # this file
```
