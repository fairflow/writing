---
layout: post
title: "Report on Github Pages"
date: 2025-11-04 22:36:36 +0000
categories: ai git
permalink: /report-on-github-pages/
---

## Main gotchas and resolutions

1. To use pages you must either make your repo public or else subscribe (although that is not very expensive)
2. You can automate the process of generating the right `_yaml` and `Gemfile` data using Copilot
(and when I mention Copilot I mean Github Copilot of course) as well as populating the Page with some content; however
it was a bit delicate to get links to work.  In the end I resorted to using permalinks but that motivated creating
python code to create new posts, fit them into categories, possibly create custom permalinks.  That process is somewhat explained
in this [post]({{ '/getting-started-with-the-new-post-tool/' | relative_url }}) but more documentation can be found in the script itself.
3. Setting up a local server was ok once the right `bundle` command was used.

## What's really nice about the setup

The process works very smoothly once things are setup.  Using VSCode is fantastic.  Git works well
in that environment of course, and also setting up a local server means that changes can be seen really quickly (for a small site such as this, less than a second after saving!); also a local branch can be kept which has sensitive data and only after filtering would these files be pushed to a public branch.  So much cleaner that a MAMP which is not pleasant
to maintain or set up in the first place.  I wanted a lightweight solution that used standard
Markdown syntax to speed up writing and for compatibility with Perplexity which I use so much.
