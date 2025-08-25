# 图片下载工具使用说明

## 概述

本工具包含两个脚本，用于从ISO文档中提取和下载图片：

1. **download_images.sh** - Bash脚本（适用于Linux/Mac/Git Bash）
2. **download_images.py** - Python脚本（跨平台通用）

## Python脚本使用说明

### 功能特点

- ✅ 支持多种URL格式（纯URL、Markdown图片语法）
- ✅ 自动创建images文件夹
- ✅ 智能文件名提取
- ✅ 图片文件完整性验证
- ✅ 详细的下载报告
- ✅ 错误处理和重试机制
- ✅ 跨平台兼容

### 安装依赖

```bash
pip install -r requirements.txt
```

### 使用方法

#### 1. 基本使用（使用默认image_urls.txt文件）

```bash
python download_images.py
```

#### 2. 指定URL文件

```bash
python download_images.py my_urls.txt
```

#### 3. 在不同目录中使用

```bash
python download_images.py /path/to/urls.txt
```

### URL文件格式

支持以下格式：

#### 格式1：纯URL
```
https://cdn-mineru.openxlab.org.cn/result/2025-08-22/xxx/image1.jpg
https://cdn-mineru.openxlab.org.cn/result/2025-08-22/xxx/image2.jpg
```

#### 格式2：Markdown图片语法
```
![](https://cdn-mineru.openxlab.org.cn/result/2025-08-22/xxx/image1.jpg)
![](https://cdn-mineru.openxlab.org.cn/result/2025-08-22/xxx/image2.jpg)
```

#### 格式3：混合格式
```
# 这是注释
https://cdn-mineru.openxlab.org.cn/result/2025-08-22/xxx/image1.jpg
![](https://cdn-mineru.openxlab.org.cn/result/2025-08-22/xxx/image2.jpg)
```

### 输出结果

脚本会在当前目录下创建`images`文件夹，并下载所有图片。

### 示例输出

```
============================================================
通用图片下载脚本
============================================================
正在读取URL文件: image_urls.txt
找到 27 个图片URL
✓ 输出目录已创建/确认: images

开始下载图片...

[1/27] 处理: https://cdn-mineru.openxlab.org.cn/result/2025-08-22/xxx/image1.jpg
正在下载: image1.jpg
✓ 下载完成: image1.jpg (22938 bytes)

...

============================================================
下载完成报告
============================================================
总URL数量: 27
成功下载: 27
下载失败: 0
成功率: 100.0%

成功下载的文件:
  - image1.jpg (22938 bytes)
  - image2.jpg (38685 bytes)
  ...

图片保存在: /path/to/images
```

## Bash脚本使用说明

### 使用方法

```bash
chmod +x download_images.sh
./download_images.sh
```

### 特点

- 适用于Linux/Mac/Git Bash环境
- 使用curl命令下载
- 支持断点续传
- 自动创建images目录

## 在不同分支中使用

### 1. 复制工具到新分支

```bash
# 切换到新分支
git checkout -b new-iso-branch

# 复制工具文件
cp download_images.py /path/to/new/iso/folder/
cp requirements.txt /path/to/new/iso/folder/
cp README_图片下载工具.md /path/to/new/iso/folder/
```

### 2. 准备URL文件

在新分支中创建`image_urls.txt`文件，包含该ISO文档的图片URL。

### 3. 运行下载

```bash
cd /path/to/new/iso/folder/
python download_images.py
```

## 故障排除

### 常见问题

1. **网络连接问题**
   - 检查网络连接
   - 尝试使用VPN
   - 增加超时时间

2. **权限问题**
   - 确保有写入权限
   - 使用管理员权限运行

3. **依赖问题**
   - 重新安装依赖：`pip install -r requirements.txt`
   - 检查Python版本（建议3.6+）

4. **文件格式问题**
   - 确保URL文件使用UTF-8编码
   - 检查URL格式是否正确

### 调试模式

在Python脚本中添加调试信息：

```python
# 在脚本开头添加
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 版本历史

- v1.0.0 - 初始版本，支持基本下载功能
- v1.1.0 - 添加图片完整性验证
- v1.2.0 - 支持Markdown图片语法
- v1.3.0 - 添加详细报告和错误处理
