# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

This is a Claude Code skill repository — not a traditional software project. The core artifact is the `learning-methods` skill at `.claude/skills/learning-methods/`. There are no build, lint, or test commands.

## Skill architecture

The skill uses progressive disclosure across three layers:

1. **YAML frontmatter** (name + description) — in context always, determines when Claude triggers the skill
2. **SKILL.md body** (~400 lines) — loaded when skill triggers. Acts as a router: overview tables, recommendation guide, speed references, workflow specs, and document index
3. **references/*.md** (10 files, ~2600 lines total) — loaded on demand. Deep content for each learning method plus meta-guides

**Important rule:** New research findings and converted notes go to `wiki/` or `visualize/`. Never modify references/01-06 with new content — those are the canonical method definitions. New methods get their own reference file (e.g., `references/10_*.md`).

## Input/output pipeline

```
raw/*.md  ──→  skill processes  ──→  wiki/*.md (Obsidian)
chat      ──→  + WebSearch      ──→  visualize/*.html (frontend-design)
questions ──→  (optional)       ──→  direct answer
```

- `raw/` — User drops markdown notes here for the skill to read and transform
- `wiki/` — Skill writes Obsidian-compatible `.md` with YAML frontmatter, `[[wikilinks]]`, and `#learning/*` tags
- `visualize/` — Skill writes self-contained HTML files via `Skill("frontend-design")`

## When editing this skill

- SKILL.md must stay under 500 lines. Current: ~400.
- Match the existing reference file pattern for new methods: H1 title with emoji, blockquote core tenet, numbered Chinese H2 sections (一、二、三...), cognitive science basis in section 二, step-by-step guide in section 三, footer disclaimer with references.
- Update the document index at the bottom of SKILL.md when adding or changing reference files.
- The skill description in YAML frontmatter is the primary trigger mechanism — update it when adding new methods or capabilities.
