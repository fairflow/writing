#!/usr/bin/env python3
"""Wrap the three paragraphs with math Unicode at sensible break points."""

file_path = '_posts/2025-11-05-cultural-theory-summary.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 1453: Split after "analysis."
if len(lines) > 1452:
    old = lines[1452].rstrip()
    if old.startswith("That's a great summary"):
        lines[1452] = ("That's a great summary of the different types of mathematical modelling and analysis. One niggle:\n"
                       "P(σi∣{σj}j=i)=∑σ′exp(−βEi(σ′))exp(−βEi(σi)) [apologies for the missing symbols: I cut and pasted from the\n"
                       "equation as you presented it]\n")

# Line 1550: Split after "sense."
if len(lines) > 1549:
    old = lines[1549].rstrip()
    if old.startswith("Thanks, but that just makes no sense"):
        lines[1549] = ("Thanks, but that just makes no sense. Individuals are distinct from cultural states and E_j is not defined\n"
                       "for cultural states. Is this an error of yours or are the equations copied from a cited source please?\n")

# Line 1627: Split into multiple lines
if len(lines) > 1626:
    old = lines[1626].rstrip()
    if old.startswith("Sorry also I didn't read"):
        lines[1626] = ("Sorry also I didn't read the previous section well enough where you defined σ_i and E_i. But E could well be\n"
                       "a general function E(i,σ) which takes two parameters: 1 the individual i and 2 the state in which i could be\n"
                       "found. Then the notation E_i(σ_i) is redundant, you don't need a family of functions if you allow a bivariate\n"
                       "function\n")

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Wrapped the three paragraphs")
