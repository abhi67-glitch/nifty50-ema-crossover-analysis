# 20/50 EMA Crossover Strategy Backtest - RELIANCE

## 1. Overview
This repository contains a 12-month backtest analysis of the 20/50 Exponential Moving Average (EMA) Crossover trading strategy applied to **RELIANCE (Daily Timeframe)** on the National Stock Exchange (NSE).

---

## 2. Strategy Rules
* **Entry Signal:** Buy when the 20-day EMA crosses above the 50-day EMA.
* **Exit Signal:** Sell when the 20-day EMA crosses back below the 50-day EMA.
* **Trade Definition:** One round trip from entry crossover to exit crossover.

---

## 3. Performance Summary Table

| Metric | Result |
| :--- | :--- |
| **Instrument** | RELIANCE (NSE) |
| **Total Trades** | 5 |
| **Winning Trades** | 2 |
| **Win Rate** | **40.0%** |
| **Largest Single Winner** | **+9.07%** (Trade #4) |
| **Largest Single Loser** | **-3.56%** (Trade #1) |

---

## 4. Repository Structure
* `trade_log.csv`: Complete trade log detailing entry/exit dates, execution prices, and P&L percentages.
* `ema_crossover.py`: Python script used to fetch historical price data and execute crossover logic.
* `screenshots/`:
  * `01_full_12month_chart.png`: 12-month daily chart with 20 & 50 EMA indicators.
  * `02_best_trade_zoomed.png`: Zoomed-in view of Trade #4 (+9.07% gain).
  * `03_worst_trade_zoomed.png`: Zoomed-in view of Trade #1 (-3.56% loss).

---

## 5. Strategy Verdict

**RELIANCE | 5 Trades | 40.0% Win Rate | NO (Would Not Trade)**

I would not trade this strategy with my own money in its pure form. While the 20/50 EMA crossover effectively captures strong, prolonged bull trends—as seen in Trade #4 where it locked in a +9.07% gain—it is severely hampered by lag and sideways choppy markets. Moving averages are lagging indicators by nature; by the time the 20 EMA crosses above the 50 EMA, a significant portion of the initial price move has already occurred. In consolidation phases, the strategy suffers from repeated false breakouts ("whip-saws"), cutting into profits through small, compounding losses and transaction costs.

The strategy works best in strong, sustained trending markets where price momentum carries far beyond the crossover point. Conversely, it consistently fails in range-bound or high-volatility sideways markets where prices oscillate around the moving averages. To make this strategy viable for real capital, it would require additional filters—such as a volume confirmation, a trend-strength filter (like ADX > 20), or a trailing stop-loss to protect open profits before the lagging exit signal triggers.
