# 🚀 快速开始指南

## 一句话说明
这个脚本用于将MD文档中的在线图片链接下载到本地，并更新文档中的图片链接为本地路径。

## 核心功能
1. 从指定文件夹读取MD文件，提取图片链接
2. 下载所有图片到本地images文件夹
3. 复制MD文件到目标文件夹，替换图片链接为本地路径

## 快速使用

### 方法1: 使用默认路径（推荐）
```bash
cd Image_Processor
python download_images.py
```
**默认路径**:
- 源文件夹: `../source_md` (包含原始MD文件)
- 目标文件夹: `../Documents Md` (生成的MD文件)

### 方法2: 指定自定义路径
```bash
python download_images.py "源文件夹路径" "目标文件夹路径"
```

### 实际示例
```bash
# 处理ISO文档
python download_images.py "D:\01_MyGit\ISO\官网" "D:\01_MyGit\ISO\ISO14230\Documents Md"

# 处理其他项目
python download_images.py "D:\MyProject\md_source" "D:\MyProject\md_output"
```

## 输入要求
- **源文件夹**: 必须包含.md文件
- **网络连接**: 用于下载图片

## 输出结果
- **目标文件夹**: 更新后的MD文件（图片链接指向本地）
- **images/**: 下载的图片文件
- **image_urls.txt**: 原始图片URL列表
- **unique_images.txt**: 本地图片路径列表

## 图片链接格式
**原始**: `![](https://example.com/image.jpg)`
**更新后**: `![](../Image_Processor/images/image_abc123.jpg)`

## 常见用法场景

### 场景1: 处理ISO文档
```bash
python download_images.py "D:\01_MyGit\ISO\官网" "D:\01_MyGit\ISO\ISO14230\Documents Md"
```

### 场景2: 处理博客文章
```bash
python download_images.py "D:\Blog\posts" "D:\Blog\local_posts"
```

### 场景3: 处理技术文档
```bash
python download_images.py "D:\Docs\markdown" "D:\Docs\local_markdown"
```

## 注意事项
- 脚本会自动创建目标文件夹
- 支持JPEG、PNG、GIF图片格式
- 自动处理文件名冲突
- 包含错误处理和重试机制

## 故障排除
如果遇到问题，检查：
1. 源文件夹是否存在且包含.md文件
2. 网络连接是否正常
3. 是否有足够的文件权限
