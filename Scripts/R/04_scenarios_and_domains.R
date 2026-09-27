library(readxl)
library(dplyr)

df <- read_excel("data/physician_dataset_150_model_ready.xlsx", sheet = "Cleaned_Data")

# حوزه‌های اجتماعی (Items 18, 19, 20) و سناریوها (Items 21, 22, 23)
domains_scenarios <- df %>%
  summarise(
    Family_Az_mean = mean(Survey_Item_18),
    Everyday_Az_mean = mean(Survey_Item_19),
    Academic_Az_mean = mean(Survey_Item_20),
    Scenario1_Az_share = mean(Survey_Item_21),
    Scenario2_Rating = mean(Survey_Item_22),
    Scenario3_Rating = mean(Survey_Item_23)
  )

print("Domains and Scenarios Summary (Uniform across 150):")
print(domains_scenarios)
