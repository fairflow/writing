# writing

My writing, especially on AI related issues, including code and discussions.

## Visit the Site

This repository is published as a GitHub Pages site at: **[https://fairflow.github.io/writing/](https://fairflow.github.io/writing/)**

## Content

### Emerging AI Tools

Documentation of cutting-edge AI tools:

- **[Perplexity AI](https://fairflow.github.io/writing/tools/perplexity/)** - AI-powered search and research platform
- **[Cursor](https://fairflow.github.io/writing/tools/cursor/)** - AI-native code editor

## Local Development

To run this site locally:

```bash
bundle install
bundle exec jekyll serve
```

Then visit `http://localhost:4000/writing/`

## Creating New Posts

Use the automated post creation tool to quickly create new blog posts:

```bash
python3 new_post.py "My Post Title"
```

This will:
- Create a new post file with proper Jekyll front matter
- Include a permalink for the post
- Open the file in your editor for content addition
- Optionally create a branch and pull request with `--create-pr`

See [tools/README.md](tools/README.md) for detailed usage instructions.

## Linting

This repository uses markdownlint to ensure consistent markdown formatting and catch common issues like bare URLs (MD034).

### Running the Linter

```bash
# Install dependencies
npm install

# Check markdown files for issues
npm run lint:md

# Auto-fix issues where possible
npm run lint:md:fix
```

### Configuration

Markdown linting rules are configured in `.markdownlint.json`. Key rules include:

- **MD034 (no-bare-urls)**: Ensures all URLs are properly formatted as markdown links or wrapped in angle brackets
- **MD013 (line-length)**: Limits line length to 120 characters (excluding code blocks and tables)

## Structure

- `_config.yml` - Jekyll configuration
- `index.md` - Homepage
- `_posts/` - Blog posts
- `_tools/` - Individual tool documentation pages
- `tools/` - Automation tools and utilities
- `new_post.py` - Automated post creation script

## Contributing

This is a personal repository, but suggestions and corrections are welcome via issues.
