# AI-Powered Production Log Analyzer and Incident Assistant

## Project Overview

A Python-based DevOps project that analyzes application logs, identifies errors and critical events, counts log severity levels, and generates a report to help engineers investigate production incidents.

The project is designed to evolve into an AI-powered incident assistant with Docker, CI/CD, AWS, Kubernetes, Prometheus, and Grafana integrations.

## Current Features

- Reads application logs from a file.
- Identifies INFO, WARNING, ERROR, and CRITICAL messages.
- Counts messages by severity level.
- Extracts errors requiring investigation.
- Generates a text-based analysis report.
- Uses Git and GitHub for source control.

## Technology Stack

- Python
- PowerShell / Windows
- Git
- GitHub

## Project Structure

```text
AI-Production-Log-Analyzer/
├── analyzer.py
├── logs/
│   └── application.log
├── reports/
│   └── analysis_report.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3 installed
- Git installed
- PowerShell or a compatible terminal

## How to Run

Clone the repository:

```bash
git clone https://github.com/shaikoushi/ai-production-log-analyzer.git
```

Navigate to the project directory:

```bash
cd ai-production-log-analyzer
```

Run the analyzer:

```bash
python analyzer.py
```

View the generated report in `reports/analysis_report.txt`.

## Sample Output

```text
=== Production Log Analysis ===
Total log lines: 7
INFO: 3
WARNING: 1
ERROR: 2
CRITICAL: 1
```

## Planned Enhancements

- Automated testing with Python
- Docker containerization
- CI/CD using GitHub Actions or Jenkins
- AWS and Kubernetes deployment
- Prometheus and Grafana monitoring
- AI-assisted incident analysis and troubleshooting recommendations

## Author

Chandini Shaik

GitHub: https://github.com/shaikoushi
