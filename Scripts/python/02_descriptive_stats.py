import pandas as pd

df = pd.read_excel("data/physician_dataset_150_model_ready.xlsx", sheet_name="Cleaned_Data")

variables = ["Gender", "Specialty", "Age_Group", "Experience_Category"]
for var in variables:
    counts = df[var].value_counts()
    percentages = (df[var].value_counts(normalize=True) * 100).round(1)
    summary = pd.DataFrame({"Count": counts, "Percentage (%)": percentages})
    print(f"\n--- {var} ---")
    print(summary)
