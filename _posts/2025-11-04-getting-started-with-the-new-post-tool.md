---
layout: post
title: "Getting Started with the New Post Tool"
date: 2025-11-04 19:54:14 +0000
categories: tools automation
permalink: /getting-started-with-the-new-post-tool/
---


This is a guide to using the new automated post creation tool for this blog.

## Quick Start

Creating a new blog post is now as simple as running:

```bash
python3 new_post.py "Your Post Title"
```

The tool will:
1. Generate a properly formatted post file
2. Add all the necessary Jekyll front matter
3. Create a permalink automatically
4. Open the file in your editor

## Features

### Automatic Slug Generation

The tool converts your title into a URL-friendly slug:
- "My New Post" becomes `my-new-post`
- Handles special characters and multiple spaces

### Front Matter

Every post includes:
- `layout: post` - Uses the post layout
- `title` - Your post title in quotes
- `date` - Current date and time with timezone
- `categories` - Space-separated categories (default: "ai")
- `permalink` - Auto-generated from title

### Custom Options

You can customize the post creation:

```bash
# Custom categories
python3 new_post.py "My Post" --categories "ai ml research"

# Custom permalink
python3 new_post.py "My Post" --permalink "/custom-url/"

# Skip editor (for automation)
python3 new_post.py "My Post" --no-edit
```

## Workflow

1. Run the script with your post title
2. Add content in your editor
3. Save and close
4. Commit and push the changes

## Benefits

- **Speed**: Create posts in seconds
- **Consistency**: All posts follow the same format
- **Accuracy**: No typos in front matter
- **Convenience**: Automatic permalink generation

Happy blogging!
