#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用图片下载脚本
用于从image_urls.txt文件读取图片链接并下载到images文件夹

使用方法:
    python download_images.py [image_urls_file] [markdown_files]

参数:
    image_urls_file: 包含图片URL的文件路径，默认为'image_urls.txt'
    markdown_files: 需要更新图片链接的Markdown文件，支持通配符，默认为'*.md'

功能:
    1. 读取指定文件中的图片URL
    2. 创建images文件夹（如果不存在）
    3. 下载所有图片到images文件夹
    4. 验证下载的图片完整性
    5. 自动替换MD文档中的CDN链接为本地链接
    6. 生成下载报告
"""

import os
import sys
import re
import requests
import time
import glob
from pathlib import Path
from urllib.parse import urlparse
import hashlib

class ImageDownloader:
    def __init__(self, urls_file='image_urls.txt', output_dir='images', md_pattern='*.md'):
        self.urls_file = urls_file
        self.output_dir = output_dir
        self.md_pattern = md_pattern
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.downloaded_files = {}  # 存储URL到本地文件名的映射
        
    def extract_filename_from_url(self, url):
        """从URL中提取文件名"""
        parsed = urlparse(url)
        path = parsed.path
        # 提取路径中的文件名
        filename = os.path.basename(path)
        if not filename or '.' not in filename:
            # 如果没有文件名或没有扩展名，使用URL的哈希值
            filename = hashlib.md5(url.encode()).hexdigest() + '.jpg'
        return filename
    
    def read_urls_from_file(self):
        """从文件中读取图片URL"""
        urls = []
        try:
            with open(self.urls_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if line and not line.startswith('#'):
                        # 支持多种URL格式
                        if line.startswith('http'):
                            urls.append(line)
                        elif line.startswith('!['):
                            # 从Markdown图片语法中提取URL
                            match = re.search(r'!\[.*?\]\((.*?)\)', line)
                            if match:
                                url = match.group(1)
                                if url.startswith('http'):
                                    urls.append(url)
                        else:
                            print(f"警告: 第{line_num}行格式不支持: {line}")
        except FileNotFoundError:
            print(f"错误: 找不到文件 {self.urls_file}")
            return []
        except Exception as e:
            print(f"错误: 读取文件时出错: {e}")
            return []
        
        return urls
    
    def create_output_directory(self):
        """创建输出目录"""
        try:
            Path(self.output_dir).mkdir(parents=True, exist_ok=True)
            print(f"✓ 输出目录已创建/确认: {self.output_dir}")
        except Exception as e:
            print(f"错误: 创建目录失败: {e}")
            return False
        return True
    
    def download_image(self, url, filename):
        """下载单个图片"""
        try:
            print(f"正在下载: {filename}")
            response = self.session.get(url, timeout=30, stream=True)
            response.raise_for_status()
            
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # 验证文件大小
            file_size = os.path.getsize(filepath)
            if file_size == 0:
                print(f"警告: {filename} 文件大小为0，可能下载失败")
                return False
            
            print(f"✓ 下载完成: {filename} ({file_size} bytes)")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"✗ 下载失败 {filename}: {e}")
            return False
        except Exception as e:
            print(f"✗ 保存文件失败 {filename}: {e}")
            return False
    
    def validate_image_file(self, filepath):
        """验证图片文件是否有效"""
        try:
            with open(filepath, 'rb') as f:
                header = f.read(10)
                # 检查JPEG文件头
                if header.startswith(b'\xff\xd8\xff'):
                    return True
                # 检查PNG文件头
                elif header.startswith(b'\x89PNG\r\n\x1a\n'):
                    return True
                else:
                    return False
        except Exception:
            return False
    
    def update_markdown_links(self):
        """更新Markdown文件中的图片链接"""
        print(f"\n正在更新Markdown文件中的图片链接...")
        
        # 查找所有匹配的Markdown文件
        md_files = glob.glob(self.md_pattern)
        if not md_files:
            print(f"警告: 没有找到匹配的Markdown文件: {self.md_pattern}")
            return
        
        print(f"找到 {len(md_files)} 个Markdown文件")
        
        total_replacements = 0
        
        for md_file in md_files:
            try:
                print(f"处理文件: {md_file}")
                
                # 读取文件内容
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                file_replacements = 0
                
                # 替换所有已下载的图片链接
                for url, local_filename in self.downloaded_files.items():
                    # 替换Markdown图片语法中的URL
                    old_pattern = f'![]({url})'
                    new_pattern = f'![](images/{local_filename})'
                    if old_pattern in content:
                        content = content.replace(old_pattern, new_pattern)
                        file_replacements += 1
                        print(f"  ✓ 替换: {url} -> images/{local_filename}")
                    
                    # 替换纯URL（如果不是Markdown语法）
                    if url in content and f'![]({url})' not in content:
                        # 这里可以添加其他替换逻辑，比如HTML img标签等
                        pass
                
                # 如果内容有变化，写回文件
                if content != original_content:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  ✓ 文件已更新，替换了 {file_replacements} 个链接")
                    total_replacements += file_replacements
                else:
                    print(f"  - 文件无需更新")
                    
            except Exception as e:
                print(f"  ✗ 处理文件 {md_file} 时出错: {e}")
        
        print(f"\n✓ 总共替换了 {total_replacements} 个图片链接")
    
    def run(self):
        """运行下载程序"""
        print("=" * 60)
        print("通用图片下载脚本")
        print("=" * 60)
        
        # 读取URL列表
        print(f"正在读取URL文件: {self.urls_file}")
        urls = self.read_urls_from_file()
        
        if not urls:
            print("没有找到有效的图片URL")
            return
        
        print(f"找到 {len(urls)} 个图片URL")
        
        # 创建输出目录
        if not self.create_output_directory():
            return
        
        # 下载图片
        print("\n开始下载图片...")
        successful_downloads = 0
        failed_downloads = 0
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] 处理: {url}")
            
            filename = self.extract_filename_from_url(url)
            if self.download_image(url, filename):
                filepath = os.path.join(self.output_dir, filename)
                if self.validate_image_file(filepath):
                    successful_downloads += 1
                    self.downloaded_files[url] = filename
                else:
                    print(f"警告: {filename} 不是有效的图片文件")
                    failed_downloads += 1
            else:
                failed_downloads += 1
            
            # 添加延迟避免请求过快
            time.sleep(0.5)
        
        # 更新Markdown文件中的链接
        if successful_downloads > 0:
            self.update_markdown_links()
        
        # 生成报告
        print("\n" + "=" * 60)
        print("下载完成报告")
        print("=" * 60)
        print(f"总URL数量: {len(urls)}")
        print(f"成功下载: {successful_downloads}")
        print(f"下载失败: {failed_downloads}")
        print(f"成功率: {successful_downloads/len(urls)*100:.1f}%")
        
        if self.downloaded_files:
            print(f"\n成功下载的文件:")
            for url, filename in self.downloaded_files.items():
                filepath = os.path.join(self.output_dir, filename)
                file_size = os.path.getsize(filepath)
                print(f"  - {filename} ({file_size} bytes)")
        
        print(f"\n图片保存在: {os.path.abspath(self.output_dir)}")

def main():
    """主函数"""
    # 解析命令行参数
    urls_file = 'image_urls.txt'
    md_pattern = '*.md'
    
    if len(sys.argv) > 1:
        urls_file = sys.argv[1]
    if len(sys.argv) > 2:
        md_pattern = sys.argv[2]
    
    # 创建下载器并运行
    downloader = ImageDownloader(urls_file, md_pattern=md_pattern)
    downloader.run()

if __name__ == "__main__":
    main()
