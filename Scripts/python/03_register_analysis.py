import pandas as pd

df = pd.read_excel("data/physician_dataset_150_model_ready.xlsx", sheet_name="Cleaned_Data")

varying_items = {
    "Survey_Item_03": "Complete explanation without Persian",
    "Survey_Item_04": "Rapid access to Az terms",
    "Survey_Item_07": "Comfort in pure Az clinical discourse",
    "Survey_Item_09": "Cognitive effort/unfamiliarity",
    "Survey_Item_25": "Primary driver of Persian usage",
    "Survey_Item_26": "Perceived expressive precision"
}

for col, description in varying_items.items():
    dist = df[col].value_counts(normalize=True) * 100
    print(f"\n[{col}] {description}:")
    for val, pct in dist.items():
        print(f"  - {val}: {pct:.1f}% (n={df[col].value_counts()[val]})")
