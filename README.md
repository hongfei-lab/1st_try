# 美股涨跌幅爬虫与可视化

从零开始：爬取美股数据、计算涨跌幅、可视化并与大盘（如 S&P 500）对比。

## 第一步：搭建环境（你现在在这里）

1. **确认已安装 Python**  
   在终端运行：
   ```bash
   python --version
   ```
   建议 Python 3.8 或以上。

2. **安装依赖**
   ```bash
   cd c:\Users\WuHongFei\Desktop\git_newtry
   pip install -r requirements.txt
   ```

3. **验证能否获取数据**  
   运行：
   ```bash
   python step1_fetch_data.py
   ```
   若能看到一只股票和大盘的最近几天数据，说明第一步完成。

## 后续步骤（规划）

- **第二步**：计算你关心的股票的日涨跌幅、周涨跌幅。
- **第三步**：用 matplotlib/seaborn 画折线图、柱状图。
- **第四步**：同一张图里画「你的股票」和「大盘」，做对比。

## 数据说明

- 使用 **yfinance** 从 Yahoo Finance 拉取美股数据，无需注册、无需 API Key。
- 「大盘」常用：**SPY**（标普500 ETF）或 **^GSPC**（标普500指数）。
