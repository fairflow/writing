#!/usr/bin/env python3
"""Fix the remaining specific lines by wrapping at sensible points."""

import textwrap

file_path = '_posts/2025-11-05-cultural-theory-summary.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 1594 (index 1593): wrap the bullet point
if len(lines) > 1593 and len(lines[1593].rstrip()) > 120:
    line = lines[1593].rstrip()
    if line.startswith('- I apologize'):
        # Split after "implementation,"
        lines[1593] = ('- I apologize for any confusion caused by the notation—these are *suggested* formalizations for computational\n'
                       '  implementation, and you are correct that care must be taken to distinguish between individuals and cultural states.\n')

# Line 1638 (index 1637): wrap the bullet point  
if len(lines) > 1637 and len(lines[1637].rstrip()) > 120:
    line = lines[1637].rstrip()
    if line.startswith('- For computational'):
        lines[1637] = ('- For computational models (e.g., agent-based or statistical mechanics analogs), this facilitates clarity,\n'
                       '  extensibility, and implementation.\n')

# Line 1653 (index 1652): wrap the bullet point
if len(lines) > 1652 and len(lines[1652].rstrip()) > 120:
    line = lines[1652].rstrip()
    if line.startswith('- $E(i,'):
        lines[1652] = ('- $E(i, \\sigma)$ can flexibly incorporate all contextual factors: individual predispositions, neighbor\n'
                       '  influence, event-driven surprise, even additional dimensions (age, context etc.).\n')

# Line 1654 (index 1653): wrap the bullet point
if len(lines) > 1653 and len(lines[1653].rstrip()) > 120:
    line = lines[1653].rstrip()
    if line.startswith('- Agent-based'):
        lines[1653] = ('- Agent-based and systems dynamics implementations benefit from this flexibility—particularly if you extend\n'
                       '  Cultural Theory to multi-context or multi-dimensional models.\n')

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Fixed specific lines")
