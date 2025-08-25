# 🚗 ISO 15765 CAN诊断协议文档库

## 📋 分支概述

本分支专门收集和整理ISO 15765标准系列文档，涵盖基于CAN总线的诊断协议(ISO 15765)的完整规范。ISO 15765是现代汽车诊断系统的核心协议，定义了如何在CAN总线上传输UDS诊断服务，是汽车电子诊断的重要标准。

## 📖 协议标准

### ISO 15765-1: 总体信息
- **标准名称**: Road vehicles — Diagnostic communication over Controller Area Network (DoCAN) — Part 1: General information and use case definition
- **文档**: `ISO 15765[1].1（2004）道路车辆__控制局域网络诊断__第1部分：总体信息.pdf`
- **内容**: 协议概述、用例定义、应用场景、架构说明

### ISO 15765-2: 网络层服务
- **标准名称**: Road vehicles — Diagnostic communication over Controller Area Network (DoCAN) — Part 2: Transport protocol and network layer services
- **文档**: `ISO 15765[1].2（2004）道路车辆__控制局域网络诊断__第2部分：网络层服务.pdf`, `ISO15765-2-2016.pdf`
- **内容**: 网络层协议、传输协议、流控制、时序要求

### ISO 15765-3: 一元化诊断服务实施
- **标准名称**: Road vehicles — Diagnostic communication over Controller Area Network (DoCAN) — Part 3: Implementation of unified diagnostic services (UDS on CAN)
- **文档**: `ISO 15765.3（2004）道路车辆__控制局域网络诊断__第3部分：一元化诊断服务实施（CAN的UDS）.pdf`
- **内容**: UDS服务在CAN上的实现、诊断服务定义、协议栈

### ISO 15765-4: 排放相关系统要求
- **标准名称**: Road vehicles — Diagnostic communication over Controller Area Network (DoCAN) — Part 4: Requirements for emission-related systems
- **文档**: `ISO 15765[1].4（2005）道路车辆__控制局域网络诊断__第4部分：排放相关系统要求.pdf`
- **内容**: 排放系统诊断要求、OBD-II兼容性、法规要求

### 其他文档
- `ISO 15765-2-2004ocr.pdf` - 2004版第2部分OCR版本
- `ISO 15765-3.5 Implementation of diagnostic services.pdf` - 诊断服务实施指南

## 🎯 核心特性

### 通信特性
- **传输介质**: CAN总线
- **传输速率**: 125 kbps - 1 Mbps
- **网络拓扑**: 总线结构
- **协议栈**: CAN + ISO 15765 + UDS

### 协议优势
- **标准化**: 国际标准，广泛支持
- **兼容性**: 与UDS协议完全兼容
- **可靠性**: 基于CAN总线的可靠传输
- **实时性**: 支持实时诊断通信

## 📁 文档结构

```
ISO15765/
├── README.md                    # 本文件 - 分支说明
├── Documents/                   # 标准文档
│   ├── ISO 15765[1].1（2004）...pdf # 第1部分：总体信息
│   ├── ISO 15765[1].2（2004）...pdf # 第2部分：网络层服务
│   ├── ISO 15765.3（2004）...pdf    # 第3部分：一元化诊断服务
│   ├── ISO 15765[1].4（2005）...pdf # 第4部分：排放相关系统
│   ├── ISO15765-2-2016.pdf         # 2016版第2部分
│   ├── ISO 15765-2-2004ocr.pdf     # 2004版第2部分OCR版
│   └── ISO 15765-3.5...pdf         # 诊断服务实施指南
├── Summary/                     # 协议摘要
├── Implementation/              # 实现指南
└── Image_Processor/             # 图片处理工具
```

## 🛠️ 使用指南

### 开发人员
1. **阅读标准**: 查看Documents目录中的PDF文档
2. **参考摘要**: 阅读Summary目录中的协议摘要
3. **实现开发**: 参考Implementation目录中的实现指南
4. **工具使用**: 利用Image_Processor处理文档图片

### 研究人员
- 深入分析CAN诊断协议架构
- 研究网络层传输机制
- 了解UDS服务实现
- 对比不同版本标准

## 🔧 技术要点

### 协议栈
- **应用层**: UDS诊断服务
- **传输层**: ISO 15765网络层
- **数据链路层**: CAN协议
- **物理层**: CAN总线

### 网络层功能
- **分段传输**: 大数据包分段处理
- **流控制**: 发送方和接收方流控制
- **时序管理**: 超时和重传机制
- **错误处理**: 网络层错误检测和恢复

### 诊断服务
- **诊断会话控制**: 会话管理
- **安全访问**: 安全认证
- **数据读写**: 参数读写服务
- **例程控制**: 测试例程执行
- **输入输出控制**: I/O控制服务

## 📈 应用领域

### 汽车诊断
- 4S店诊断系统
- 车载诊断设备
- 开发测试工具
- 质量检测系统

### 排放控制
- OBD-II系统
- 排放监测
- 环保法规符合性
- 故障码管理

### 研发测试
- 协议栈开发
- 兼容性测试
- 性能验证
- 故障注入测试

## 🔗 相关标准

- **ISO 15765**: CAN诊断协议系列
- **ISO 14229**: UDS诊断服务
- **ISO 11898**: CAN总线协议
- **ISO 15031**: OBD-II标准
- **SAE J1979**: OBD-II诊断测试模式

## 📞 技术支持

如有技术问题或需要补充文档，请通过以下方式联系：
- GitHub Issues: [项目问题反馈](https://github.com/duanhaoyu88/ISO/issues)
- GitHub Discussions: [技术讨论](https://github.com/duanhaoyu88/ISO/discussions)

---

*最后更新: 2024年8月25日*

*本分支致力于为CAN诊断协议开发提供完整的技术文档和实现指南。*
