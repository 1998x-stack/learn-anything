# 🔬 网络搜索研究集成工作流

> 本文件定义了如何使用子代理（Subagent）和 WebSearch 工具为学习内容补充最新研究成果。

---

## 一、何时使用网络搜索

### 触发条件

当用户的问题满足以下任一条件时，使用网络搜索补充：

- 询问的内容超出已有参考文件（references/01-06）的范围
- 需要最新研究、2024-2026 年的进展
- 需要对比五种方法之外的替代方法
- 询问特定人群/场景的适配（如 ADHD、老年人、编程学习等）
- 用户明确要求"查一下最新研究"或"搜索一下"

### 不需要搜索的情况

- 问题完全在已有参考文件范围内
- 用户只是做个人经验分享（对话转 wiki 即可）
- 纯方法论解释或操作指导

---

## 二、搜索查询设计

### 2.1 查询数量

- 简单补充（1 个主题）：2-3 条查询
- 全面调研（多主题对比）：3-5 条查询

### 2.2 查询模板

```
"[学习法名称] [具体话题] research [年份范围]"
"[学习方法] [应用场景] best practices"
"cognitive science [认知概念] learning efficiency study"
```

### 2.3 查询示例

| 用户意图 | 搜索查询 |
|---------|---------|
| 费曼法与神经科学的关联 | "Feynman technique neuroscience learning retention 2025 2026" |
| 番茄法对 ADHD 的效果 | "Pomodoro technique ADHD effectiveness study" |
| 西蒙学习法的现代验证 | "Simon learning method 6 months mastery research update" |
| 费曼法 vs Blurting 方法 | "Feynman technique vs blurting method comparison learning science" |

### 2.4 查询原则

- 优先使用英文查询（研究文献覆盖面更广）
- 包含年份范围以获取最新结果
- 使用权威关键词：research, study, meta-analysis, review
- 避免过于宽泛的查询（"学习方法"），聚焦具体方面

---

## 三、子代理调度

### 3.1 单个搜索主题

使用 WebSearch 工具直接搜索：

```
WebSearch(query="[搜索查询]")
```

### 3.2 多个并行搜索主题（推荐）

使用 Agent 工具并行调度，参考 `superpowers:dispatching-parallel-agents` 技能：

```
同时启动 2-3 个子代理，每个负责一个搜索方向：

Agent 1: 搜索 "[查询1]"
Agent 2: 搜索 "[查询2]"
Agent 3: 搜索 "[查询3]"

每个子代理的 prompt：
"使用 WebSearch 工具搜索以下主题，返回 3-5 个关键发现的摘要，
每条附上来源 URL。以要点列表形式输出，每个发现 1-2 句。"
```

### 3.3 子代理 Prompt 模板

```
你在做一个研究任务。你的目标是用 WebSearch 搜索"[搜索主题]"，
找到关于[具体方面]的最新信息。

要求：
1. 执行搜索并阅读前 3-5 个最相关的结果
2. 提取 3-5 个有证据支持的关键发现
3. 每个发现用 1-2 句话概括
4. 附上每个发现的来源 URL
5. 如果有矛盾的信息，同时报告两方观点
6. 输出格式：要点列表，每项格式为 "- 发现描述。来源：[title](url)"
```

---

## 四、结果整合

### 4.1 Wiki 笔记整合

研究结果写入 wiki 笔记的 `## 🔬 研究补充` 版块：

```markdown
## 🔬 研究补充

- 2025 年的一项元分析显示，费曼学习法的记忆保留率在主动学习方法中位列前三。
  来源：[Active Learning Meta-Analysis](https://example.com)
- 神经影像研究表明，"教"的行为激活了前额叶皮层和海马体的协同活动。
  来源：[Neural Correlates of Teaching-Based Learning](https://example.com)
```

### 4.2 Frontmatter 更新

在 YAML frontmatter 中记录研究信息：

```yaml
researched: 2026-06-13
sources:
  - url: "https://example.com/meta-analysis"
    title: "Active Learning Techniques: A Comprehensive Meta-Analysis"
  - url: "https://example.com/neural-study"
    title: "Neural Correlates of Teaching-Based Knowledge Transfer"
```

### 4.3 重要原则

- **绝不修改 references/01-06**：现有参考文件保持不变，所有新发现写入 `wiki/` 笔记
- **标注来源**：所有外部信息必须注明来源 URL
- **区分观点与事实**：如果是个人解读，明确说明；如果是研究结论，标注出处
- **时效性优先**：优先引用最近（2024-2026）的研究
- **中文用户友好**：研究摘要用中文撰写，保留英文关键词

---

## 五、限制与注意事项

### 5.1 不做的事

- 不进行需要登录/付费的数据库搜索
- 不尝试访问需要认证的学术资源
- 不为引用来源背书（AI 生成的结果需标注"来自网络搜索"）
- 不以研究结果修改现有参考文件

### 5.2 质量把控

- 对搜索结果保持批判态度，不盲目采信排名第一的结果
- 如果搜索结果相互矛盾，同时呈现多方观点
- 区分一手研究（原始论文）与二手报道（博客/文章）
- 如果没有找到高质量来源，坦诚告知用户而非敷衍

### 5.3 降级策略

- WebSearch 不可用时：使用已有知识补充，在 wiki 中注明"未进行实时搜索"
- 搜索结果质量低：告知用户并请求更具体的搜索方向
- 搜索结果过多：聚焦前 5 个最权威/相关的结果
