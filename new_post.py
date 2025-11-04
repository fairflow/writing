#!/usr/bin/env python3
"""
Script to automate the process of creating a new blog post.

This script:
1. Creates a new post file with proper Jekyll front matter (including permalink)
2. Opens the file in the user's default editor for content addition
3. After editing, creates a new branch and pull request (optional)

Usage:
    python3 new_post.py "My Post Title"
    python3 new_post.py "My Post Title" --categories "ai ml"
    python3 new_post.py "My Post Title" --create-pr
"""

import sys
import os
import argparse
import time
from datetime import datetime
import subprocess
import re


def slugify(text):
    """Convert text to a URL-friendly slug."""
    # Convert to lowercase
    text = text.lower()
    # Replace spaces and special characters with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def create_post_file(title, categories=None, permalink=None):
    """Create a new post file with Jekyll front matter."""
    # Generate filename
    today = datetime.now()
    date_str = today.strftime('%Y-%m-%d')
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join('_posts', filename)
    
    # Check if file already exists
    if os.path.exists(filepath):
        print(f"Error: File {filepath} already exists!")
        return None
    
    # Generate permalink if not provided
    if permalink is None:
        permalink = f"/{slug}/"
    elif not permalink.startswith('/'):
        permalink = f"/{permalink}"
    if not permalink.endswith('/'):
        permalink = f"{permalink}/"
    
    # Default categories
    if categories is None:
        categories = "ai"
    
    # Create front matter
    # Get timezone offset in format +0000
    tz_offset = time.strftime('%z')
    if not tz_offset:
        tz_offset = '+0000'
    
    front_matter = f"""---
layout: post
title: "{title}"
date: {today.strftime('%Y-%m-%d %H:%M:%S')} {tz_offset}
categories: {categories}
permalink: {permalink}
---

"""
    
    # Write the file
    with open(filepath, 'w') as f:
        f.write(front_matter)
    
    print(f"Created new post file: {filepath}")
    return filepath


def open_in_editor(filepath):
    """Open the file in the user's default editor."""
    # Try to get the editor from environment variables
    editor = os.environ.get('EDITOR') or os.environ.get('VISUAL')
    
    if editor:
        print(f"Opening {filepath} in {editor}...")
        try:
            subprocess.run([editor, filepath], check=True)
        except subprocess.CalledProcessError:
            print(f"Error: Could not open file in {editor}")
            return False
    else:
        # Try common editors
        for editor_cmd in ['nano', 'vim', 'vi']:
            try:
                subprocess.run(['which', editor_cmd], check=True, 
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"Opening {filepath} in {editor_cmd}...")
                subprocess.run([editor_cmd, filepath], check=True)
                break
            except subprocess.CalledProcessError:
                continue
        else:
            print(f"No editor found. Please edit the file manually: {filepath}")
            return False
    
    return True


def create_branch_and_pr(filepath, title):
    """Create a new branch and pull request for the post."""
    slug = slugify(title)
    branch_name = f"post/{slug}"
    
    try:
        # Check if there are changes to commit
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        
        if not result.stdout.strip():
            print("No changes to commit.")
            return False
        
        # Check if we're already on a feature branch
        result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                              capture_output=True, text=True, check=True)
        current_branch = result.stdout.strip()
        
        # If we're not on main/master, just commit to current branch
        if current_branch not in ['main', 'master']:
            print(f"Currently on branch: {current_branch}")
            print("Committing changes to current branch...")
            
            # Add the file
            subprocess.run(['git', 'add', filepath], check=True)
            
            # Commit the changes
            commit_message = f"Add new post: {title}"
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            
            print(f"\nChanges committed to branch {current_branch}")
            print("To push your changes, run:")
            print(f"  git push origin {current_branch}")
            return True
        
        # We're on main/master, create a new branch
        print(f"Creating branch: {branch_name}")
        subprocess.run(['git', 'checkout', '-b', branch_name], check=True)
        
        # Add the file
        subprocess.run(['git', 'add', filepath], check=True)
        
        # Commit the changes
        commit_message = f"Add new post: {title}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        
        # Push the branch
        print(f"Pushing branch {branch_name} to origin...")
        subprocess.run(['git', 'push', '-u', 'origin', branch_name], check=True)
        
        # Create pull request using gh CLI if available
        try:
            subprocess.run(['which', 'gh'], check=True, 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("Creating pull request...")
            pr_body = f"This PR adds a new blog post: {title}"
            subprocess.run(['gh', 'pr', 'create', 
                          '--title', f"Add post: {title}",
                          '--body', pr_body], check=True)
            print("Pull request created successfully!")
        except subprocess.CalledProcessError:
            print("\nNote: 'gh' CLI not found. Please create the pull request manually:")
            print(f"  Branch: {branch_name}")
            print(f"  Title: Add post: {title}")
            print("\nOr visit: https://github.com/fairflow/writing/compare")
            
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Create a new blog post with Jekyll front matter',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "My New Post"
  %(prog)s "My New Post" --categories "ai ml"
  %(prog)s "My New Post" --permalink "/custom-url/"
  %(prog)s "My New Post" --create-pr
  %(prog)s "My New Post" --categories "ai ml" --create-pr
        """
    )
    
    parser.add_argument('title', help='Title of the blog post')
    parser.add_argument('--categories', '-c', 
                       help='Space-separated categories (default: "ai")')
    parser.add_argument('--permalink', '-p',
                       help='Custom permalink (default: generated from title)')
    parser.add_argument('--create-pr', action='store_true',
                       help='Create a branch and pull request after editing')
    parser.add_argument('--no-edit', action='store_true',
                       help='Skip opening the file in an editor')
    
    args = parser.parse_args()
    
    # Create the post file
    filepath = create_post_file(args.title, args.categories, args.permalink)
    
    if filepath is None:
        return 1
    
    # Open in editor unless --no-edit is specified
    if not args.no_edit:
        print("\nThe file is ready for editing.")
        print("Add your content below the front matter (after the '---' line).")
        print("Save and close the editor when done.\n")
        open_in_editor(filepath)
    
    # Create branch and PR if requested
    if args.create_pr:
        print("\nCreating branch and pull request...")
        create_branch_and_pr(filepath, args.title)
    else:
        print("\nPost created successfully!")
        print(f"File: {filepath}")
        print("\nTo create a pull request later, run:")
        print(f"  git add {filepath}")
        print(f"  git commit -m 'Add new post: {args.title}'")
        print(f"  git push")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
