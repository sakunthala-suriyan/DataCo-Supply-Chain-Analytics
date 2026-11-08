import pandas as pd

df = pd.read_csv('01_Raw_Data/DataCoSupplyChainDataset.csv', encoding='latin-1')
desc = pd.read_csv('01_Raw_Data/DescriptionDataCoSupplyChain.csv')

print("=== MAIN DATASET ===")
print(f"Shape: {df.shape}")
print(f"\nColumn Names:\n{df.columns.tolist()}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
print(f"\nDuplicates: {df.duplicated().sum()}")
print(f"\nFirst 5 Rows:\n{df.head()}")

print("\n=== DATA DICTIONARY ===")
print(desc.head(20))