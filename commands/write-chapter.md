---
name: write-chapter
description: 根据细纲撰写指定章节。
argument-hint: "[章节号]"
---

# /novel-creator:write-chapter

此命令根据已有的细纲撰写指定章节的正文。

## Claude 指令

1. **解析参数**：获取要撰写的章节号（如 `1`、`5`）。
2. **读取相关资料**：
   - 读取 `./novel/meta/settings.md` 获取世界观设定
   - 读取 `./novel/meta/characters.md` 获取角色信息
   - 读取对应章节的细纲（如有）
3. **确认写作参数**：
   - 询问目标字数（默认 2000-3000 字）
   - 确认章节标题
   - 确认是否有特殊要求
4. **撰写正文**：
   - 遵循第三人称限知视角
   - 注重"展示而非叙述"
   - 在章节末尾设置钩子
   - 保持与已有设定的一致性
5. **保存文件**：写入 `./novel/chapters/XXX-章节标题.md`
6. **更新状态**：在状态文件中记录已完成的章节。

## 章节格式

```markdown
# 第X章 章节标题

正文内容...

---
<!-- 章节信息 -->
<!-- 字数：XXXX -->
<!-- 创建时间：YYYY-MM-DD -->
```

## 使用示例

- `/novel-creator:write-chapter 1` - 撰写第一章。
- `/novel-creator:write-chapter 5` - 撰写第五章。
