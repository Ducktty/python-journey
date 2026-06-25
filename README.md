# Python Journey: AI Stock Analyst

Welcome to my Python learning and development journey! This repository contains a collection of Python scripts focusing on integrating Artificial Intelligence with financial data analysis, charting, and automated stock reporting.

---

## 🚀 Overview

This project evolves from a simple "Hello World" AI integration into a sophisticated, multi-file stock analyst system that parses financial data, generates visual charts, and uses AI to summarize market trends.

### Key Features

* **AI Stock Analysis:** Leverage LLMs to evaluate stock market data and trends.
* **Automated Reporting:** Generate formatted stock reports automatically from CSV data.
* **Interactive Chat:** Chat-based interfaces (`chat.py` and `chat_analyst.py`) to query financial data dynamically.
* **Data Visualization:** Scripts designed to parse `stocks.csv` and output visual insights.

---

## 📂 Repository Structure

| File | Description |
| --- | --- |
| **`ai_stock_analyst_v2.py`** | The latest version of the AI stock analyst pipeline. |
| **`ai_stock_analyst.py`** | Core AI analysis logic and initial implementation. |
| **`chat_analyst.py`** & **`chat.py`** | Interactive terminal interfaces to converse with the AI analyst. |
| **`stock_report.py`** | Processes financial data to generate structured performance reports. |
| **`analyze.py`** | Scripts for baseline data parsing and evaluation. |
| **`hello_ai.py`** | A simple starter script to test AI API connectivity. |
| **`stocks.csv`** | The underlying dataset containing historical or tracked stock metrics. |

---

## 🛠️ Getting Started

### 1. Prerequisites

Make sure you have Python 3.8+ installed. You will also need an API key from your chosen AI provider (e.g., OpenAI, Anthropic, or Google Gemini) depending on your underlying implementation.

### 2. Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/Ducktty/python-journey.git
cd python-journey

```

### 3. Setup Environment Variables

Create a `.env` file in the root directory and add your API credentials:

```env
AI_API_KEY=your_api_key_here

```

---

## 📈 Usage Examples

### Run the AI Stock Analyst Pipeline

To run the primary analysis tool against the stock dataset:

```bash
python ai_stock_analyst_v2.py

```

### Start an Interactive Chat Session

To query the AI model directly about stock performance or custom prompts:

```bash
python chat_analyst.py

```

---

## ⚙️ Future Roadmap

* [ ] Add automated visualization (saving charts as PNGs).
* [ ] Integrate live web-scraping for real-time stock quotes.
* [ ] Implement a lightweight web UI (e.g., Streamlit).
