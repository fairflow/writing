#!/usr/bin/env python3
"""Fix remaining overlong lines in the markdown file."""

import re

def wrap_line(line, max_length=120):
    """Wrap a line if it exceeds max_length."""
    if len(line) <= max_length:
        return line
    
    # Don't wrap URLs, LaTeX, code blocks, or horizontal rules
    if line.strip().startswith(('http', '```', '---', '$$', '<')):
        return line
    if '<!--' in line or '$' in line:
        return line
    
    # For bullet lists  
    if line.strip().startswith(('- ', '* ')):
        indent = len(line) - len(line.lstrip())
        prefix = line[:indent + 2]  # "- " or "* "
        rest = line[indent + 2:].strip()
        
        # If starts with bold
        bold_match = re.match(r'\*\*([^*]+)\*\*:\s*(.+)', rest)
        if bold_match:
            bold_text = bold_match.group(1)
            remaining = bold_match.group(2)
            if len(prefix + f'**{bold_text}**: {remaining}') <= max_length:
                return line
            # Wrap after the bold part
            wrapped = f"{prefix}**{bold_text}**: {remaining[:max_length-len(prefix)-len(bold_text)-6]}\n"
            wrapped += f"{' ' * (indent + 2)}{remaining[max_length-len(prefix)-len(bold_text)-6:]}"
            return wrapped
        
        # Simple wrap
        words = rest.split()
        lines = []
        current = prefix
        for word in words:
            if len(current + word) <= max_length:
                current += word + ' '
            else:
                lines.append(current.rstrip())
                current = ' ' * (indent + 2) + word + ' '
        if current.strip():
            lines.append(current.rstrip())
        return '\n'.join(lines)
    
    # Simple word wrap for other lines
    words = line.split()
    lines = []
    current = ''
    for word in words:
        if len(current + word) <= max_length:
            current += word + ' '
        else:
            if current:
                lines.append(current.rstrip())
            current = word + ' '
    if current.strip():
        lines.append(current.rstrip())
    return '\n'.join(lines)

def main():
    file_path = '_posts/2025-11-05-cultural-theory-summary.md'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Process specific problem lines
    problem_lines = {
        1589: True,  # 161 chars
        1590: True,  # 210 chars
        1591: True,  # 225 chars
        1635: True,  # 141 chars
        1650: True,  # 184 chars
        1651: True,  # 169 chars
    }
    
    new_lines = []
    i = 0
    while i < len(lines):
        line_num = i + 1
        line = lines[i].rstrip('\n')
        
        if line_num in problem_lines and len(line) > 120:
            wrapped = wrap_line(line)
            new_lines.append(wrapped + '\n')
        else:
            new_lines.append(lines[i])
        i += 1
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Fixed {len(problem_lines)} lines")

if __name__ == '__main__':
    main()
