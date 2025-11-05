#!/usr/bin/env python3
"""
Script to wrap long lines in markdown files while preserving structure.
"""
import re
import sys

def wrap_text(text, max_length):
    """Wrap text to max_length."""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        word_len = len(word) + (1 if current_line else 0)
        if current_length + word_len > max_length and current_line:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += word_len
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

def wrap_line(line, max_length=120):
    """Wrap a line to max_length, trying to break at word boundaries."""
    if len(line) <= max_length:
        return [line]
    
    # Don't wrap certain types of lines
    if line.startswith(('#', '- ', '* ', '>', '|', '```', '    ', '\t')):
        return [line]
    if line.startswith('[^') and ']:' in line:  # Footnote reference
        return [line]
    if line.strip().startswith('<') or line.strip().endswith('>'):  # HTML
        return [line]
    if line.startswith('**') and '**:' in line[:50]:  # Bold definition
        return [line]
    
    # Handle numbered lists with special care
    match = re.match(r'^(\d+\.\s+)', line)
    if match:
        prefix = match.group(1)
        rest = line[len(prefix):]
        if len(line) <= max_length:
            return [line]
        # Wrap the rest with proper indentation
        wrapped = wrap_text(rest, max_length - 3)  # 3 spaces for continuation
        return [prefix + wrapped[0]] + ['   ' + l for l in wrapped[1:]]
    
    # Wrap the line
    words = line.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        word_len = len(word) + (1 if current_line else 0)  # +1 for space
        if current_length + word_len > max_length and current_line:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += word_len
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

def process_file(filepath):
    """Process a markdown file and wrap long lines."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    output = []
    in_code_block = False
    
    for line in lines:
        line = line.rstrip('\n')
        
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            output.append(line)
            continue
        
        # Don't wrap code blocks
        if in_code_block:
            output.append(line)
            continue
        
        # Wrap the line if needed
        wrapped = wrap_line(line)
        output.extend(wrapped)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in output:
            f.write(line + '\n')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <markdown_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    print(f"Processing {filepath}...")
    process_file(filepath)
    print("Done!")
