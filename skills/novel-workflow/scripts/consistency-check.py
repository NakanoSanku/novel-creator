#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一致性检查脚本
检查章节内容与设定、角色卡的一致性
"""

import os
import sys
import json
import re
from pathlib import Path

def load_characters(meta_dir):
    """加载角色信息"""
    chars_file = meta_dir / 'characters.md'
    if not chars_file.exists():
        return {}

    content = chars_file.read_text(encoding='utf-8')
    # 简单提取角色名（以 # 或 ## 开头的行）
    names = re.findall(r'^#+\s*(?:角色卡[：:]?\s*)?(.+?)(?:\s*\(|$)', content, re.MULTILINE)
    return {name.strip() for name in names if name.strip()}

def load_settings(meta_dir):
    """加载设定信息"""
    settings_file = meta_dir / 'settings.md'
    if not settings_file.exists():
        return {}

    content = settings_file.read_text(encoding='utf-8')
    # 提取关键术语（粗体标记的内容）
    terms = re.findall(r'\*\*(.+?)\*\*', content)
    return {term.strip() for term in terms}

def check_chapter(chapter_file, characters, settings):
    """检查单个章节"""
    content = chapter_file.read_text(encoding='utf-8')
    issues = []

    # 检查是否有未定义的角色名
    # 简单的启发式：查找引号中的对话者
    dialogues = re.findall(r'(\S{2,4})(?:说道|问道|喊道|冷笑|大喝)', content)
    for name in dialogues:
        if name not in characters and len(characters) > 0:
            issues.append(f"可能的未定义角色：{name}")

    return issues

def main():
    if len(sys.argv) > 1:
        project_dir = Path(sys.argv[1])
    else:
        project_dir = Path('.')

    meta_dir = project_dir / 'novel' / 'meta'
    chapters_dir = project_dir / 'novel' / 'chapters'

    if not chapters_dir.exists():
        print("未找到章节目录。")
        return

    print("=" * 50)
    print("🔍 一致性检查")
    print("=" * 50)

    # 加载设定和角色
    characters = load_characters(meta_dir)
    settings = load_settings(meta_dir)

    print(f"\n已加载角色：{len(characters)} 个")
    print(f"已加载设定术语：{len(settings)} 个")

    # 检查各章节
    all_issues = {}
    for chapter_file in sorted(chapters_dir.glob('*.md')):
        issues = check_chapter(chapter_file, characters, settings)
        if issues:
            all_issues[chapter_file.name] = issues

    # 输出结果
    print("\n" + "-" * 50)
    if all_issues:
        print("⚠️  发现以下潜在问题：\n")
        for chapter, issues in all_issues.items():
            print(f"📄 {chapter}:")
            for issue in issues:
                print(f"   - {issue}")
            print()
    else:
        print("✅ 未发现明显的一致性问题。")

    print("-" * 50)
    print("注意：此脚本仅做基础检查，详细一致性请人工审核。")

if __name__ == '__main__':
    main()
