import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def generate_assets():
    # 1. Load Data
    # Ensure your CSV file is named 'Supply_Chain_Data.csv'
    try:
        df = pd.read_csv('Supply_Chain_Data.csv')
    except FileNotFoundError:
        # Fallback for demonstration if file isn't found (using snippet data)
        print("File 'Supply_Chain_Data.csv' not found. Please ensure the file is in the directory.")
        return

    # Select only the relevant numeric columns
    cols = ['Supplier_Lead_Time', 'Inventory_Levels', 'Order_Frequency', 'Delivery_Performance', 'Cost_Per_Unit']
    df = df[cols]

    # 2. Generate Correlation Matrix
    corr_matrix = df.corr()
    
    # Save correlation matrix to CSV
    corr_matrix.to_csv('correlation.csv')
    print("Generated: correlation.csv")

    # 3. Create Heatmap (Excel Style: Red-White-Green)
    # Excel default Red-White-Green hex codes
    colors = ["#F8696B", "#FFFFFF", "#63BE7B"] 
    cmap = LinearSegmentedColormap.from_list("ExcelRWG", colors)

    # Set figure size to 500x500 pixels (5 inches * 100 dpi)
    plt.figure(figsize=(5, 5), dpi=100)
    
    # Create heatmap
    # vmin and vmax set the range for the color scale (adjusting to data min/max like Excel)
    sns.heatmap(corr_matrix, 
                annot=True,           # Show numbers
                fmt='.2f',            # 2 decimal places
                cmap=cmap,            # Custom Excel-like colormap
                center=0,             # White at 0 (or remove to center on data mean)
                cbar=False,           # Hide color bar to look like a simple Excel screenshot
                square=True,          # Keep cells square
                linewidths=0.5,       # Grid lines
                linecolor='lightgray')

    plt.title("Supply Chain Correlation Matrix", pad=20)
    plt.tight_layout()

    # Save heatmap
    plt.savefig('heatmap.png', dpi=100, bbox_inches='tight')
    print("Generated: heatmap.png (Dimensions: 500x500 approx)")

if __name__ == "__main__":
    generate_assets()
