---
name: Dev.to Publishing
description: Write and publish tech articles to Dev.to.
metadata:
  {
    "openclaw": {
      "emoji": "📝",
      "requires": { "env": ["DEVTO_API_KEY"] },
      "always": false
    }
  }
---

# Dev.to Publishing Skill

Allows the bot to write, edit, and publish articles to Dev.to.

## Capabilities

- **Post Article**: Create new drafts or published articles
- **Update Article**: Edit existing articles
- **List Articles**: See what you've published

## Configuration

Requires `DEVTO_API_KEY` in `.env`.
Key can be generated at [https://dev.to/settings/extensions](https://dev.to/settings/extensions).

## Tools

### `post_devto_article(title, content, tags, published)`
Creates a new article.
- `title`: Title of the article
- `content`: Markdown body
- `tags`: List of tags (e.g. `["python", "bot"]`)
- `published`: `True` to publish, `False` for draft (default)

### `list_devto_articles()`
Lists your recent published articles.

### `update_devto_article(id, ...)`
Update an article by ID.
