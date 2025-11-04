# GitHub Pages Deployment

This site is configured for GitHub Pages deployment.

## Automatic Deployment

GitHub Pages will automatically build and deploy this Jekyll site when changes are pushed to the main branch.

## Configuration Steps

1. Go to your repository settings on GitHub
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select the branch you want to deploy from (typically `main`)
4. GitHub will automatically detect the Jekyll site and build it
5. Your site will be available at: `https://fairflow.github.io/writing/`

## Local Development

To build and test the site locally:

```bash
# Install dependencies
bundle install

# Build the site
bundle exec jekyll build

# Serve the site locally
bundle exec jekyll serve
```

Then visit `http://localhost:4000/writing/` in your browser.

## Troubleshooting

If the site doesn't build on GitHub Pages:

1. Check the Actions tab for build errors
2. Verify that GitHub Pages is enabled in repository settings
3. Ensure the branch selected for Pages matches your source branch
4. Check that all file paths use the correct baseurl (/writing)

## Theme

This site uses the `minima` theme, which is the default GitHub Pages theme.
