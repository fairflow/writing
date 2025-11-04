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
python3 new-post.py "My Post Title"
```

This will:
- Create a new post file with proper Jekyll front matter
- Include a permalink for the post
- Open the file in your editor for content addition
- Optionally create a branch and pull request with `--create-pr`

See [tools/README.md](tools/README.md) for detailed usage instructions.

## Structure

- `_config.yml` - Jekyll configuration
- `index.md` - Homepage
- `_posts/` - Blog posts
- `_tools/` - Individual tool documentation pages
- `tools/` - Automation tools and utilities
- `new-post.py` - Automated post creation script

## Contributing

This is a personal repository, but suggestions and corrections are welcome via issues.
