# 📦 Inventory Optimization & Demand Analytics System

An end-to-end data analytics pipeline designed to eliminate capital inefficiencies and prevent retail stockouts through mathematical inventory modeling.

## 🛠️ Tech Stack & Skills
* **Database Querying:** SQL (CTEs, Window Functions, Joins)[cite: 1]
* **Data Processing:** Python (Pandas, NumPy)[cite: 1]
* **Operational Reporting:** MS Excel (Pivot Tables, Conditional Formatting)[cite: 1]
* **Domain Focus:** Supply Chain & Inventory Management[cite: 1]

## 💡 Business Problem
Retail companies face dual financial threats: running out of high-demand stock (lost sales) while locking up capital in excessive deadstock[cite: 1]. This project provides automated replenishment logic to balance stock levels dynamically[cite: 1].

## ⚙️ How It Works
1. **SQL Layer (`extract_inventory_data.sql`):** Extracts transactional sales and running revenue totals using window functions[cite: 1].
2. **Python Analytics (`inventory_analysis.py`):** 
   - Executes an **ABC Inventory Classification** (Pareto 80/15/5 Rule) using vectorized NumPy operations[cite: 1].
   - Computes deterministic **Safety Stock** and dynamic **Reorder Points (ROP)**.
3. **Excel Output (`Inventory_Optimization_Report.xlsx`):** Generates conditional `Trigger Reorder` vs `Healthy Stock` alerts for warehouse managers[cite: 1].

## 📊 Core Business Logic
* **Average Daily Sales:** `Total Units Sold / 365`
* **Safety Stock:** `Average Daily Sales × 3 Days`
* **Reorder Point (ROP):** `(Average Daily Sales × 7 Day Lead Time) + Safety Stock`
