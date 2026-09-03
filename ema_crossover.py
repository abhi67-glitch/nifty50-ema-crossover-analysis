import pandas as pd
import numpy as np

def run_ema_crossover_strategy(df):
    df['EMA20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['EMA50'] = df['Close'].ewm(span=50, adjust=False).mean()

    df['Signal'] = np.where(df['EMA20'] > df['EMA50'], 1, -1)
    df['Crossover'] = df['Signal'].diff()

    trades = []
    in_trade = False
    entry_date, entry_price = None, 0.0

    for date, row in df.iterrows():
        if row['Crossover'] == 2 and not in_trade:
            in_trade = True
            entry_date = date.strftime('%Y-%m-%d')
            entry_price = float(row['Close'])
        elif row['Crossover'] == -2 and in_trade:
            in_trade = False
            exit_date = date.strftime('%Y-%m-%d')
            exit_price = float(row['Close'])
            pnl = ((exit_price - entry_price) / entry_price) * 100
            trades.append({
                'Trade #': len(trades) + 1,
                'Entry Date': entry_date,
                'Entry Price': round(entry_price, 2),
                'Exit Date': exit_date,
                'Exit Price': round(exit_price, 2),
                'P&L (%)': round(pnl, 2)
            })

    return pd.DataFrame(trades)
