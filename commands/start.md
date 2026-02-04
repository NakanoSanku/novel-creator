---
name: start
description: 初始化或继续小说创作项目。
argument-hint: "[项目名称]"
---

# /novel-creator:start

此命令启动或继续六步小说创作工作流。

## Claude 指令

1. **检查状态**：使用 `Read` 工具在当前工作目录中查找 `.novel-creator.state.json`。
2. **若存在则继续**：
   - 如果状态文件存在，读取 `current_step`（当前步骤）和 `project_name`（项目名称）。
   - 向用户问好，并告知正在继续执行“[项目名称]”的第 [步骤编号] 步。
   - 简要总结目前的进度。
3. **若不存在则新建**：
   - 如果不存在，询问用户拟定的书名（或询问是否需要头脑风暴一个）。
   - 初始化状态文件，设置 `current_step: 1` 和项目名称。
   - 如果目录结构不存在，则创建：
     - `./novel/meta/`
     - `./novel/chapters/`
     - `./novel/backlog/`
4. **触发 Agent**：告知用户 **小说助手 (Novel Assistant)** 现已激活并开始引导。
5. **行动号召**：针对第一步（头脑风暴）提出第一个问题。

## 使用示例

- `/novel-creator:start` - 在当前目录开始一个新的小说项目。
- `/novel-creator:start` - 继续当前目录中已有的项目。
