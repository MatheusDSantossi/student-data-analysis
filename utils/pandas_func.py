import pandas as pd
import matplotlib.pyplot as plt

def set_columns(columns, df: pd.DataFrame):
    
    df.columns = columns
    
    return df
 
def create_top_cities_chart(df: pd.DataFrame, top_n = 20):
    """Show top N cities and group the rest as 'Others'"""
    
    # Get top N cities
    top_cities = df.nlargest(top_n)
    
    # Calculate 'Others' category
    others_sum = df.iloc[top_n:].sum()
    
    # Create new series with 'Others'
    if others_sum > 0:
        top_cities_with_others = pd.concat([
            top_cities,
            pd.Series([others_sum], index=["Others"])
        ])
        
    else:
        top_cities_with_others = top_cities
        
    # Create horizontal bar chart (better for many labels)
    plt.figure(figsize=(12, 8))
    bars = plt.barh(range(len(top_cities_with_others)), top_cities_with_others.values)
    
    # Coloring the "Others" bar differently
    if others_sum > 0:
        bars[-1].set_color('lightgray')
        
    plt.yticks(range(len(top_cities_with_others)), top_cities_with_others.index)

    plt.xlabel("Number of Stundents")
    plt.title(f"Top {top_n} Cities by Student Count")
    plt.gca().invert_yaxis() # Highest at top
    
    # Add value label on bars
    for i, v in enumerate(top_cities_with_others.values):
        plt.text(v + max(top_cities_with_others.values) * 0.01, i, f'{v:,}', va="center")
        
    plt.tight_layout()
    plt.show()
