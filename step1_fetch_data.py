# -*- coding: utf-8 -*-
"""
第一步：验证环境 + 获取美股与大盘数据

运行前请先执行: pip install -r requirements.txt
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# 1. 先定好「你的股票」和「大盘」的代码（美股用 ticker symbol）
MY_STOCK = "AAPL"   # 示例：苹果，你可以改成 NVDA、TSLA 等
MARKET = "SPY"      # 大盘：标普500 ETF，美股最常用

# 2. 拉取最近 5 个交易日的数据（先少一点，确认能跑通）
end = datetime.now()
start = end - timedelta(days=14)  # 多取几天，因为周末没交易

print("正在拉取数据（首次可能稍慢）...")
my_ticker = yf.Ticker(MY_STOCK)
market_ticker = yf.Ticker(MARKET)

my_hist = my_ticker.history(start=start, end=end)
market_hist = market_ticker.history(start=start, end=end)

# 3. 简单看一下
print("\n--- 你的股票 {} 最近几天 ---".format(MY_STOCK))
print(my_hist[["Open", "Close", "High", "Low"]].tail())

print("\n--- 大盘 {} 最近几天 ---".format(MARKET))
print(market_hist[["Open", "Close", "High", "Low"]].tail())

print("\n第一步完成：已经能拿到美股和大盘数据。")
print("下一步可以：算涨跌幅、画图、和 SPY 对比。")
