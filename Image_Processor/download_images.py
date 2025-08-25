#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MD文档图片本地化脚本
用于将MD文档中的在线图片链接下载到本地，并更新文档中的链接

功能:
    1. 从指定文件夹读取MD文件，提取图片链接到image_urls.txt
    2. 下载所有图片到images文件夹
    3. 存储下载的图片本地链接到unique_images.txt
    4. 复制MD文件到目标文件夹，修改文件名与PDF一致，替换图片链接为本地链接

使用方法:
    python download_images.py [source_folder] [target_folder]

参数:
    source_folder: 源文件夹路径，包含MD文件的文件夹（可选，默认为'../source_md'）
    target_folder: 目标文件夹路径，生成的MD文件存放位置（可选，默认为'../Documents Md'）

示例:
    python download_images.py
    python download_images.py "../my_md_files" "../output_md"
    python download_images.py "D:/MyProject/md_source" "D:/MyProject/md_output"
"""

import os
import sys
import re
import requests
import time
import glob
import shutil
from pathlib import Path
from urllib.parse import urlparse
import hashlib

class MDImageLocalizer:
    def __init__(self, source_folder='source_md', target_folder='Documents Md'):
        self.source_folder = source_folder
        self.target_folder = target_folder
        self.images_folder = os.path.join(os.path.dirname(__file__), 'images')
        self.urls_file = 'image_urls.txt'
        self.unique_images_file = 'unique_images.txt'
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        # 禁用SSL验证以避免SSL错误
        self.session.verify = False
        # 禁用代理
        self.session.proxies = {}
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.downloaded_files = {}  # 存储URL到本地文件名的映射
        self.image_urls = set()  # 存储所有图片URL
        
    def validate_paths(self):
        """验证路径是否存在"""
        if not os.path.exists(self.source_folder):
            print(f"错误: 源文件夹不存在: {self.source_folder}")
            print("请检查路径是否正确，或使用命令行参数指定正确的源文件夹路径")
            return False
        
        # 确保目标文件夹存在
        try:
            Path(self.target_folder).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"错误: 无法创建目标文件夹 {self.target_folder}: {e}")
            return False
            
        return True
        
    def extract_image_urls_from_md_files(self):
        """从MD文件中提取所有图片链接"""
        print(f"正在从 {self.source_folder} 文件夹中提取图片链接...")
        
        # 查找所有MD文件
        md_pattern = os.path.join(self.source_folder, '*.md')
        md_files = glob.glob(md_pattern)
        
        if not md_files:
            print(f"警告: 在 {self.source_folder} 中没有找到MD文件")
            print("请确保源文件夹中包含.md文件")
            return False
            
        print(f"找到 {len(md_files)} 个MD文件")
        
        # 图片链接的正则表达式
        image_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
        
        for md_file in md_files:
            try:
                print(f"处理文件: {os.path.basename(md_file)}")
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 提取所有图片链接
                matches = re.findall(image_pattern, content)
                for url in matches:
                    self.image_urls.add(url)
                    print(f"  找到图片链接: {url}")
                    
            except Exception as e:
                print(f"  错误: 处理文件 {md_file} 时出错: {e}")
        
        print(f"总共找到 {len(self.image_urls)} 个唯一的图片链接")
        return True
    
    def save_image_urls_to_file(self):
        """将图片链接保存到文件"""
        try:
            with open(self.urls_file, 'w', encoding='utf-8') as f:
                for url in sorted(self.image_urls):
                    f.write(f"{url}\n")
            print(f"[OK] 图片链接已保存到 {self.urls_file}")
            return True
        except Exception as e:
            print(f"错误: 保存图片链接失败: {e}")
            return False
    
    def create_images_directory(self):
        """创建images目录"""
        try:
            Path(self.images_folder).mkdir(parents=True, exist_ok=True)
            print(f"[OK] 图片目录已创建: {self.images_folder}")
            return True
        except Exception as e:
            print(f"错误: 创建图片目录失败: {e}")
            return False
    
    def extract_filename_from_url(self, url):
        """从URL中提取文件名"""
        parsed = urlparse(url)
        path = parsed.path
        filename = os.path.basename(path)
        
        if not filename or '.' not in filename:
            # 如果没有文件名或没有扩展名，使用URL的哈希值
            filename = hashlib.md5(url.encode()).hexdigest() + '.jpg'
        else:
            # 确保文件名唯一
            name, ext = os.path.splitext(filename)
            if not ext:
                ext = '.jpg'
            filename = f"{name}_{hashlib.md5(url.encode()).hexdigest()[:8]}{ext}"
        
        return filename
    
    def download_image(self, url, filename):
        """下载单个图片"""
        try:
            print(f"正在下载: {filename}")
            response = self.session.get(url, timeout=30, stream=True)
            response.raise_for_status()
            
            filepath = os.path.join(self.images_folder, filename)
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # 验证文件大小
            file_size = os.path.getsize(filepath)
            if file_size == 0:
                print(f"警告: {filename} 文件大小为0，可能下载失败")
                return False
            
            print(f"[OK] 下载完成: {filename} ({file_size} bytes)")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] 下载失败 {filename}: {e}")
            return False
        except Exception as e:
            print(f"[ERROR] 保存文件失败 {filename}: {e}")
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
                # 检查GIF文件头
                elif header.startswith(b'GIF87a') or header.startswith(b'GIF89a'):
                    return True
                else:
                    return False
        except Exception:
            return False
    
    def download_all_images(self):
        """下载所有图片"""
        print(f"\n开始下载 {len(self.image_urls)} 个图片...")
        
        successful_downloads = 0
        failed_downloads = 0
        
        for i, url in enumerate(self.image_urls, 1):
            print(f"\n[{i}/{len(self.image_urls)}] 处理: {url}")
            
            filename = self.extract_filename_from_url(url)
            if self.download_image(url, filename):
                filepath = os.path.join(self.images_folder, filename)
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
        
        print(f"\n下载完成: 成功 {successful_downloads}, 失败 {failed_downloads}")
        return successful_downloads > 0
    
    def save_unique_images_to_file(self):
        """保存本地图片链接到文件"""
        try:
            with open(self.unique_images_file, 'w', encoding='utf-8') as f:
                for url, filename in self.downloaded_files.items():
                    local_path = f"images/{filename}"
                    f.write(f"{local_path}\n")
            print(f"[OK] 本地图片链接已保存到 {self.unique_images_file}")
            return True
        except Exception as e:
            print(f"错误: 保存本地图片链接失败: {e}")
            return False
    
    def get_pdf_filename_mapping(self):
        """获取PDF文件名映射"""
        # 尝试多个可能的PDF文件夹位置
        possible_pdf_folders = [
            os.path.join(self.target_folder, '..', 'Documents'),
            os.path.join(self.target_folder, '..', 'PDFs'),
            os.path.join(self.target_folder, '..', 'pdfs'),
            os.path.join(os.path.dirname(self.target_folder), 'Documents'),
            os.path.join(os.path.dirname(self.target_folder), 'PDFs'),
        ]
        
        pdf_mapping = {}
        for pdf_folder in possible_pdf_folders:
            if os.path.exists(pdf_folder):
                pdf_files = glob.glob(os.path.join(pdf_folder, '*.pdf'))
                if pdf_files:
                    print(f"找到PDF文件夹: {pdf_folder}")
                    for pdf_file in pdf_files:
                        pdf_name = os.path.basename(pdf_file)
                        # 提取ISO编号或其他文档编号
                        match = re.search(r'ISO\s+14230-(\d+)', pdf_name)
                        if match:
                            part_num = match.group(1)
                            pdf_mapping[part_num] = pdf_name.replace('.pdf', '.md')
                    break
        
        if not pdf_mapping:
            print("警告: 未找到PDF文件，将使用原始文件名")
        
        return pdf_mapping
    
    def copy_and_update_md_files(self):
        """复制MD文件并更新图片链接"""
        print(f"\n正在复制和更新MD文件...")
        
        # 获取PDF文件名映射
        pdf_mapping = self.get_pdf_filename_mapping()
        if pdf_mapping:
            print(f"PDF文件名映射: {pdf_mapping}")
        
        # 查找所有源MD文件
        md_pattern = os.path.join(self.source_folder, '*.md')
        md_files = glob.glob(md_pattern)
        
        for md_file in md_files:
            try:
                source_name = os.path.basename(md_file)
                print(f"处理文件: {source_name}")
                
                # 确定目标文件名
                target_name = source_name
                if pdf_mapping:
                    for part_num, pdf_name in pdf_mapping.items():
                        if f"14230-{part_num}" in source_name:
                            target_name = pdf_name
                            break
                
                target_file = os.path.join(self.target_folder, target_name)
                print(f"  目标文件名: {target_name}")
                
                # 读取源文件内容
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 替换图片链接
                original_content = content
                replacements = 0
                
                for url, filename in self.downloaded_files.items():
                    # 替换Markdown图片语法中的URL
                    old_pattern = f'![]({url})'
                    # 根据目标文件夹位置计算正确的相对路径
                    if 'ISO14230' in self.target_folder:
                        # 如果在ISO14230子文件夹中，需要回到根目录
                        new_pattern = f'![](../../Image_Processor/images/{filename})'
                    else:
                        # 如果在根目录的Documents Md中，使用原来的路径
                        new_pattern = f'![](../Image_Processor/images/{filename})'
                    if old_pattern in content:
                        content = content.replace(old_pattern, new_pattern)
                        replacements += 1
                        print(f"    替换: {url} -> {new_pattern}")
                
                # 保存更新后的文件
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"  [OK] 文件已保存: {target_name} (替换了 {replacements} 个链接)")
                
            except Exception as e:
                print(f"  [ERROR] 处理文件 {md_file} 时出错: {e}")
    
    def run(self):
        """运行完整的本地化流程"""
        print("=" * 60)
        print("MD文档图片本地化脚本")
        print("=" * 60)
        print(f"源文件夹: {self.source_folder}")
        print(f"目标文件夹: {self.target_folder}")
        print(f"图片文件夹: {self.images_folder}")
        print("=" * 60)
        
        # 验证路径
        if not self.validate_paths():
            return
        
        # 1. 提取图片链接
        if not self.extract_image_urls_from_md_files():
            return
        
        # 2. 保存图片链接到文件
        if not self.save_image_urls_to_file():
            return
        
        # 3. 创建图片目录
        if not self.create_images_directory():
            return
        
        # 4. 下载所有图片
        if not self.download_all_images():
            print("没有成功下载任何图片，跳过后续步骤")
            return
        
        # 5. 保存本地图片链接
        if not self.save_unique_images_to_file():
            return
        
        # 6. 复制和更新MD文件
        self.copy_and_update_md_files()
        
        # 生成报告
        print("\n" + "=" * 60)
        print("本地化完成报告")
        print("=" * 60)
        print(f"源文件夹: {self.source_folder}")
        print(f"目标文件夹: {self.target_folder}")
        print(f"图片文件夹: {self.images_folder}")
        print(f"总图片数量: {len(self.image_urls)}")
        print(f"成功下载: {len(self.downloaded_files)}")
        if len(self.image_urls) > 0:
            print(f"成功率: {len(self.downloaded_files)/len(self.image_urls)*100:.1f}%")
        
        if self.downloaded_files:
            print(f"\n成功下载的文件:")
            for url, filename in self.downloaded_files.items():
                filepath = os.path.join(self.images_folder, filename)
                file_size = os.path.getsize(filepath)
                print(f"  - {filename} ({file_size} bytes)")
        
        print(f"\n图片保存在: {os.path.abspath(self.images_folder)}")
        print(f"图片链接文件: {self.unique_images_file}")
        print(f"URL列表文件: {self.urls_file}")

def main():
    """主函数"""
    # 解析命令行参数
    source_folder = 'source_md'
    target_folder = 'Documents Md'
    
    if len(sys.argv) > 1:
        source_folder = sys.argv[1]
    if len(sys.argv) > 2:
        target_folder = sys.argv[2]
    
    # 显示使用说明
    if len(sys.argv) == 1:
        print("MD文档图片本地化脚本")
        print("=" * 40)
        print("使用方法:")
        print("  python download_images.py [源文件夹] [目标文件夹]")
        print("")
        print("参数说明:")
        print("  源文件夹: 包含MD文件的文件夹路径 (默认: source_md)")
        print("  目标文件夹: 生成的MD文件存放位置 (默认: Documents Md)")
        print("")
        print("示例:")
        print("  python download_images.py")
        print("  python download_images.py \"../my_md_files\" \"../output_md\"")
        print("  python download_images.py \"D:/MyProject/md_source\" \"D:/MyProject/md_output\"")
        print("")
        print("注意: 源文件夹必须包含.md文件，目标文件夹会自动创建")
        print("=" * 40)
        print("")
    
    # 创建本地化器并运行
    localizer = MDImageLocalizer(source_folder, target_folder)
    localizer.run()

if __name__ == "__main__":
    main()
