#!/usr/bin/env python3
"""Replace the H1 headers with H2 headers to reduce line length issues."""

file_path = '_posts/2025-11-05-cultural-theory-summary.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the three long H1 headers with H2 headers
replacements = [
    ("# that's a great summary", "## User Question: Mathematical Modelling\n\nThat's a great summary"),
    ("# thanks, but that just makes no sense", "## User Follow-up: Energy Function Definition\n\nThanks, but that just makes no sense"),
    ("# sorry also I didn't read", "## User Clarification: Bivariate Function Notation\n\nSorry also I didn't read"),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old[:50]}...")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
