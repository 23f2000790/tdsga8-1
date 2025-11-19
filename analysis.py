import marimo

__generated_with = "0.1.63"
app = marimo.App(width="medium")

@app.cell
def __():
    import marimo as mo
    import math

    # Data Scientist: 23f2000790@ds.study.iitm.ac.in
    # This notebook demonstrates a reactive data flow.
    return math, mo

@app.cell
def __(mo):
    # Cell 1: Create the interactive widget
    # This slider controls the input variable 'x' for our analysis.
    input_slider = mo.ui.slider(start=1, end=100, step=1, label="Input Value (x)")
    
    mo.md(f"### Control Panel\nAdjust the input variable: {input_slider}")
    return input_slider,

@app.cell
def __(input_slider):
    # Cell 2: Variable Dependency
    # This cell depends on 'input_slider' from the previous cell.
    # Every time the slider moves, this code re-runs automatically.
    
    x = input_slider.value
    
    # Calculate a non-linear relationship (e.g., Logarithmic growth)
    # We add 1 to avoid log(0) if x starts at 0, though our slider starts at 1.
    y = 10 * (x ** 0.5) 
    
    return x, y

@app.cell
def __(mo, x, y):
    # Cell 3: Dynamic Markdown Output
    # This cell depends on variables 'x' and 'y' calculated above.
    # It renders a markdown block that updates in real-time.
    
    md_output = mo.md(
        f"""
        ## Data Analysis Report
        
        We are analyzing the relationship $y = 10\\sqrt{{x}}$.
        
        - **Current Input ($x$):** {x}
        - **Calculated Output ($y$):** {y:.2f}
        
        ___
        *As you move the slider above, these values update instantly due to Marimo's reactive execution graph.*
        """
    )
    return md_output,

if __name__ == "__main__":
    app.run()
