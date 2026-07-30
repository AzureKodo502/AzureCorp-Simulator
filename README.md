# 🌾 Stochastic Agricultural Simulator – B.Sc. Computer Science Thesis

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Data_Visualization-orange)
![Algorithms](https://img.shields.io/badge/Algorithms-Stochastic_Modeling-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Project Type](https://img.shields.io/badge/Project-Thesis-informational)

> **IT Italian version available here → [Leggi in Italiano](./README_IT.md)**

## 🌟 Overview

This project is a **Python-based stochastic simulator** developed as the final thesis for my Bachelor's Degree in Computer Science.

The application dynamically models the trend of economic and production KPIs over time in an agricultural context. It calculates daily variations based on real-world financial variables, applying decision-making logic conditioned by fluctuating probabilistic events.

The main goal of this project was to design a scalable calculation engine focused on complex algorithmic modeling, probabilistic data generation, and time-trend visualization.

---

## 📸 Screenshots

| **KPI Trends Analysis** | **Event Impact Visualization** |
|:---:|:---:|
| ![KPI Trends](screenshots/kpi_trends.png) | ![Event Impact](screenshots/event_impact.png) |

---

## 🚀 How to Run

To run this application, you need to execute the main Python script.

### Prerequisites
* **Python 3.11+** installed.
* **pip** package manager.

### Step 1: Setup Environment
Open a terminal in the project folder and run:
```bash
# Create a virtual environment (Recommended)
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Step 2: Install Dependencies and Run
Bash
# Install required packages
pip install -r requirements.txt

# Run the simulator
python main.py
⚙️ Core Configuration (Medium Difficulty Default Parameters)
The calculation engine runs on a strictly parameterized environment. The default fallback values configured for the "Medio" difficulty level are:

Budget: 20000.0

Meteo (Weather Index): 0.7

Tasso_Interesse_Passivo (Passive Interest Rate): 0.20

Probabilita_Evento (Adverse Event Probability): 0.04

Affitto_e_Tasse_Giornaliero (Daily Fixed Costs): 150.0

🏗️ Architecture
The application is structured into modular components to ensure scalability and separation of concerns.

Simulation Engine → Core logic for daily variations and stochastic math.

Configuration Manager → Handles parsing and validation of difficulty parameters.

Data Visualizer → Processes complex datasets to export time-trend charts using Matplotlib.

Data Exporter → Generates structured output logs for further analysis.

💻 Technologies Used
Python 3.11

Matplotlib (Data Visualization)

NumPy / Math modules (Stochastic calculations)

Git

✨ Features
🎲 Stochastic Engine
Calculates unpredictable daily variations using advanced randomization logic.

Applies probability-based adverse events affecting production metrics.

📊 Automated Data Visualization
Processes generated datasets dynamically.

Exports 5+ types of time-trend charts (KPIs, profit margins, event impacts).

💾 Data Management
Tracks historical data across simulated days.

Exports simulation results in readable formats.

🛣️ Future Improvements (Roadmap)
GUI Integration: Implement a graphical user interface using PyQt or Tkinter to replace CLI execution.

Real-Time Data Integration: Connect external weather APIs to replace static probability variables.

Advanced Export: Support for exporting datasets directly to Excel/CSV format.

🧠 What I Learned
Through this project I developed practical experience in:

Designing and implementing stochastic algorithms.

Translating complex business and mathematical rules into scalable Python code.

Generating dynamic and readable data visualizations programmatically.

Fine-tuning parameters for balanced simulation environments.

Notes
This project is strictly a Computer Science thesis, focusing on the software engineering, algorithms, and programmatic data modeling behind the simulation, rather than economic theory.

Please note that source code comments and variable names are written in Italian, to comply with the original academic requirements.

📄 License
Project created for educational purposes, academic thesis, and personal portfolio.

✍️ Author
Developed by Oleksandr
