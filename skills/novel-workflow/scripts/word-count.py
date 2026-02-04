#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小说字数统计脚本
统计项目中的章节字数和总字数
"""

import os
import sys
import json
from pathlib import Path

def count_chinese_chars(text):
    """统计中文字符数"""
    count = 0
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            count += 1
    return count

def count_words(text):
    """统计总字数（中文字符 + 英文单词）"""
    chinese_count = count_chinese_chars(text)
    # 移除中文字符后统计英文单词
    english_text = ''.join([c if not '\u4e00' <= c <= '\u9fff' else ' ' for c in text])
    english_words = len(english_text.split())
    return chinese_count + english_words

def main():
    # 获取项目目录
    if len(sys.argv) > 1:
        project_dir = Path(sys.argv[1])
    else:
        project_dir = Path('.')

    chapters_dir = project_dir / 'novel' / 'chapters'

    if not chapters_dir.exists():
        print("未找到章节目录：novel/chapters/")
        print("请在小说项目目录中运行此脚本。")
        return

    # 统计各章节
    stats = []
    total_words = 0

    for file in sorted(chapters_dir.glob('*.md')):
        content = file.read_text(encoding='utf-8')
        words = count_words(content)
        stats.append({
            'file': file.name,
            'words': words
        })
        total_words += words

    # 输出结果
    print("=" * 50)
    print("📚 小说字数统计")
    print("=" * 50)

    if stats:
        print(f"\n{'章节':<30} {'字数':>10}")
        print("-" * 42)
        for stat in stats:
            print(f"{stat['file']:<30} {stat['words']:>10,}")
        print("-" * 42)
        print(f"{'总计':<30} {total_words:>10,}")
        print(f"\n共 {len(stats)} 章，{total_words:,} 字")
    else:
        print("\n暂无章节文件。")

    # 输出 JSON 格式（供程序调用）
    result = {
        'chapters': stats,
        'total_words': total_words,
        'chapter_count': len(stats)
    }

    # 保存统计结果
    stats_file = project_dir / 'novel' / 'stats.json'
    stats_file.parent.mkdir(parents=True, exist_ok=True)
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n统计结果已保存至：{stats_file}")

if __name__ == '__main__':
    main()
