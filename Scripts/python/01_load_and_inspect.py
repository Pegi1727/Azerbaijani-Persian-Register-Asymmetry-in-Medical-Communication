import pandas as pd

FILE_PATH = "data/physician_dataset_150_model_ready.xlsx"

excel_obj = pd.ExcelFile(FILE_PATH)
print("Available sheets:", excel_obj.sheet_names)

df = pd.read_excel(FILE_PATH, sheet_name="Cleaned_Data")
print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")

assert df.shape == (150, 33), "Unexpected dimensions!"
assert df["Physician_ID"].nunique() == 150, "Duplicate IDs found!"
assert df.isna().sum().sum() == 0, "Missing values found!"
print("Validation successful: 150 complete records.")
