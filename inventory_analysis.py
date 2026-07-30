import pandas as pd
import numpy as np

print("🚀 Starting Inventory Optimization Analysis...")

# 1. Load the dataset 
try:
    df = pd.read_csv("sku_sales_data.csv")
    print("✅ Dataset loaded successfully.")
except FileNotFoundError:
    print("❌ Error: 'sku_sales_data.csv' not found. Ensure it is in the same folder.")
    exit()

# 2. ABC Classification using NumPy vectorization
# 2. ABC Classification using NumPy vectorization
conditions = [
    df['cumulative_rev_pct'] <= 0.80,
    (df['cumulative_rev_pct'] > 0.80) & (df['cumulative_rev_pct'] <= 0.95),
    df['cumulative_rev_pct'] > 0.95
]
choices = ['Class A', 'Class B', 'Class C']
df['ABC_Category'] = np.select(conditions, choices, default='Class C')
# 3. Apply Inventory Math (Assuming a standard 7-day supplier lead time)
df['Average_Daily_Sales'] = df['total_units_sold'] / 365
df['Safety_Stock'] = df['Average_Daily_Sales'] * 3  # 3 days of safety buffer
df['Reorder_Point'] = (df['Average_Daily_Sales'] * 7) + df['Safety_Stock']

# Clean up formatting numbers
df['Average_Daily_Sales'] = df['Average_Daily_Sales'].round(2)
df['Safety_Stock'] = df['Safety_Stock'].round(0).astype(int)
df['Reorder_Point'] = df['Reorder_Point'].round(0).astype(int)

# 4. Actionable Stock Check Trigger
df['Inventory_Action'] = np.where(
    df['current_stock_level'] <= df['Reorder_Point'], 
    "Trigger Reorder", 
    "Healthy Stock"
)

# 5. Export the Final Report to Excel
output_file = "Inventory_Optimization_Report.xlsx"
df.to_excel(output_file, index=False)

print(f"🎉 Analysis Complete! Report exported as '{output_file}'.")