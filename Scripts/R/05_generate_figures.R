library(readxl)
library(ggplot2)
library(tidyr)
library(dplyr)

df <- read_excel("data/physician_dataset_150_model_ready.xlsx", sheet = "Cleaned_Data")

# نمودار درصد عدم دسترسی (Items 03, 04, 07)
bottlenecks <- data.frame(
  Item = c("Cannot give complete Az explanation (Item 03)",
           "No rapid access to Az medical terms (Item 04)",
           "Not fully comfortable in Az clinical talk (Item 07)"),
  Percentage = c(
    mean(df$Survey_Item_03 == "No") * 100,
    mean(df$Survey_Item_04 == "No") * 100,
    mean(df$Survey_Item_07 == "No") * 100
  )
)

p <- ggplot(bottlenecks, aes(x = reorder(Item, Percentage), y = Percentage)) +
  geom_col(fill = "steelblue", width = 0.5) +
  coord_flip() +
  ylim(0, 100) +
  theme_minimal() +
  labs(title = "Self-Reported Register Bottlenecks among Physicians",
       x = "", y = "Physicians Reporting 'No' (%)")

ggsave("figures_register_bottlenecks.png", plot = p, width = 8, height = 4.5, dpi = 300)
message("Figure saved to figures_register_bottlenecks.png")
