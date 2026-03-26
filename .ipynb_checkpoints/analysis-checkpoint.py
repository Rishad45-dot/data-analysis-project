# %% [markdown]
# # Warehouse Data Analysis
# Loading and cleaning warehouse dataset

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your Excel files
df = pd.read_excel('warehouse_messy_data.xlsx')
print(df.head())

# %%
# Check for missing values
print(df.isnull().sum())

# %%
# Handle quantity NaN values
df['quantity'] = df['quantity'].fillna(0)  # Example