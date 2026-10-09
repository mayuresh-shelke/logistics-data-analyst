# Logistics Data Analyst Internship — Portfolio

**Candidate:** Mayuresh  
**Role:** Logistics Data Analyst Intern  
**Program:** Yuva Intern  
**Core Domain:** Supply Chain Optimization, Last-Mile Delivery Analytics, Predictive Modeling  
**Tech Stack:** Python (Pandas, NumPy, Scikit-Learn, SciPy), Git, Optimization Heuristics  

---

## 📌 Repository Overview
This repository houses the end-to-end analytical deliverables, source code, and strategic reports developed across the 4-week internship program.

| Week | Milestone / Task Scope | Status | Deliverables |
| :---: | :--- | :---: | :--- |
| **Week 1** | **Strategic Planning & Data Exploration** | ✅ Completed | [Week-1 Folder](./Week-1-Strategic-Planning/) |
| **Week 2** | **Data Cleaning & Advanced Exploratory Data Analysis** | ⏳ In Progress | [Week-2 Folder](./Week-2-Data-Exploration-Cleaning/) |
| **Week 3** | **Predictive Delay & ETA Machine Learning Modeling** | 📅 Upcoming | [Week-3 Folder](./Week-3-Predictive-Modeling/) |
| **Week 4** | **Route Optimization, Dashboards & Final Synthesis** | 📅 Upcoming | [Week-4 Folder](./Week-4-Final-Deployment/) |

---

## 📁 Week 1: Strategic Planning & Data Exploration

### 1. Problem Scenario
Optimizing urban last-mile delivery operations for a high-throughput distribution hub handling 8,000+ daily orders. The objective is to mitigate delivery delays caused by traffic congestion, weather variability, and inefficient stop sequencing.

### 2. Targeted KPIs
* **On-Time In-Full Rate (OTIF %):** Target $\ge 93.5\%$ (Baseline: $81.4\%$)
* **Fleet Distance & Fuel Reduction:** Target $12\% - 15\%$ decrease via route reordering
* **Driver Dwell Time per Stop:** Target $< 5.5$ minutes (Down from $9.2$ minutes)

### 3. Strategic Methodology
* **Unsupervised Clustering:** Micro-zone customer grouping using K-Means.
* **Supervised Regression:** Random Forest / XGBoost models predicting delivery transit times (ETA).
* **Combinatorial Optimization:** Formulating stop sequences using Traveling Salesperson Problem (TSP) constraints.

### 4. Week 1 Contents
* [📄 Strategy Report (.docx)](./Week-1-Strategic-Planning/Mayuresh_Week1_Report.docx)
* [🐍 Python Strategy & Simulation Code](./Week-1-Strategic-Planning/logistics_strategy_pipeline.py)
* [📊 Strategic Roadmap Visual](./Week-1-Strategic-Planning/strategic_roadmap.png)

---

## 🛠️ Setup & Execution

```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)<your-username>/logistics-data-analyst-internship.git

# Navigate to project directory
cd logistics-data-analyst-internship

# Run Week 1 script
python Week-1-Strategic-Planning/logistics_strategy_pipeline.py
