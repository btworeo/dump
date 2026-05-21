csv_data = read.csv("data.csv")
details = subset(csv_data, dept == "IT" & salary > 600)
print(details)
