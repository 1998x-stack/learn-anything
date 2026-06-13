# Learn Anything

A personal learning system powered by [Claude Code](https://claude.ai/code) skills. Transform raw notes into structured Obsidian wikis and beautiful HTML visualizations — guided by the world's five most proven learning methods.

## The Five Methods

| Method | Core Idea | Best For |
|--------|-----------|----------|
| **Feynman Technique** | Teach to learn — output drives input | Understanding concepts deeply |
| **Simon Method** | Focused mastery — 6 months to proficiency | Systematic skill acquisition |
| **SQ3R** | Active reading — Survey, Question, Read, Recite, Review | Textbook and academic reading |
| **Pomodoro Technique** | 25-minute focus units — beat procrastination | Sustained attention and time management |
| **Cornell Notes (5R)** | Structured note system — Record, Reduce, Recite, Reflect, Review | Lecture notes and exam prep |

## How It Works

```
Input                  Process                Output
─────────────────────────────────────────────────────
Chat history    →     five-learning-     →   wiki/*.md (Obsidian)
raw/*.md        →     methods skill      →   visualize/*.html
Questions       →     + WebSearch        →   Direct answers
```

### Input Sources
- **Chat history** — Discuss learning topics; insights are automatically captured
- **`raw/*.md`** — Drop in raw markdown notes, articles, or study logs
- **Direct questions** — Ask about any learning method or challenge

### Output Formats
- **Obsidian Wiki** — Interlinked markdown files with YAML frontmatter, `[[wikilinks]]`, and tags
- **HTML Visualizations** — Beautiful, self-contained pages via the `frontend-design` skill
- **Direct answers** — Deep, method-grounded responses when you just need an answer

## Directory Structure

```
learn-anything/
├── .claude/
│   └── skills/
│       └── five-learning-methods/    # The core skill
│           ├── SKILL.md              # Main skill definition
│           └── references/           # Deep reference content
├── raw/                              # Input: raw markdown notes
├── wiki/                             # Output: Obsidian wiki pages
├── visualize/                        # Output: HTML visualizations
└── README.md
```

## Getting Started

### Prerequisites
- [Claude Code](https://claude.ai/code) installed
- This repository cloned locally

### Setup
```bash
git clone git@github.com:1998x-stack/learn-anything.git
cd learn-anything
```

The skill activates automatically. Just start discussing learning methods — Claude will recognize the context and load the skill.

### Usage Examples

**Ask a question:**
> "I keep forgetting what I read. What should I do?"

→ Claude recommends Feynman + Cornell, with specific steps.

**Process raw notes:**
> "Process my notes in raw/quantum-physics-notes.md"

→ Claude reads, analyzes, and writes a formatted wiki page with tags and wikilinks.

**Create a visualization:**
> "Make an HTML comparison chart of all five methods"

→ Claude invokes the frontend-design skill and saves the result to `visualize/`.

**Research + document:**
> "What's the latest research on spaced repetition? Make it a wiki page."

→ Claude dispatches websearch subagents, synthesizes findings, and writes to `wiki/`.

## Skill Architecture

The `five-learning-methods` skill is a Claude Code skill that acts as an expert system for the five learning methods. It follows progressive disclosure:

- **SKILL.md** (~385 lines) — Workflow router + quick reference
- **references/01-06** — Deep guides for each method + comparison (~2000 lines)
- **references/07-09** — Output specs, HTML guide, research workflow (~450 lines)

See `.claude/skills/five-learning-methods/SKILL.md` for the full skill definition.

## License

MIT
