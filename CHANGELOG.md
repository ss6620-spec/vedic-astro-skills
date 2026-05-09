# 📋 Changelog

All notable changes to this project will be documented in this file.

---

## [v4.0] - 2026-05-10

> **工程化重构** — 以实测反馈驱动的全面体验升级

### 🔧 Reader (vedic-reader)

#### Added
- **强制双通道PDF提取**：PyMuPDF文本层 + AI视觉识别同时执行，交叉验证
- **智能引导开场白**：三种输入方式按推荐程度排序（文字粘贴→PDF→截图）
- **JH导出指南**：5步表格复制操作指引 + South Indian (Regular) 设置建议
- **陈述式验前事**：从提问式改为占星师"验身"式陈述（"您应该是..."）
- **信息补充窗口**：验前事后开放用户补充重大人生事件信息
- **时间精度→分盘启用矩阵**：精度不够直接禁用高敏感分盘
- **校准推荐决策树**：精度不足时完整的推荐→接受/拒绝→后续处理流程
- **南/北印盘识别指引**：快速识别方法 + 推荐南印度盘 (Regular)
- **12个触发词**：新增"印占""占星""vedic""激活占星""看盘""排盘"等

#### Changed
- **验前事阈值收紧**：3/5命中不再被视为"可接受"，现在≤3/5=低→推荐校准
- **ABC矫正触发条件**：从仅度数条件扩展为度数 OR 验前事≤3/5
- **校验规则**：12条→16条（新增燃烧、行星战争、Sandhi/Gandanta、盈月亏月）
- **措辞统一**：全部"盘面初验"→"验前事"

#### Fixed
- OCR跳过问题：禁止跳过PyMuPDF直接视觉识别

### 🔬 Rectifier (vedic-rectifier)

#### Added
- **改时间硬性条件**：必须同时满足3条才能修改出生时间
- **防过度校准规则**：5/5匹配绝对禁止进入扫描

#### Changed
- 核心理念转变：校准≠必须改时间，确认正确也是有效输出

### 📦 Cross-Skill

#### Changed
- Career/Love YAML描述去JH限定，改为通用占星软件表述
- Career yogas引用路径修正为显式跨Skill引用
- data_contract校验模板从12条扩充至16条

---

## [v3.2] - 2026-05-08

### Added
- Reader通用提取架构：从JH专用→任意占星软件
- 引导开场白（初版）
- 三级数据清单（🔴关键/🟡重要/🟢可选）
- 触发词扩展

---

## [v3.1] - 2026-05-07

### Added
- Chehil独立审计对比合入
- 燃烧 (Combustion) 检测
- 行星战争 (Planetary War) 检测
- Dig Bala 方位力量

### Fixed
- 移除150行硬限制（导致内容压缩）

---

## [v3.0] - 2026-05-06

### Added
- **五Skill架构**：reader / core / career / love / rectifier
- vedic-rectifier 上线（5事件逆推出生时间，精度±5分钟）
- 正反双审 (Double Blind Audit) 机制
- D9身份继承矩阵五维分析
- Badhaka/Maraka审计模块

---

## [v2.x] - 2026-05-05

### Added
- Q&A规则外置 (qa_rules.md)
- HTML报告生成脚本 (report_builder.py)
- 报告打包规则 (report_rules.md)
- 语言风格规范同步至career/love

---

## [v1.x] - 2026-05-04

### Added
- 初始三Skill架构（core/career/love）
- 验前事反转：AI先预测，用户确认
- 十大板块白话文总结模板
- Claude Code命令支持
