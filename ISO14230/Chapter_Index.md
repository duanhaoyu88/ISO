# 📖 ISO 14230 章节索引

## 📋 概述
本文档提供ISO 14230系列标准的详细章节内容索引，包含每个章节的具体内容、关键参数、实现要点和注意事项，为开发人员和AI工具提供深度查询支持。

## 📚 ISO 14230-1: 物理层规范

### 第1章: Scope (适用范围)
**内容**: 定义标准的适用范围和目的  
**关键要点**:
- 适用于道路车辆诊断系统
- 定义KWP2000物理层要求
- 与ISO 9141-2兼容性要求

### 第2章: Normative references (引用标准)
**内容**: 列出所有引用的标准文档  
**重要引用**:
- ISO 9141-2: 道路车辆诊断系统
- ISO 11898: CAN总线标准
- IEC 60068: 环境试验标准

### 第3章: Terms and definitions (术语和定义)
**内容**: 定义关键术语和概念  
**重要术语**:
- **Diagnostic Link**: 诊断链路
- **Keyword Protocol**: 关键词协议
- **Physical Layer**: 物理层
- **Interface**: 接口

### 第4章: Abbreviations (缩写词)
**内容**: 列出所有缩写词  
**常用缩写**:
- KWP: Keyword Protocol
- ECU: Electronic Control Unit
- OBD: On-Board Diagnostics
- UART: Universal Asynchronous Receiver/Transmitter

### 第5章: Physical layer requirements (物理层要求)
**内容**: 定义物理层基本要求  
**关键要求**:
- 接口类型: 单线或双线接口
- 通信方式: 异步串行通信
- 波特率: 10400, 9600, 4800 bps
- 数据格式: 8位数据, 1位停止位, 无校验

### 第6章: Electrical characteristics (电气特性)
**内容**: 详细的电气参数规范  
**关键参数**:
| 参数 | 最小值 | 典型值 | 最大值 | 单位 |
|------|--------|--------|--------|------|
| 高电平电压 | 4.0 | 5.0 | 6.0 | V |
| 低电平电压 | 0.0 | 0.0 | 0.8 | V |
| 输入阻抗 | 10 | - | - | kΩ |
| 输出电流 | - | - | 20 | mA |

**实现要点**:
- 电平转换电路设计
- 输入保护电路
- 输出驱动能力

### 第7章: Interface requirements (接口要求)
**内容**: 接口连接器和引脚定义  
**连接器规范**:
- 标准OBD-II连接器
- 引脚分配: K线(7号), L线(15号)
- 屏蔽要求: 电磁兼容性

**引脚定义**:
- **K线**: 主要通信线
- **L线**: 辅助通信线(可选)
- **电源**: 12V供电
- **地线**: 信号地

### 第8章: Timing requirements (时序要求)
**内容**: 通信时序规范  
**关键时序**:
| 参数 | 最小值 | 最大值 | 单位 |
|------|--------|--------|------|
| 帧间隔 | 5 | - | ms |
| 响应时间 | - | 50 | ms |
| 超时时间 | 1000 | - | ms |
| 位时间 | - | 96 | μs |

**时序控制**:
- 初始化时序
- 通信时序
- 超时处理

### 第9章: Test requirements (测试要求)
**内容**: 物理层测试方法  
**测试项目**:
- 电气特性测试
- 时序测试
- 兼容性测试
- 环境测试

---

## 📚 ISO 14230-2: 数据链路层规范

### 第1章: Scope (适用范围)
**内容**: 定义数据链路层协议范围  
**关键要点**:
- 定义消息格式和传输协议
- 实现错误检测和恢复
- 管理通信状态

### 第2章: Normative references (引用标准)
**内容**: 相关标准引用  
**重要引用**:
- ISO 14230-1: 物理层规范
- ISO 11898: CAN协议
- ISO 9141-2: 诊断系统

### 第3章: Terms and definitions (术语和定义)
**内容**: 数据链路层术语  
**重要术语**:
- **Message**: 消息
- **Frame**: 帧
- **Checksum**: 校验和
- **Flow Control**: 流控制

### 第4章: Abbreviations (缩写词)
**内容**: 协议相关缩写  
**常用缩写**:
- DLL: Data Link Layer
- SID: Service Identifier
- NRC: Negative Response Code
- SID: Service Identifier

### 第5章: Data link layer services (数据链路层服务)
**内容**: 定义服务原语和功能  
**服务类型**:
- **DL_Data.request**: 数据发送请求
- **DL_Data.indication**: 数据接收指示
- **DL_Status.indication**: 状态指示

### 第6章: Message format (消息格式)
**内容**: 定义消息帧结构  
**帧格式**:
```
[Format][Target][Source][Length][Data...][Checksum]
```

**字段定义**:
- **Format**: 消息格式标识
- **Target**: 目标地址
- **Source**: 源地址
- **Length**: 数据长度
- **Data**: 数据内容
- **Checksum**: 校验和

**消息类型**:
- **Single Frame**: 单帧消息
- **First Frame**: 首帧消息
- **Consecutive Frame**: 连续帧
- **Flow Control Frame**: 流控制帧

### 第7章: Protocol control (协议控制)
**内容**: 协议状态机和流程控制  
**状态定义**:
- **IDLE**: 空闲状态
- **INIT**: 初始化状态
- **COMMUNICATING**: 通信状态
- **ERROR**: 错误状态

**状态转换**:
```
IDLE → INIT → COMMUNICATING → ERROR → IDLE
```

**流程控制**:
- 初始化序列
- 通信建立
- 数据传输
- 通信结束

### 第8章: Error handling (错误处理)
**内容**: 错误检测和恢复机制  
**错误类型**:
- **Timeout Error**: 超时错误
- **Checksum Error**: 校验错误
- **Format Error**: 格式错误
- **Sequence Error**: 序列错误

**错误处理**:
- 错误检测
- 错误报告
- 错误恢复
- 重传机制

### 第9章: Timing requirements (时序要求)
**内容**: 协议时序规范  
**关键时序**:
| 参数 | 最小值 | 最大值 | 单位 |
|------|--------|--------|------|
| 帧间隔 | 5 | - | ms |
| 响应时间 | - | 50 | ms |
| 重传时间 | 100 | 1000 | ms |

### 第10章: Test requirements (测试要求)
**内容**: 协议测试方法  
**测试项目**:
- 消息格式测试
- 协议流程测试
- 错误处理测试
- 性能测试

---

## 📚 ISO 14230-3: 应用层规范

### 第1章: Scope (适用范围)
**内容**: 定义应用层服务范围  
**关键要点**:
- 定义诊断服务集
- 实现会话管理
- 提供安全访问

### 第2章: Normative references (引用标准)
**内容**: 应用层相关标准  
**重要引用**:
- ISO 14230-2: 数据链路层
- ISO 15031: OBD标准
- ISO 15765: CAN诊断

### 第3章: Terms and definitions (术语和定义)
**内容**: 应用层术语定义  
**重要术语**:
- **Service**: 服务
- **Session**: 会话
- **Security Access**: 安全访问
- **Routine**: 例程

### 第4章: Abbreviations (缩写词)
**内容**: 服务相关缩写  
**常用缩写**:
- SID: Service Identifier
- NRC: Negative Response Code
- DTC: Diagnostic Trouble Code
- PID: Parameter Identifier

### 第5章: Application layer services (应用层服务)
**内容**: 定义服务原语  
**服务类型**:
- **AL_Data.request**: 数据请求
- **AL_Data.indication**: 数据指示
- **AL_Status.indication**: 状态指示

### 第6章: Diagnostic services (诊断服务)
**内容**: 具体诊断服务实现  
**核心服务**:
- **0x10**: Diagnostic Session Control
- **0x11**: ECU Reset
- **0x14**: Clear Diagnostic Information
- **0x19**: Read DTC Information
- **0x22**: Read Data by Identifier
- **0x23**: Read Memory by Address
- **0x27**: Security Access
- **0x28**: Communication Control
- **0x2E**: Write Data by Identifier
- **0x2F**: Input Output Control by Identifier
- **0x31**: Routine Control
- **0x34**: Request Download
- **0x35**: Request Upload
- **0x36**: Transfer Data
- **0x37**: Request Transfer Exit

### 第7章: Session control (会话控制)
**内容**: 会话管理机制  
**会话类型**:
- **Default Session**: 默认会话
- **Programming Session**: 编程会话
- **Extended Session**: 扩展会话
- **Safety Session**: 安全会话

**会话管理**:
- 会话切换
- 会话保持
- 会话超时
- 会话恢复

### 第8章: Security access (安全访问)
**内容**: 安全访问实现  
**安全级别**:
- **Level 1**: 基本访问
- **Level 2**: 扩展访问
- **Level 3**: 编程访问
- **Level 4**: 安全访问

**访问流程**:
1. 发送安全访问请求
2. 接收种子(Seed)
3. 计算密钥(Key)
4. 发送密钥验证
5. 获得访问权限

### 第9章: Data access (数据访问)
**内容**: 数据读写服务  
**数据标识符**:
- **0xF100-0xF1FF**: 车辆信息
- **0xF200-0xF2FF**: 系统信息
- **0xF300-0xF3FF**: 诊断信息

**访问方式**:
- 按标识符读取
- 按地址读取
- 按标识符写入
- 按地址写入

### 第10章: Input/Output control (输入输出控制)
**内容**: I/O控制服务  
**控制类型**:
- **Return Control to ECU**: 返回控制
- **Reset to Default**: 重置默认
- **Freeze Current Data**: 冻结当前数据
- **Short Term Adjustment**: 短期调整

### 第11章: Routine control (例程控制)
**内容**: 例程执行控制  
**例程类型**:
- **Start Routine**: 启动例程
- **Stop Routine**: 停止例程
- **Request Routine Results**: 请求例程结果

**例程标识符**:
- **0x0100-0x01FF**: 系统测试
- **0x0200-0x02FF**: 功能测试
- **0x0300-0x03FF**: 诊断测试

### 第12章: Upload/Download (上传下载)
**内容**: 数据传输服务  
**传输流程**:
1. 请求下载/上传
2. 数据传输
3. 传输退出

**传输参数**:
- 数据大小
- 传输模式
- 校验方式

### 第13章: Communication control (通信控制)
**内容**: 通信参数控制  
**控制类型**:
- **Enable Rx and Tx**: 启用收发
- **Enable Rx and Disable Tx**: 启用接收禁用发送
- **Disable Rx and Enable Tx**: 禁用接收启用发送
- **Disable Rx and Tx**: 禁用收发

### 第14章: Test requirements (测试要求)
**内容**: 应用层测试方法  
**测试项目**:
- 服务功能测试
- 会话管理测试
- 安全访问测试
- 性能测试

---

## 📚 ISO 14230-4: 排放相关系统要求

### 第1章: Scope (适用范围)
**内容**: 排放系统诊断要求  
**关键要点**:
- 定义OBD系统要求
- 排放法规合规
- 环保标准满足

### 第2章: Normative references (引用标准)
**内容**: 排放相关标准  
**重要引用**:
- ISO 15031: OBD标准
- ISO 14230-3: 应用层
- 各国排放法规

### 第3章: Terms and definitions (术语和定义)
**内容**: 排放系统术语  
**重要术语**:
- **OBD**: On-Board Diagnostics
- **MIL**: Malfunction Indicator Lamp
- **DTC**: Diagnostic Trouble Code
- **Freeze Frame**: 冻结帧

### 第4章: Abbreviations (缩写词)
**内容**: 排放系统缩写  
**常用缩写**:
- OBD: On-Board Diagnostics
- MIL: Malfunction Indicator Lamp
- DTC: Diagnostic Trouble Code
- PID: Parameter Identifier

### 第5章: General requirements (通用要求)
**内容**: 基本诊断要求  
**通用要求**:
- 诊断功能完整性
- 数据可访问性
- 故障检测能力
- 信息显示要求

### 第6章: OBD requirements (OBD要求)
**内容**: 车载诊断系统要求  
**OBD功能**:
- 故障检测
- 故障存储
- 故障显示
- 故障清除

**排放相关系统**:
- 发动机控制系统
- 排放控制系统
- 燃油系统
- 点火系统

### 第7章: Test requirements (测试要求)
**内容**: 排放系统测试方法  
**测试项目**:
- OBD功能测试
- 排放测试
- 耐久性测试
- 环境测试

### 第8章: Data requirements (数据要求)
**内容**: 排放数据规范  
**数据要求**:
- 实时数据
- 冻结帧数据
- 故障码数据
- 测试结果数据

### 第9章: Communication requirements (通信要求)
**内容**: 排放通信规范  
**通信要求**:
- 数据访问速度
- 通信可靠性
- 数据完整性
- 兼容性要求

---

## 🔍 快速查询索引

### 按技术领域查询
| 技术领域 | 主要章节 | 关键内容 |
|----------|----------|----------|
| 硬件设计 | ISO 14230-1 第5-8章 | 电气特性、接口规范 |
| 协议开发 | ISO 14230-2 第5-8章 | 消息格式、协议控制 |
| 服务实现 | ISO 14230-3 第6-13章 | 诊断服务、会话管理 |
| 排放系统 | ISO 14230-4 第6-8章 | OBD要求、排放数据 |

### 按开发任务查询
| 开发任务 | 重点章节 | 实现要点 |
|----------|----------|----------|
| 接口设计 | ISO 14230-1 第6-7章 | 电气参数、引脚定义 |
| 协议栈 | ISO 14230-2 第6-7章 | 消息格式、状态机 |
| 诊断服务 | ISO 14230-3 第6-8章 | 服务定义、安全访问 |
| 排放合规 | ISO 14230-4 第6-8章 | OBD功能、数据要求 |

### 按问题类型查询
| 问题类型 | 解决方案章节 | 关键参数 |
|----------|--------------|----------|
| 通信问题 | ISO 14230-1 第8章, ISO 14230-2 第8章 | 时序要求、错误处理 |
| 接口问题 | ISO 14230-1 第6-7章 | 电气特性、接口规范 |
| 服务问题 | ISO 14230-3 第6-8章 | 服务定义、参数格式 |
| 合规问题 | ISO 14230-4 第6-8章 | OBD要求、测试方法 |

---

## 🔄 版本信息
- **文档版本**: v1.0.0
- **创建日期**: 2024年8月22日
- **最后更新**: 2024年8月22日
- **适用标准**: ISO 14230:1999

---
*本文档提供ISO 14230系列标准的详细章节内容索引，为开发人员和AI工具提供深度技术查询支持。*
