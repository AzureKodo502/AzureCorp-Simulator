# 🌾 Agricultural Stochastic Simulator – Computer Science Thesis

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Data_Visualization-orange)
![NumPy](https://img.shields.io/badge/NumPy-Math-lightblue)
![Algorithms](https://img.shields.io/badge/Algorithms-Stochastic_Modeling-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Project Type](https://img.shields.io/badge/Project-Thesis-informational)

> **IT Versione italiana disponibile qui → [Leggi in Italiano](./README.md)**

## 🌟 Overview

This project is a **stochastic simulator developed in Python**, created as a final thesis for a Bachelor's degree in Computer Science.

The application dynamically models the trends of economic and production key performance indicators (KPIs) over time within an agricultural context. The system calculates daily variations based on real financial variables, applying decision-making logic driven by the probabilistic generation of unforeseen events.

The project's primary objective is the design of a scalable computational engine focused on complex algorithmic modeling, object-oriented programming (OOP), and advanced data visualization.

---

## 📸 Screenshot

| **Financial Trend Analysis (Matplotlib)** | **Impact of Adverse Events (Console/Log)** |
|:---:|:---:|
| ![KPI Trends](screenshots/kpi_trends.png) | ![Event Impact](screenshots/event_impact.png) |

---

## How to start the project

To run this application, simply launch the main Python file.

### Prerequisites
* **Python 3.11+** installed.
* Package manager **pip**.

### Step 1: Environment Configuration
Open a terminal in the project folder and run:
```bash
# Creating a virtual environment (Recommended)
python -m venv venv

# Activating the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
Step 2: Installing dependencies and execution
Bash
# Installation of the necessary libraries (Matplotlib, NumPy, ecc.)
pip install -r requirements.txt

# Starting the simulator
python main.py
The calculation engine operates in an environment strictly parameterized via the config.py module.
```
### Initial Parameters (Default: Medium difficulty)

- Initial Budget: €20,000.00

- Weather Index (Stability): 0.7 (0.0 stable, 1.0 chaotic)

- Interest Rate Payable: 0.20 (20%)

- Adverse Event Probability: 0.04 (4%)

- Fixed Costs (Rent and Daily Taxes): €150.00

- Note: The simulation supports the input of a specific SEED to ensure the complete reproducibility of the generated scenarios.

---  

### Software Architecture
- The code strictly applies the principle of separation of responsibilities (Separation of Concerns), separating configuration, domain logic, and the execution engine.

### config.py (Configuration Manager)
- It isolates all global parameters, allowing the model to be balanced without altering the code logic.

### classi.py (Domain Logic & OOP)
- Implement an object-oriented architecture. Use a `ProductionUnit` superclass from which specific modules (WheatField, Stable, Vineyard) inherit, leveraging polymorphism to calculate daily balances.

### main.py (Simulation Engine)
- The system's algorithmic core. It manages the time cycle, applies statistical distributions (Gaussian and Uniform) to model market behavior, and orchestrates data export.

---

### Technologies Used

- Language: Python 3.11

- Data Visualization: Matplotlib

- Stochastic Mathematics: NumPy, native random module

- Data Management: native CSV module for exporting structured datasets

---

### Key Features
- Stochastic Engine and Risk Analysis
Calculation of market variations using advanced randomization algorithms (Gaussian and uniform distributions).

- A system for injecting unforeseen, asymmetrically impactful events (e.g., drought, war, pandemic, export boom) that dynamically alter price and production multipliers.

- Dynamic Data Generation and Visualization

- Real-time monitoring of cash flow, debt, and sectoral profits.

- Automated export of results to a .csv file (report_dati_AzureCorp.csv) for external analysis.

- Rendering of multi-plot graphical dashboards using Matplotlib (Financial Health, Market Scenario, Sector Performance).

---

### Financial Logic Enterprise
- Automated management of daily debit interest in the event of a negative balance.

- Early-exit system for irreversible bankruptcy based on preset deficit thresholds.

---

### Skills Acquired
- Through the development of this thesis, I have gained practical experience in:

- Design and implementation of stochastic algorithms and probability distributions.

- Object-Oriented (OOP) software architecture applied to complex simulation models.

- Processing, tracking, and exporting programmatic datasets for Business Intelligence.

---

### Note
- This project is a Computer Science thesis. Its primary focus lies in software engineering, algorithmic robustness, and data manipulation, rather than microeconomic logic.

- Source code comments, variable names, and console output are kept in Italian to comply with the original academic requirements set by the faculty.

---

### License
Project created for educational purposes, as an academic thesis, and for a personal portfolio.

### Author
Developed by Oleksandr Bevtsyk

