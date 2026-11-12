# Learn Anything

A personal learning system powered by [Claude Code](https://claude.ai/code) skills. Transform raw notes into structured Obsidian wikis and beautiful HTML visualizations — guided by six proven learning methods.

## The Six Methods

| Method | Core Idea | Best For |
|--------|-----------|----------|
| **Feynman Technique** | Teach to learn — output drives input | Understanding concepts deeply |
| **Simon Method** | Focused mastery — 6 months to proficiency | Systematic skill acquisition |
| **SQ3R** | Active reading — Survey, Question, Read, Recite, Review | Textbook and academic reading |
| **Pomodoro Technique** | 25-minute focus units — beat procrastination | Sustained attention and time management |
| **Cornell Notes (5R)** | Structured note system — Record, Reduce, Recite, Reflect, Review | Lecture notes and exam prep |
| **Allegorical Insight** | Teach through indirect stories — delayed concept reveal creates "aha moments" | Abstract concepts, teaching, writing, cross-discipline communication |

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
│       └── learning-methods/         # The core skill
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

**Teach through story:**
> "Explain 'survivorship bias' using an allegorical story at graduate level"

→ Claude writes a寓言 (allegory) that conceals the concept until near the end, then maps each story element back to the concept.

**Research + document:**
> "What's the latest research on spaced repetition? Make it a wiki page."

→ Claude dispatches websearch subagents, synthesizes findings, and writes to `wiki/`.

## Skill Architecture

The `learning-methods` skill is a Claude Code skill that acts as an expert system for multiple proven learning methods. It follows progressive disclosure:

- **SKILL.md** (~400 lines) — Workflow router + quick reference
- **references/01-06** — Deep guides for the original five methods + comparison (~2000 lines)
- **references/07-09** — Output specs, HTML guide, research workflow (~450 lines)
- **references/10** — Allegorical Insight method guide (~420 lines)

See `.claude/skills/learning-methods/SKILL.md` for the full skill definition.

## License

MIT
