library(readxl)
library(dplyr)

df <- read_excel("data/physician_dataset_150_model_ready.xlsx", sheet = "Cleaned_Data")

# توزیع جنسیت، سن، سابقه و تخصص
demo_summary <- list(
  gender = table(df$Gender),
  age_group = table(df$Age_Group),
  experience = table(df$Experience_Category),
  specialty = table(df$Specialty)
)

print("Demographic Summary:")
print(demo_summary)
