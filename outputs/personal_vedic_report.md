## 元信息

```
出生日期: 1997-08-25
出生时间: 12:35
出生地点: 中国安徽合肥 (117.2272, 31.8206)
时间精度: 精确到分钟
时间来源: 用户提供
有效精度: ±分钟级
验证轨道: 轨道1-标准
读盘方式: vedic-calculator直接计算
Ayanamsa: Lahiri (23.8242°)
Node模式: Mean Node
基础盘数据源: swisseph fallback
宫制: whole sign
```

## Fallback / Warning 声明

```
本文件包含 swisseph-only fallback 基础排盘。
来自 swisseph fallback: Lagna、行星恒星黄经、D1、D9、D10、Nakshatra、Vimshottari Dasha fallback。
暂时跳过或降级: SAV/BAV、Shadbala、PyJHora校验；如对应模块恢复可用，应重新计算。
- dashaflow unavailable; using swisseph-only fallback helpers: No module named 'dashaflow'
- SAV/BAV skipped; PyJHora ashtakavarga failed: ImportError: jhora package not found
- PyJHora divisional charts skipped; using swisseph fallback D9/D10/D4/D5: ImportError: jhora package not found
- PyJHora dasha skipped; using swisseph Moon Vimshottari fallback: ModuleNotFoundError: No module named 'jhora'
- Shadbala skipped; PyJHora shadbala failed: ImportError: jhora package not found
- Optional PyJHora extras skipped: ImportError: jhora package not found
```

## 用户信息

```
性别: 女
感情状态: 未提供
```

## D1基础数据

### 行星位置
| 行星 | 星座 | 宫位 | 度数 | 逆行 |
|------|------|------|------|------|
| Lagna | Scorpio | 1 | 4°54' | — |
| Sun | Leo | 10 | 8°12' | D |
| Moon | Taurus | 7 | 9°20' | D |
| Mars | Libra | 12 | 12°57' | D |
| Mercury | Leo | 10 | 19°51' | R |
| Jupiter | Capricorn | 3 | 21°12' | R |
| Venus | Virgo | 11 | 15°10' | D |
| Saturn | Pisces | 5 | 26°04' | R |
| Rahu | Leo | 10 | 26°43' | R |
| Ketu | Aquarius | 4 | 26°43' | R |

### Chara Karakas
| 排名 | Karaka | 行星 | 有效度数 | 说明 |
|------|--------|------|---------|------|
| 1 | AK | Saturn | 26.1° | 灵魂指示星 |
| 2 | AmK | Jupiter | 21.2° | 事业指示星 |
| 3 | BK | Mercury | 19.8° | 兄弟指示星 |
| 4 | MK | Venus | 15.2° | 母亲指示星 |
| 5 | PK | Mars | 12.9° | 子女指示星 |
| 6 | GK | Moon | 9.3° | 障碍指示星 |
| 7 | DK | Sun | 8.2° | 配偶指示星 |

> KN Rao 7K体系：Sun~Saturn共7颗参与排序

### DK (配偶指示星)
```
DK = Sun（7K主用）
8K参考 DK = Rahu
```

### Nakshatra
| 行星 | Nakshatra | Pada | Nakshatra主 |
|------|-----------|------|-------------|
| Lagna | Anuradha | 1 | Saturn |
| Sun | Magha | 3 | Ketu |
| Moon | Krittika | 4 | Sun |
| Mars | Swati | 2 | Rahu |
| Mercury | Purva Phalguni | 2 | Venus |
| Jupiter | Shravana | 4 | Moon |
| Venus | Hasta | 2 | Moon |
| Saturn | Revati | 3 | Mercury |
| Rahu | Uttara Phalguni | 1 | Sun |
| Ketu | Purva Bhadrapada | 3 | Jupiter |

### 特殊点位
| 点位 | 星座 | 宫位 | 说明 |
|------|------|------|------|
| AL (Arudha Lagna) | Virgo | 11 | 外在形象/世人眼中的你 |
| UL (Upapada Lagna) | Leo | 10 | 婚姻/伴侣宫 |

## 量化数据

### Shadbala
| 行星 | Rupas | 百分比 | 排名 | 强弱 | IshtaPhala | KashtaPhala | calc基准 | 数据来源/校验 |
|------|-------|--------|------|------|-----------|-------------|----------|---------------|

> Shadbala 暂时跳过: skipped in swisseph fallback mode
> 来源: vedic-calculator引擎；PyJHora不可用时会显式标注跳过，不生成占位强度。
> 如导入同一出生时间的JHora PDF，逐行对照Shadbala；有PDF的行展示PDF值，不一致时标注“calc与PDF不一致；当前采用PDF”。
> 强: ≥150% | 中: 100-149% | 弱: <100%

### SAV (Sarvashtakavarga)

#### 原始值（按星座，用于校验）
| Ar | Ta | Ge | Cn | Le | Vi | Li | Sc | Sg | Cp | Aq | Pi | 总计 |
|----|----|----|----|----|----|----|----|----|----|----|----|------|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

> SAV/BAV 暂时跳过：当前为 swisseph fallback 基础排盘，不使用 0 值做解读。

#### 宫位映射（按宫位，供core/career/love直接使用）
> Lagna星座: Scorpio

| 1宫 | 2宫 | 3宫 | 4宫 | 5宫 | 6宫 | 7宫 | 8宫 | 9宫 | 10宫 | 11宫 | 12宫 |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### BAV (Bhinnashtakavarga)
| 行星 | Ar | Ta | Ge | Cn | Le | Vi | Li | Sc | Sg | Cp | Aq | Pi | 行和 |
|------|----|----|----|----|----|----|----|----|----|----|----|----|------|
| Sun | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Moon | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Mercury | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Jupiter | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Saturn | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### Vimsottari Dasha
| 大运 | 行星 | 起始 | 结束 | 年数 |
|------|------|------|------|------|
|  | Sun | 1991-12 | 1997-12 | 6 |
|  | Moon | 1997-12 | 2007-12 | 10 |
|  | Mars | 2007-12 | 2014-12 | 7 |
| →当前 | Rahu | 2014-12 | 2032-12 | 18 |
|  | Jupiter | 2032-12 | 2048-12 | 16 |
|  | Saturn | 2048-12 | 2067-12 | 19 |
|  | Mercury | 2067-12 | 2084-12 | 17 |
|  | Ketu | 2084-12 | 2091-12 | 7 |
|  | Venus | 2091-12 | 2111-12 | 20 |

### Sun大运 Antardasha
| 小运 | 起始 | 结束 |
|------|------|------|
| Sun-Sun | 1991-12-14 | 1992-04-02 |
| Sun-Moon | 1992-04-02 | 1992-10-01 |
| Sun-Mars | 1992-10-01 | 1993-02-06 |
| Sun-Rahu | 1993-02-06 | 1994-01-01 |
| Sun-Jupiter | 1994-01-01 | 1994-10-20 |
| Sun-Saturn | 1994-10-20 | 1995-10-02 |
| Sun-Mercury | 1995-10-02 | 1996-08-07 |
| Sun-Ketu | 1996-08-07 | 1996-12-13 |
| Sun-Venus | 1996-12-13 | 1997-12-14 |

### Moon大运 Antardasha
| 小运 | 起始 | 结束 |
|------|------|------|
| Moon-Moon | 1997-12-14 | 1998-10-14 |
| Moon-Mars | 1998-10-14 | 1999-05-15 |
| Moon-Rahu | 1999-05-15 | 2000-11-13 |
| Moon-Jupiter | 2000-11-13 | 2002-03-15 |
| Moon-Saturn | 2002-03-15 | 2003-10-14 |
| Moon-Mercury | 2003-10-14 | 2005-03-15 |
| Moon-Ketu | 2005-03-15 | 2005-10-14 |
| Moon-Venus | 2005-10-14 | 2007-06-14 |
| Moon-Sun | 2007-06-14 | 2007-12-14 |

### Mars大运 Antardasha
| 小运 | 起始 | 结束 |
|------|------|------|
| Mars-Mars | 2007-12-14 | 2008-05-11 |
| Mars-Rahu | 2008-05-11 | 2009-05-30 |
| Mars-Jupiter | 2009-05-30 | 2010-05-06 |
| Mars-Saturn | 2010-05-06 | 2011-06-14 |
| Mars-Mercury | 2011-06-14 | 2012-06-11 |
| Mars-Ketu | 2012-06-11 | 2012-11-07 |
| Mars-Venus | 2012-11-07 | 2014-01-07 |
| Mars-Sun | 2014-01-07 | 2014-05-15 |
| Mars-Moon | 2014-05-15 | 2014-12-14 |

### Rahu大运 Antardasha（当前）
| 小运 | 起始 | 结束 |
|------|------|------|
| Rahu-Rahu | 2014-12-14 | 2017-08-26 |
| Rahu-Jupiter | 2017-08-26 | 2020-01-20 |
| Rahu-Saturn | 2020-01-20 | 2022-11-26 |
| Rahu-Mercury | 2022-11-26 | 2025-06-14 |
| Rahu-Ketu | 2025-06-14 | 2026-07-02 | ← 当前
| Rahu-Venus | 2026-07-02 | 2029-07-02 |
| Rahu-Sun | 2029-07-02 | 2030-05-27 |
| Rahu-Moon | 2030-05-27 | 2031-11-26 |
| Rahu-Mars | 2031-11-26 | 2032-12-13 |

### Jupiter大运 Antardasha（下一）
| 小运 | 起始 | 结束 |
|------|------|------|
| Jupiter-Jupiter | 2032-12-13 | 2035-01-31 |
| Jupiter-Saturn | 2035-01-31 | 2037-08-14 |
| Jupiter-Mercury | 2037-08-14 | 2039-11-20 |
| Jupiter-Ketu | 2039-11-20 | 2040-10-26 |
| Jupiter-Venus | 2040-10-26 | 2043-06-27 |
| Jupiter-Sun | 2043-06-27 | 2044-04-14 |
| Jupiter-Moon | 2044-04-14 | 2045-08-14 |
| Jupiter-Mars | 2045-08-14 | 2046-07-21 |
| Jupiter-Rahu | 2046-07-21 | 2048-12-13 |

### Saturn大运 Antardasha
| 小运 | 起始 | 结束 |
|------|------|------|
| Saturn-Saturn | 2048-12-13 | 2051-12-17 |
| Saturn-Mercury | 2051-12-17 | 2054-08-26 |
| Saturn-Ketu | 2054-08-26 | 2055-10-05 |
| Saturn-Venus | 2055-10-05 | 2058-12-05 |
| Saturn-Sun | 2058-12-05 | 2059-11-17 |
| Saturn-Moon | 2059-11-17 | 2061-06-17 |
| Saturn-Mars | 2061-06-17 | 2062-07-27 |
| Saturn-Rahu | 2062-07-27 | 2065-06-02 |
| Saturn-Jupiter | 2065-06-02 | 2067-12-14 |

### Mercury大运 Antardasha
| 小运 | 起始 | 结束 |
|------|------|------|
| Mercury-Mercury | 2067-12-14 | 2070-05-12 |
| Mercury-Ketu | 2070-05-12 | 2071-05-09 |
| Mercury-Venus | 2071-05-09 | 2074-03-09 |
| Mercury-Sun | 2074-03-09 | 2075-01-13 |
| Mercury-Moon | 2075-01-13 | 2076-06-14 |
| Mercury-Mars | 2076-06-14 | 2077-06-11 |
| Mercury-Rahu | 2077-06-11 | 2079-12-29 |
| Mercury-Jupiter | 2079-12-29 | 2082-04-05 |
| Mercury-Saturn | 2082-04-05 | 2084-12-13 |

### Ketu大运 Antardasha
| 小运 | 起始 | 结束 |
|------|------|------|
| Ketu-Ketu | 2084-12-13 | 2085-05-11 |
| Ketu-Venus | 2085-05-11 | 2086-07-12 |
| Ketu-Sun | 2086-07-12 | 2086-11-16 |
| Ketu-Moon | 2086-11-16 | 2087-06-17 |
| Ketu-Mars | 2087-06-17 | 2087-11-14 |
| Ketu-Rahu | 2087-11-14 | 2088-12-01 |
| Ketu-Jupiter | 2088-12-01 | 2089-11-07 |
| Ketu-Saturn | 2089-11-07 | 2090-12-17 |
| Ketu-Mercury | 2090-12-17 | 2091-12-14 |

### Venus大运 Antardasha
| 小运 | 起始 | 结束 |
|------|------|------|
| Venus-Venus | 2091-12-14 | 2095-04-15 |
| Venus-Sun | 2095-04-15 | 2096-04-14 |
| Venus-Moon | 2096-04-14 | 2097-12-14 |
| Venus-Mars | 2097-12-14 | 2099-02-13 |
| Venus-Rahu | 2099-02-13 | 2102-02-13 |
| Venus-Jupiter | 2102-02-13 | 2104-10-14 |
| Venus-Saturn | 2104-10-14 | 2107-12-15 |
| Venus-Mercury | 2107-12-15 | 2110-10-15 |
| Venus-Ketu | 2110-10-15 | 2111-12-15 |

当前状态:
```
Mahadasha: Rahu (2014-12 ~ 2032-12)
Antardasha: Rahu-Ketu (2025-06-14 ~ 2026-07-02)
```

## 预分析（calculator计算，core直接引用）

### 行星尊贵度（Compound Dignity / Panchadha Maitri）
| 行星 | 落座 | 座主 | 复合尊贵度 | 说明 |
|------|------|------|-----------|------|
| Sun | Leo | Sun | own_sign | |
| Moon | Taurus | Venus | exalted | |
| Mars | Libra | Venus | friend | |
| Mercury | Leo | Sun | neutral | |
| Jupiter | Capricorn | Saturn | debilitated | |
| Venus | Virgo | Mercury | debilitated | |
| Saturn | Pisces | Jupiter | friend | |

### 主要相位关系
| 行星A | 行星B | 关系 | 度数差 | 影响 |
|-------|-------|------|--------|------|
| Rahu | Ketu | 对冲(180°) | 180.0° | |
| Sun | Moon | 刑(90°) | 88.87° | |
| Sun | Mars | 六合(60°) | 64.75° | |
| Jupiter | Saturn | 六合(60°) | 64.87° | |
| Moon | Venus | 三合(120°) | 125.84° | |
| Jupiter | Venus | 三合(120°) | 126.03° | |
| Mercury | Rahu | 合相 | 6.88° | |
| Mercury | Ketu | 对冲(180°) | 173.12° | |

### 宫主表
| 宫位 | 领域 | 宫主 | 宫主落宫 |
|------|------|------|---------|
| 1 | 自我 | Mars | 12 |
| 2 | 财富 | Jupiter | 3 |
| 3 | 兄弟 | Saturn | 5 |
| 4 | 家庭 | Saturn | 5 |
| 5 | 子女 | Jupiter | 3 |
| 6 | 疾病 | Mars | 12 |
| 7 | 婚姻 | Venus | 11 |
| 8 | 变故 | Mercury | 10 |
| 9 | 运势 | Moon | 7 |
| 10 | 事业 | Sun | 10 |
| 11 | 收入 | Mercury | 10 |
| 12 | 损耗 | Venus | 11 |

## 分盘数据

### 分盘可信度声明
```
D1  ✅ 可信（直接计算）
D9  ✅ 可信（直接计算）
D10 ✅ 可信（直接计算）
D4  ✅ 可信（直接计算）
D5  ✅ 可信（直接计算）
```

### D9 Navamsha
| 行星 | D9星座 | D9宫位 | Vargottama |
|------|--------|--------|-----------|
| Lagna | Leo | 1 | — |
| Sun | Gemini | 11 | 否 |
| Moon | Pisces | 8 | 否 |
| Mars | Capricorn | 6 | 否 |
| Mercury | Virgo | 2 | 否 |
| Jupiter | Cancer | 12 | 否 |
| Venus | Taurus | 10 | 否 |
| Saturn | Aquarius | 7 | 否 |
| Rahu | Sagittarius | 5 | 否 |
| Ketu | Gemini | 11 | 否 |

### D10 Dasamsha
| 行星 | D10星座 | D10宫位 |
|------|---------|---------|
| Lagna | Leo | 1 |
| Sun | Libra | 3 |
| Moon | Aries | 9 |
| Mars | Aquarius | 7 |
| Mercury | Aquarius | 7 |
| Jupiter | Aries | 9 |
| Venus | Libra | 3 |
| Saturn | Cancer | 12 |
| Rahu | Aries | 9 |
| Ketu | Libra | 3 |

### D4 Chaturthamsha
| 行星 | D4星座 | D4宫位 |
|------|--------|--------|
| Lagna | Scorpio | 1 |
| Sun | Scorpio | 1 |
| Moon | Leo | 10 |
| Mars | Capricorn | 3 |
| Mercury | Aquarius | 4 |
| Jupiter | Cancer | 9 |
| Venus | Pisces | 5 |
| Saturn | Sagittarius | 2 |
| Rahu | Taurus | 7 |
| Ketu | Scorpio | 1 |

### D5 Panchamsha
| 行星 | D5星座 | D5宫位 |
|------|--------|--------|
| Lagna | Taurus | 1 |
| Sun | Aquarius | 10 |
| Moon | Virgo | 5 |
| Mars | Sagittarius | 8 |
| Mercury | Gemini | 2 |
| Jupiter | Capricorn | 9 |
| Venus | Pisces | 11 |
| Saturn | Scorpio | 7 |
| Rahu | Libra | 6 |
| Ketu | Libra | 6 |

## 校验结果

```
 1. SAV=0          ❌
 2. BAV行常量        ❌ Sun:0≠48 Moon:0≠49 Mars:0≠39 Mercury:0≠54 Jupiter:0≠56 Venus:0≠52 Saturn:0≠39 
 3. 行星完整性(10)   ✅
 4. 度数唯一性        ✅
 5. Ra-Ke差180°      ✅
 6. 逆行标记完整      ✅
 6b. 燃烧检测        ✅ [Mercury]
 7. Ayanamsa一致     ✅ Lahiri
 7c. 盈月/亏月       亏月 (距Sun 271.1°)
 8. Nakshatra↔度数   ✅
 9. Chara Karaka排序 ✅
10. Dasha时长常数    ✅
11. D9公式交叉       ✅（直接计算，无需交叉验证）
12. Ra-Ke分盘校验    ✅（直接计算）
```

## 当前过运位置（Transit Data）

> 数据来源：vedic-calculator直接计算
> 提取时间点：2026-06-25

### 慢行星过运
| 行星 | 过运星座 | 过运宫位(从Lagna数) | 说明 |
|------|---------|-------------------|------|
| Saturn | Pisces | 5 | ~2.5年/星座 |
| Jupiter | Cancer | 9 | ~1年/星座 |
| Rahu | Aquarius | 4 | ~1.5年/星座 |
| Ketu | Leo | 10 | 自动取Rahu对冲 |

### Sade Sati初判
```
Moon本命星座: Taurus
Saturn过运星座: Pisces
相对位置: 非Sade Sati
Sade Sati状态: 未激活
```

### 双过运触发检查（Saturn-Jupiter Double Transit）
```
Saturn过运相位覆盖宫位: [2, 5, 7, 11]
Jupiter过运相位覆盖宫位: [1, 3, 5, 9]
双过运激活宫位: [5]
```