#!/usr/bin/env python3
"""
Simple tests for the new_post.py script.
"""

import os
import sys
import subprocess
import tempfile
import shutil
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the functions we want to test
from new_post import slugify, create_post_file


def test_slugify():
    """Test the slugify function."""
    assert slugify("My New Post") == "my-new-post"
    assert slugify("Test with Special!@# Characters") == "test-with-special-characters"
    assert slugify("Multiple   Spaces") == "multiple-spaces"
    assert slugify("Title-With-Hyphens") == "title-with-hyphens"
    print("✓ slugify tests passed")


def test_create_post_file():
    """Test creating a post file."""
    # Create a temporary directory
    original_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    
    try:
        os.chdir(temp_dir)
        os.makedirs('_posts')
        
        # Test basic post creation
        filepath = create_post_file("Test Post", "testing", "/test-permalink/")
        assert filepath is not None
        assert os.path.exists(filepath)
        
        # Check file contents
        with open(filepath, 'r') as f:
            content = f.read()
            assert 'title: "Test Post"' in content
            assert 'categories: testing' in content
            assert 'permalink: /test-permalink/' in content
            assert 'layout: post' in content
            
        print("✓ create_post_file tests passed")
        
        # Test that duplicate files are not created
        filepath2 = create_post_file("Test Post", "testing", "/test-permalink/")
        assert filepath2 is None
        print("✓ duplicate file prevention test passed")
        
    finally:
        os.chdir(original_dir)
        shutil.rmtree(temp_dir)


def test_script_execution():
    """Test running the script via command line."""
    result = subprocess.run(
        ['python3', 'new_post.py', '--help'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert 'Create a new blog post' in result.stdout
    print("✓ script execution test passed")


if __name__ == '__main__':
    print("Running tests for new_post.py...\n")
    
    try:
        test_slugify()
        test_create_post_file()
        test_script_execution()
        print("\n✅ All tests passed!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
