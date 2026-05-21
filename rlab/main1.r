csv_data <- read.csv("data.csv")
details <- subset(csv_data, dept == "IT")
print(details)
