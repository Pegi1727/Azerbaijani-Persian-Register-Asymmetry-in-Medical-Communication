library(readxl)
library(dplyr)

file_path <- "data/physician_dataset_150_model_ready.xlsx"

# بررسی شیت‌ها
sheets <- excel_sheets(file_path)
message("Sheets found: ", paste(sheets, collapse = ", "))

# بارگذاری شیت اصلی
df <- read_excel(file_path, sheet = "Cleaned_Data")

# کنترل‌های اولیه تضمین کیفیت
stopifnot(nrow(df) == 150)
stopifnot(ncol(df) == 33)
stopifnot(n_distinct(df$Physician_ID) == 150)
stopifnot(sum(is.na(df)) == 0)

message("QA passed: 150 unique records, 0 missing values.")
