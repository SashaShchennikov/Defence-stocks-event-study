import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


start = "2021-01-01"
end = "2026-01-01"

tickers = ["RHM.DE", "ba.l", "ho.pa", "ldo.mi", "^gdaxi"]

events = {"invasion":"2022-04-24",
          "zeitenwende":"2022-02-28",
          "kupiansk":"2022-09-12",
          "rearm_europe": "2025-03-04",
          "spiderweb": "2025-06-02",
          "nato_5_percent": "2025-06-25",
          "alaska_summit": "2025-08-18"}

data = yf.download(tickers, start = start, end = end)
print(data.head())

returns = data["Close"].pct_change()
abnormal = returns.sub(returns["^GDAXI"], axis = 0)
print(abnormal.head())

results = {}

for name, date in events.items():
    window = abnormal.loc[date:].head(3)
    reaction = window.sum()
    results[name] = reaction

table = pd.DataFrame(results).T
print(table.round(3))

vollatility = returns.std()
print(vollatility)

growth = (1+returns).cumprod()
growth.plot()
plt.show()