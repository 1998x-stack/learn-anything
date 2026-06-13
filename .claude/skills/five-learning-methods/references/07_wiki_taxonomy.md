# 📋 Obsidian Wiki 输出规范

> 本文件定义了生成 Obsidian 维基笔记时使用的 YAML frontmatter、标签分类、双向链接和文件命名规则。

---

## 一、YAML Frontmatter 模板

每篇维基笔记必须包含以下 frontmatter：

```yaml
---
title: "精确的页面标题"           # 必填，人类可读标题
date: 2026-06-13                  # 必填，ISO 日期格式
tags:                             # 必填，至少一个标签（见标签分类表）
  - learning/feynman
  - learning/active-recall
aliases:                          # 可选，同义词/别名
  - 费曼技巧
created: 2026-06-13               # 自动记录，创建后不可修改
modified: 2026-06-13              # 每次修订时更新
source: "conversation"            # "conversation" | "raw/<filename>" | "research"
related:                          # 可选，显式双向链接
  - "[[西蒙学习法]]"
  - "[[康奈尔笔记法]]"
researched: 2026-06-13            # 可选，使用网络搜索时设置
sources:                          # 可选，网络搜索引用源
  - url: "https://..."
    title: "来源标题"
---
```

### 字段说明

| 字段 | 必需性 | 说明 |
|------|--------|------|
| `title` | 必填 | 页面标题，与 H1 标题一致 |
| `date` | 必填 | 内容日期，对话/文件创建日期 |
| `tags` | 必填 | 至少一个 `learning/*` 标签 |
| `aliases` | 可选 | Obsidian 别名搜索使用 |
| `created` | 自动 | 生成时自动填入当天日期 |
| `modified` | 自动 | 生成/更新时填入 |
| `source` | 必填 | 来源追踪 |
| `related` | 推荐 | 显式双向链接，增强图谱连接 |
| `researched` | 条件必填 | 使用 websearch 时必填 |
| `sources` | 条件必填 | 有外部引用时必填 |

---

## 二、标签分类体系（Tag Taxonomy）

统一使用 `learning/*` 命名空间：

### 方法标签（必选至少一个）

| 标签 | 定义 |
|------|------|
| `#learning/feynman` | 费曼学习法相关内容 |
| `#learning/simon` | 西蒙学习法相关内容 |
| `#learning/sq3r` | SQ3R 阅读法相关内容 |
| `#learning/pomodoro` | 番茄学习法相关内容 |
| `#learning/cornell` | 康奈尔笔记法相关内容 |

### 概念标签（可选，组合使用）

| 标签 | 定义 |
|------|------|
| `#learning/active-recall` | 主动回忆/检索练习 |
| `#learning/spaced-repetition` | 间隔重复 |
| `#learning/metacognition` | 元认知 |
| `#learning/productivity` | 效率/时间管理 |
| `#learning/note-taking` | 笔记方法 |
| `#learning/reading` | 阅读策略 |
| `#learning/memory` | 记忆科学 |
| `#learning/ai-learning` | AI 辅助学习 |

---

## 三、Wikilink 双向链接规范

### 已知实体名称列表（精确匹配）

**五大方法：**
- `[[费曼学习法]]`
- `[[西蒙学习法]]`
- `[[SQ3R阅读法]]`
- `[[番茄学习法]]`
- `[[康奈尔笔记法]]`

**跨领域概念：**
- `[[主动回忆]]`
- `[[间隔重复]]`
- `[[元认知]]`
- `[[认知负荷]]`
- `[[生成效应]]`
- `[[心流状态]]`
- `[[深度工作]]`
- `[[学习迁移]]`
- `[[精细编码]]`

### 链接规则

1. **首次提及链接**：每个实体在文章中首次出现时用 `[[]]` 链接
2. **精确匹配**：wikilink 名称必须与目标页面的 `title` 字段一致
3. **可链则链**：遇到上表中列出的概念时，总是使用 `[[]]` 语法
4. **新概念不造字**：遇到未知概念时不臆造反链，等目标页面创建后补充
5. **别名处理**：如果页面有 `aliases`，在正文中可以用别名文本但 link 指向主 title

---

## 四、文件命名规范

```
wiki/<方法或主题>-<描述词>-<YYYY-MM-DD>.md
```

### 示例

```
wiki/feynman-js-closures-explanation-2026-06-13.md
wiki/pomodoro-adhd-adaptations-2026-06-13.md
wiki/sq3r-textbook-reading-experience-2026-06-13.md
wiki/learning-methods-comparison-2026-06-13.md
```

### 命名规则

- 使用英文小写 kebab-case（Obsidian 兼容性最佳）
- 包含主题关键词和方法名
- 以日期结尾（ISO 格式），便于追溯
- 不包含空格、特殊字符或 emoji

---

## 五、正文内容结构模板

```markdown
# Title（与 frontmatter 一致）

## 📝 摘要
1-3 句话概括这份笔记的核心内容

## 💡 要点
- 关键发现的要点列表
- 每个要点一行

## 🔗 与五大学习法的关联
（说明这份内容如何关联到一个或多个学习法，使用 [[wikilink]]）

## ❓ 待探索的问题
- 开放性问题或需要进一步研究的点

## 🔬 研究补充
（当使用 websearch 时，研究结果放在这里，包含内联引用）

## 📖 来源
> 原始内容（当从 raw/ 文件转换时，原始内容作为引用块保留）
```

---

## 六、验证清单

生成 wiki 笔记后，逐项检查：

- [ ] YAML frontmatter 用 `---` 正确包裹
- [ ] `title` 字段存在且非空
- [ ] `date` 字段存在且为 ISO 格式
- [ ] `tags` 字段存在且至少包含一个 `#learning/*` 标签
- [ ] `source` 字段已设置
- [ ] 至少有一个 `[[wikilink]]` 指向已知实体
- [ ] 文件名符合命名规范且写入 `wiki/` 目录
- [ ] 文件可被 Obsidian 正常解析（frontmatter 无语法错误）
