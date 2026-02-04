---
name: novel-workflow
description: 当用户要求"开始写小说"、"头脑风暴小说想法"、"创建角色卡"、"编写剧情大纲"、"开发小说设定"、"编写剧情细纲"、"撰写章节"、"修改章节"或"导出小说"时，应使用此技能。它为中文小说创作提供了六步工作流。
version: 0.2.0
---

# 中文小说创作工作流

此技能提供了一个结构化的六步过程来创作中文小说，并针对网文套路、节奏和结构进行了优化。

## 工作流概览

按顺序遵循以下步骤，进行全面的小说创作：

1. **想法头脑风暴** - 交流想法以确定类型、核心冲突和独特卖点 (卖点)。
2. **世界观设定** - 定义世界的等级体系、地理环境和社会规则。
3. **角色与大纲** - 创建角色卡和高层剧情摘要。
4. **剧情细纲** - 将剧情分解为逐场景的节拍 (细纲)。
5. **正文撰写** - 根据细纲编写实际章节内容。
6. **内容修改** - 根据用户反馈完善初稿。

## 第一步：想法头脑风暴

首先，与用户进行对话以确立：
- **类型**： (例如：仙侠、玄幻、都市、科幻)。
- **核心冲突**：推动故事发展的主要矛盾。
- **卖点 (Unique Selling Point)**：是什么让这个故事新鲜或令人兴奋？
- **基调**：严肃、幽默、黑暗或轻快。

请咨询 **`references/genres.md`** 以了解特定类型的套路和预期。

## 第二步：世界观设定

定义世界的内在逻辑：
- **等级体系**：等级、修炼方法或魔法规则。
- **地理环境**：主要地点及其重要性。
- **势力**：宗门、帝国或组织。
- **历史**：塑造当前世界状态的关键过去事件。

使用 **`examples/setting-template.md`** 中的模板。
参考 **`references/power-system.md`** 了解力量体系设计。

## 第三步：角色与大纲

### 角色卡
开发主要角色阵容，包括：
- **姓名/身份**：包括称号或化名。
- **动机**：他们想要什么？为什么？
- **性格**：核心特质和缺陷。
- **金手指 (Cheat)**：如果适用，他们的独特优势。

### 高层大纲
规划主要的故事情节线：
- **开端**：诱发事件和早期成长。
- **发展**：关键冲突和等级提升。
- **高潮**：主要冲突的解决。

参考 **`references/character-design.md`** 了解角色原型。
使用 **`examples/character-templates.md`** 中的角色卡模板。
使用 **`examples/outline-template.md`** 规划剧情大纲。

## 第四步：剧情细纲 (细纲)

将特定的情节线或章节分解为节拍：
- **场景地点**：发生的地点。
- **动作**：实际发生了什么。
- **对话**：关键点或情感节拍。
- **钩子**：场景或章节如何结束 (卡文/钩子)。

参考 **`examples/detailed-outline.md`** 了解细纲格式。

## 第五步：正文撰写

编写章节文本：
- **视角**：保持一致性（通常是第三人称限知视角）。
- **节奏**：在情感或动作节拍中注重"展示，而非叙述" (Show, don't Tell)。
- **张力**：确保主角面临有意义的障碍。

写作技巧参考：
- **`references/dialogue-techniques.md`** - 对话写作技巧
- **`references/scene-writing.md`** - 场景描写指南
- **`references/combat-writing.md`** - 战斗描写技巧
- **`references/pacing-techniques.md`** - 节奏与张力管理

完整章节示例见 **`examples/sample-chapter.md`**。

## 第六步：内容修改

根据以下内容完善文本：
- **反馈**：处理特定的用户要求。
- **一致性**：根据已确立的设定和角色特质进行检查。
- **节奏**：根据需要紧凑或扩展场景。

常见问题与解决方案见 **`references/common-problems.md`**。

## 状态管理

插件使用 `.novel-creator.state.json` 文件跟踪进度。
- **`current_step`**：1-6。
- **`project_name`**：小说标题。
- **`files`**：每个步骤生成的文件映射。

## 可用命令

| 命令 | 功能 |
|------|------|
| `/novel-creator:start` | 开始或继续项目 |
| `/novel-creator:status` | 查看项目进度 |
| `/novel-creator:next-step` | 进入下一步 |
| `/novel-creator:write-chapter [章节号]` | 撰写指定章节 |
| `/novel-creator:edit-chapter [章节号]` | 修改指定章节 |
| `/novel-creator:export [格式]` | 导出完整小说 |

## 实用脚本

- **`scripts/word-count.py`** - 统计章节和总字数
- **`scripts/consistency-check.py`** - 检查设定一致性

运行方式：
```bash
uv run python $CLAUDE_PLUGIN_ROOT/skills/novel-workflow/scripts/word-count.py ./
```

## 附加资源

### 参考文件
- **`references/genres.md`** - 中文网文类型详解
- **`references/character-design.md`** - 角色原型和成长曲线
- **`references/pacing-techniques.md`** - 节奏与钩子技巧
- **`references/dialogue-techniques.md`** - 对话写作技巧
- **`references/scene-writing.md`** - 场景描写指南
- **`references/combat-writing.md`** - 战斗描写技巧
- **`references/power-system.md`** - 力量体系设计
- **`references/common-problems.md`** - 常见问题与解决方案

### 示例文件
- **`examples/setting-template.md`** - 世界观构建模板
- **`examples/character-card.md`** - 角色卡示例
- **`examples/character-templates.md`** - 多种角色卡模板
- **`examples/detailed-outline.md`** - 细纲示例
- **`examples/outline-template.md`** - 剧情大纲模板
- **`examples/sample-chapter.md`** - 完整章节示例
