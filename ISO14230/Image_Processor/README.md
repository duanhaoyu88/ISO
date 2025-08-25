# Image_Processor 图片处理工具

## 概述

这个文件夹包含了MD文档图片本地化处理的所有工具和资源文件。该工具可以将MD文档中的在线图片链接下载到本地，并更新文档中的链接，避免因网络问题导致的图片无法显示。

## 文件结构

```
Image_Processor/
├── download_images.py      # 主处理脚本
├── image_urls.txt         # 原始图片URL列表
├── unique_images.txt      # 本地图片路径列表
├── images/                # 下载的图片文件夹
│   └── *.jpg             # 所有下载的图片文件
└── README.md             # 本说明文件
```

## 功能说明

### download_images.py
- **功能**: MD文档图片本地化脚本
- **主要特性**:
  - 从指定文件夹读取MD文件并提取图片链接
  - 下载所有图片到本地images文件夹
  - 生成本地图片路径列表
  - 复制MD文件到目标文件夹并更新图片链接
  - 自动匹配PDF文件名（如果存在）

### image_urls.txt
- **内容**: 从MD文件中提取的所有原始图片URL
- **格式**: 每行一个URL
- **用途**: 记录所有需要下载的图片链接

### unique_images.txt
- **内容**: 成功下载的图片的本地路径
- **格式**: 每行一个本地路径 (如: `images/filename.jpg`)
- **用途**: 记录所有本地图片的相对路径

### images/
- **内容**: 所有下载的图片文件
- **命名规则**: 基于原始URL生成唯一文件名
- **格式**: 支持JPEG、PNG、GIF等常见图片格式

## 使用方法

### 基本用法（推荐）
```bash
cd Image_Processor
python download_images.py
```
这将使用默认路径：
- 源文件夹: `../source_md`
- 目标文件夹: `../Documents Md`

### 指定自定义路径
```bash
python download_images.py "源文件夹路径" "目标文件夹路径"
```

### 使用示例

#### 示例1: 使用默认路径
```bash
# 确保在Image_Processor文件夹中
cd Image_Processor
python download_images.py
```

#### 示例2: 指定绝对路径
```bash
python download_images.py "D:\MyProject\md_source" "D:\MyProject\md_output"
```

#### 示例3: 指定相对路径
```bash
python download_images.py "../my_md_files" "../output_md"
```

#### 示例4: 处理ISO文档
```bash
python download_images.py "D:\01_MyGit\ISO\官网" "D:\01_MyGit\ISO\ISO14230\Documents Md"
```

## 工作流程

1. **路径验证**: 检查源文件夹是否存在，创建目标文件夹
2. **提取链接**: 从源文件夹的MD文件中提取所有图片URL
3. **下载图片**: 将所有图片下载到images文件夹
4. **生成列表**: 创建本地图片路径列表
5. **更新文档**: 复制MD文件到目标文件夹，并将图片链接替换为本地路径
6. **文件名匹配**: 如果存在PDF文件，自动匹配文件名

## 输出结果

- **目标文件夹**: 包含更新后的MD文件，图片链接指向本地文件
- **图片链接格式**: `![](../Image_Processor/images/filename.jpg)`
- **文件名映射**: 自动匹配PDF文件名（如果存在）

## 配置说明

### 默认路径设置
- **源文件夹**: `../source_md` - 包含原始MD文件的文件夹
- **目标文件夹**: `../Documents Md` - 生成的MD文件存放位置
- **图片文件夹**: `./images` - 下载的图片存放位置

### PDF文件名匹配
脚本会自动查找以下位置的PDF文件进行文件名匹配：
- `../Documents/`
- `../PDFs/`
- `../pdfs/`
- 其他常见PDF文件夹位置

## 注意事项

- **源文件夹要求**: 必须包含.md文件
- **网络连接**: 需要网络连接来下载图片
- **文件权限**: 确保有足够的权限创建文件夹和文件
- **文件名冲突**: 脚本会自动处理文件名冲突
- **图片验证**: 自动验证下载图片的有效性
- **错误处理**: 包含完善的错误处理和重试机制

## 依赖要求

- **Python版本**: 3.6+
- **必需库**: 
  - `requests` - 用于网络请求
  - `pathlib` - 用于路径处理
  - `urllib3` - 用于SSL处理
- **网络连接**: 用于下载图片

## 安装依赖

```bash
pip install requests urllib3
```

## 故障排除

### 常见问题

1. **源文件夹不存在**
   ```
   错误: 源文件夹不存在: ../source_md
   ```
   **解决方案**: 使用命令行参数指定正确的源文件夹路径

2. **没有找到MD文件**
   ```
   警告: 在 ../source_md 中没有找到MD文件
   ```
   **解决方案**: 确保源文件夹中包含.md文件

3. **下载失败**
   ```
   [ERROR] 下载失败 filename: Connection timeout
   ```
   **解决方案**: 检查网络连接，或稍后重试

4. **权限错误**
   ```
   错误: 无法创建目标文件夹
   ```
   **解决方案**: 检查文件夹权限，或选择有写入权限的路径

### 调试模式

运行脚本时会显示详细的执行信息，包括：
- 找到的MD文件数量
- 提取的图片链接
- 下载进度
- 文件替换情况
- 最终统计报告

## 扩展功能

### 自定义PDF文件夹
如果需要自定义PDF文件夹位置，可以修改脚本中的 `possible_pdf_folders` 列表。

### 支持更多图片格式
脚本支持JPEG、PNG、GIF格式，如需支持其他格式，可以修改 `validate_image_file` 函数。

### 批量处理
脚本支持批量处理多个文件夹，只需多次运行即可。

## 版本信息

- **版本**: 1.0
- **更新日期**: 2024年
- **兼容性**: Windows, macOS, Linux
