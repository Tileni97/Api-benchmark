# Crypto Exchange API Benchmark

![API Benchmark Visualization](results/exchange_comparison_example.png)

A performance comparison tool for cryptocurrency exchange APIs, focusing on latency analysis for trading applications.

## 📌 Key Findings

| Exchange | Avg Latency | vs Kraken |
|----------|------------|-----------|
| Kraken   | 498ms      | 1.0x      |
| Binance  | 631ms      | 1.3x      |
| Gate.io  | 1888ms     | 3.8x      |

> Gate.io's API showed 3.8x higher latency than Kraken in recent tests (1888ms vs 498ms)

## 🚀 Features

- Measures end-to-end API response times
- Compares multiple exchanges simultaneously
- Generates visual reports and raw data
- Configurable test iterations and endpoints

## 🛠 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gateio-api-benchmark.git
   cd gateio-api-benchmark

2. Create and activate virtual environment:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3. Install dependencies:
   pip install -r requirements.txt

4.  Running the Benchmark
   python scripts/benchmark.py 
   
5.Example output:
Running 3 test iterations on exchange APIs...

Iteration 1/3
Gate.io   : 2008ms
Binance   : 698ms
Kraken    : 641ms

Benchmark complete! Files saved to /results

6. 📂 Output Files
-results/exchange_results_[DATE].csv - Raw latency data

-results/exchange_comparison_[DATE].png - Visual comparison chart

-results/exchange_report_[DATE].md - Analysis report

7. 📝 Customization
-Edit scripts/benchmark.py to:

-Change test iterations (TEST_ITERATIONS)

-Modify timeout settings (REQUEST_TIMEOUT)

-Add/remove exchange APIs (APIS dictionary)

8. 🤝 Contributing
1 Contributions welcome! Please:

2 Fork the repository

3 Create a feature branch

4 Submit a pull request

Created by Tileni  - For internship application to Gate.io