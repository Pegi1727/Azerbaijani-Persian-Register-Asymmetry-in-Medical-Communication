library(readxl)
library(dplyr)

df <- read_excel("data/physician_dataset_150_model_ready.xlsx", sheet = "Cleaned_Data")

# اقلام متغیر (Items 03, 04, 07, 09, 25, 26)
calc_prop <- function(var) {
  df %>% count({{ var }}) %>% mutate(pct = round(n / sum(n) * 100, 2))
}

message("Item 03 (Complete explanation in Az):")
print(calc_prop(Survey_Item_03))

message("Item 04 (Rapid access to Az terms):")
print(calc_prop(Survey_Item_04))

message("Item 07 (Comfort in Az clinical discourse):")
print(calc_prop(Survey_Item_07))

message("Item 09 (Cognitive effort/unfamiliarity):")
print(calc_prop(Survey_Item_09))

message("Item 25 (Attribution for Persian):")
print(calc_prop(Survey_Item_25))

message("Item 26 (Expressive precision preference):")
print(calc_prop(Survey_Item_26))
