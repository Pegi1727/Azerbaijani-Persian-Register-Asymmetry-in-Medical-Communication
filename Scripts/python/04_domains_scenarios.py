import pandas as pd

df = pd.read_excel("data/physician_dataset_150_model_ready.xlsx", sheet_name="Cleaned_Data")

print("=== Domain Proportions (Azerbaijani Share) ===")
print(f"Domestic/Family (Item 18): {df['Survey_Item_18'].iloc[0] * 100:.0f}%")
print(f"Informal Social (Item 19): {df['Survey_Item_19'].iloc[0] * 100:.0f}%")
print(f"Formal Academic (Item 20): {df['Survey_Item_20'].iloc[0] * 100:.0f}%")

print("\n=== Stepped Clinical Vignettes ===")
print(f"Scenario 1 (Colloquial Az patient - Item 21): {df['Survey_Item_21'].iloc[0] * 100:.0f}% Azerbaijani")
print(f"Scenario 2 (Educated formal patient - Item 22): Score {df['Survey_Item_22'].iloc[0]} / 5 (Hybrid stance)")
print(f"Scenario 3 (Elevated technical Az patient - Item 23): Score {df['Survey_Item_23'].iloc[0]} / 5 (Near-ceiling Persian)")
print(f"Scenario 3 Attribution (Item 24): {df['Survey_Item_24'].iloc[0]}")
