# Python Journey: AI Stock Analyst | Python 学习之旅：AI 股票分析师

Welcome to my Python learning and development journey! This repository contains a collection of Python scripts focusing on integrating Artificial Intelligence with financial data analysis, charting, and automated stock reporting.

欢迎来到 my Python 学习与开发之旅！本仓库包含一系列 Python 脚本，专注于将人工智能与金融数据分析、图表生成及自动化股票报告相结合。

---

## 🚀 Overview / 项目概述

**[EN]** This project evolves from a simple "Hello World" AI integration into a sophisticated, multi-file stock analyst system that parses financial data, generates visual charts, and uses AI to summarize market trends.

**[ZH]** 本项目从简单的 "Hello World" AI 对接开始，逐步演变为一个完善的、多文件的股票分析师系统。它能够解析金融数据、生成可视化图表，并利用 AI 总结市场趋势。

### Key Features / 核心功能

* **AI Stock Analysis / AI 股票分析:** Leverage LLMs to evaluate stock market data and trends. / 结合大语言模型（LLM）评估股市数据和趋势。
* **Automated Reporting / 自动化报告:** Generate formatted stock reports automatically from CSV data. / 自动从 CSV 数据生成格式化的股票报告。
* **Interactive Chat / 互动对话:** Chat-based interfaces (`chat.py` and `chat_analyst.py`) to query financial data dynamically. / 通过命令行聊天界面动态查询金融数据。
* **Data Visualization / 数据可视化:** Scripts designed to parse `stocks.csv` and output visual insights. / 解析 `stocks.csv` 并输出直观的可视化图表。

---

## 📂 Repository Structure / 仓库结构

| File / 文件 | Description (EN) | 功能简介 (ZH) |
| --- | --- | --- |
| **`ai_stock_analyst_v2.py`** | The latest version of the AI stock analyst pipeline. | AI 股票分析师流水线的最新版本。 |
| **`ai_stock_analyst.py`** | Core AI analysis logic and initial implementation. | 核心 AI 分析逻辑及初始实现。 |
| **`chat_analyst.py`** | Interactive terminal interface to converse with the AI analyst. | 与 AI 分析师对话的交互式终端界面。 |
| **`chat.py`** | Standard interactive terminal chat interface. | 标准的交互式终端聊天界面。 |
| **`stock_report.py`** | Processes financial data to generate structured performance reports. | 处理金融数据并生成结构化的业绩报告。 |
| **`analyze.py`** | Scripts for baseline data parsing and evaluation. | 用于基础数据解析和评估的脚本。 |
| **`hello_ai.py`** | A simple starter script to test AI API connectivity. | 用于测试 AI API 连接的简单入门脚本。 |
| **`stocks.csv`** | The underlying dataset containing historical or tracked stock metrics. | 包含历史或追踪股票指标的基础数据集。 |

---

## 🛠️ Getting Started / 快速入门

### 1. Prerequisites / 环境准备

Make sure you have **Python 3.8+** installed. You will also need an API key from your chosen AI provider (e.g., OpenAI, Anthropic, or Google Gemini).

请确保已安装 **Python 3.8+**。您还需要准备所选 AI 服务商（如 OpenAI、Anthropic 或 Google Gemini）的 API 密钥。

### 2. Installation / 安装

Clone the repository and navigate into the project directory: / 克隆仓库并进入项目目录：

```bash
git clone https://github.com/Ducktty/python-journey.git
cd python-journey

```

### 3. Setup Environment Variables / 配置环境变量

Create a `.env` file in the root directory and add your API credentials: / 在根目录下创建一个 `.env` 文件并添加您的 API 凭证：

```env
AI_API_KEY=your_api_key_here

```

---

## 📈 Usage Examples / 使用示例

### Run the AI Stock Analyst Pipeline / 运行 AI 股票分析流水线

To run the primary analysis tool against the stock dataset: / 运行针对股票数据集的核心分析工具：

```bash
python ai_stock_analyst_v2.py

```

### Start an Interactive Chat Session / 开启交互式对话

To query the AI model directly about stock performance or custom prompts: / 直接向 AI 模型提问关于股票表现或自定义提示词：

```bash
python chat_analyst.py

```

---

## ⚙️ Future Roadmap / 后续规划

* [ ] Add automated visualization (saving charts as PNGs). / 添加自动化可视化功能（将图表保存为 PNG）。
* [ ] Integrate live web-scraping for real-time stock quotes. / 集成实时网页抓取以获取即时股票行情。
* [ ] Implement a lightweight web UI (e.g., Streamlit). / 实现轻量级 Web 界面（例如 Streamlit）。
