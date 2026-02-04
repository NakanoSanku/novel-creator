# 小说创作插件 (Novel Creator Plugin)

这是一个在 Claude Code 中用于编写中文小说的结构化工作流助手。

## 功能特色

### 六步工作流
1. **头脑风暴** - 确定类型、卖点、核心冲突
2. **世界观设定** - 力量体系、地理、势力
3. **角色与大纲** - 角色卡、剧情主线
4. **剧情细纲** - 逐章节拍、场景设计
5. **正文撰写** - 章节内容、对话描写
6. **内容修改** - 润色、一致性检查

### 专业写作指南
- 中文网文类型详解（仙侠、玄幻、都市、言情）
- 角色设计原型（废柴流、重生流、无敌流）
- 对话写作技巧
- 场景描写指南
- 战斗描写技巧
- 节奏与张力管理
- 常见问题解决方案

### 智能助手
- **小说助手 (Novel Assistant)**：引导你完成整个创作过程
- 自动状态管理：记录你的创作进度
- 文件自动组织：元数据、章节、想法分类存储

## 安装

```bash
cc --plugin-dir /path/to/novel-creator
```

## 可用命令

| 命令 | 说明 |
|------|------|
| `/novel-creator:start` | 开始或继续小说项目 |
| `/novel-creator:status` | 查看当前项目进度 |
| `/novel-creator:next-step` | 进入工作流的下一步 |
| `/novel-creator:write-chapter [章节号]` | 撰写指定章节 |
| `/novel-creator:edit-chapter [章节号] [要求]` | 修改指定章节 |
| `/novel-creator:export [格式]` | 导出完整小说（md/txt） |

## 快速开始

1. 运行 `/novel-creator:start "你的小说名"` 开始新项目
2. 按照小说助手的引导完成头脑风暴
3. 使用 `/novel-creator:next-step` 进入下一阶段
4. 使用 `/novel-creator:write-chapter 1` 撰写第一章
5. 使用 `/novel-creator:export` 导出完成的小说

## 项目结构

插件会自动创建以下目录结构：

```
your-project/
├── .novel-creator.state.json  # 进度状态
└── novel/
    ├── meta/                  # 元数据
    │   ├── settings.md        # 世界观设定
    │   ├── characters.md      # 角色卡
    │   └── outline.md         # 剧情大纲
    ├── chapters/              # 章节正文
    │   ├── 001-章节名.md
    │   └── 002-章节名.md
    ├── backlog/               # 想法库
    │   └── ideas.md
    └── export/                # 导出文件
        └── 完整版.md
```

## 写作参考资料

插件内置了丰富的写作参考资料：

- **类型指南**：仙侠、玄幻、都市、言情的套路与技巧
- **角色设计**：废柴流、重生流、无敌流等主角原型
- **力量体系**：修真境界、武道等级、异能分级设计
- **写作技巧**：对话、场景、战斗描写要点
- **节奏控制**：黄金三章、钩子设置、打脸循环
- **问题解决**：开篇慢、水文、角色脸谱化等常见问题

## 许可证

MIT License
