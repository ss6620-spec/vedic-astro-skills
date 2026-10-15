# vedic-synastry 使用指南

`vedic-synastry` 是双人关系分析 skill，用于比较两份已经结构化的吠陀星盘数据，生成关系性质、承载力、互动触发点与时间窗口分析。

## 输入要求

至少需要两份 `structured_data.md`：

- A 方：`<A>/structured_data.md`
- B 方：`<B>/structured_data.md`

如果其中一方尚未有结构化数据，应先通过：

1. `vedic-reader` 从 PDF、截图或文本中提取；或
2. `vedic-calculator` 根据出生时间、地点直接计算。

## 推荐工作流

```bash
python scripts/validate_synastry_data.py <A_structured_data.md> <B_structured_data.md>
python scripts/build_synastry_data.py <A_structured_data.md> <B_structured_data.md> <output_dir> --a <A_name> --b <B_name>
```

生成的 `<output_dir>/synastry_data.md` 是后续合盘分析的计算中间层，包含：

- Ashtakoota / 月宿筛查原料
- 双向落宫
- 跨盘 Drishti / 相位信号
- 关键 Karaka、UL、AL、D9、Dasha 对照原料

## 分析层级

建议按以下顺序输出：

1. **Layer 0：关系性质指纹**  
   先判断关系是偏恋爱、婚姻、合作、家庭、朋友，还是混合关系，不直接下结论。

2. **Layer 1：双方个人关系承载卡**  
   分别看 A 与 B 能提供什么、需要什么、压力下如何失衡。

3. **Layer 2：跨盘触发机制**  
   分 A→B 与 B→A 两个方向分析，不合并为单一匹配度。

4. **Layer 3：关系框架分析**  
   根据关系类型选择 romantic、family、business、friendship 或 general 框架。

5. **Layer 4：时间窗口与现实建议**  
   使用双方 Dasha、D9、UL、7 宫、Karaka、Shadbala / Ashtakavarga 作为参考。

## 输出规则

- 不输出笼统“匹配度总分”。
- 不使用西方占星合盘话术替代吠陀判据。
- 不在缺少双方数据时给出具体互动结论。
- 追问同一对关系时，优先复用已有 `synastry_data.md` 与报告，不重复跑 pipeline。
- 所有判断都应引用具体盘面依据或 `synastry_data.md` 字段。

## 典型目录

```text
synastry_<B>_<YYYYMMDD>/
├── synastry_data.md
├── reports/
│   ├── 00_signal_triage.md
│   ├── 01_individual_capacity.md
│   ├── 02_cross_triggers.md
│   ├── 03_relationship_framework.md
│   └── 04_timing_and_advice.md
└── qa_<topic>.md
```
