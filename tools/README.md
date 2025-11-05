# New Post Creation Tool

This directory contains automation tools for managing blog posts.

## new_post.py

A Python script to automate the process of creating new blog posts with proper Jekyll front matter.

### Features

- Automatically generates post filename with date (YYYY-MM-DD-title.md)
- Creates Jekyll front matter with:
  - layout: post
  - title
  - date (with timestamp)
  - categories
  - permalink
- Opens the file in your editor for content addition
- Optionally creates a git branch and pull request

### Requirements

- Python 3.6 or higher
- Git (for branch and PR creation)
- GitHub CLI (`gh`) - optional, for automated PR creation

### Usage

#### Basic Usage

Create a new post:

```bash
python3 new_post.py "My Post Title"
```

This will:

1. Create a new file in `_posts/` with the format `YYYY-MM-DD-my-post-title.md`
2. Add Jekyll front matter with a permalink `/my-post-title/`
3. Open the file in your default editor

#### Advanced Options

Specify custom categories:

```bash
python3 new_post.py "My Post Title" --categories "ai ml research"
```

Specify a custom permalink:

```bash
python3 new_post.py "My Post Title" --permalink "/custom-url/"
```

Create a branch and pull request automatically:

```bash
python3 new_post.py "My Post Title" --create-pr
```

Skip opening the editor (useful for automation):

```bash
python3 new_post.py "My Post Title" --no-edit
```

Combine options:

```bash
python3 new_post.py "My Post Title" --categories "ai tools" --create-pr
```

### Workflow

1. **Create the post**:

   ```bash
   python3 new_post.py "My Awesome Post"
   ```

2. **Edit the content**: The script opens the file in your editor. Add your content below the front matter (after the `---` line).

3. **Save and close** the editor.

4. **Review the file** to ensure everything looks good.

5. **Create a PR** (if not using `--create-pr`):

   ```bash
   git add _posts/YYYY-MM-DD-my-awesome-post.md
   git commit -m "Add new post: My Awesome Post"
   git push
   ```

### Setting Your Editor

The script uses your default editor from environment variables. To set it:

```bash
export EDITOR=nano    # or vim, vi, code, etc.
```

Add this to your `~/.bashrc` or `~/.zshrc` to make it permanent.

### Examples

Create a post about AI tools:

```bash
python3 new_post.py "Exploring New AI Tools" --categories "ai tools"
```

Create a post and immediately create a PR:

```bash
python3 new_post.py "My Research Findings" --categories "research" --create-pr
```

Create a post with a custom permalink:

```bash
python3 new_post.py "Guide to Machine Learning" --permalink "/ml-guide/" --categories "ai ml tutorial"
```

### Tips

- The script automatically creates a URL-friendly slug from your title
- Permalinks should start and end with `/` (the script will add them if missing)
- Categories are space-separated
- If the file already exists, the script will alert you and not overwrite it
- When using `--create-pr`, ensure you have git credentials configured

### Troubleshooting

**"No editor found"**: Set the `EDITOR` environment variable or install `nano`, `vim`, or `vi`.

**Git errors**: Make sure you're in the repository directory and have git configured properly.

**PR creation fails**: Install GitHub CLI (`gh`) and authenticate with `gh auth login`, or create the PR manually via GitHub's web interface.
