data = c(5, 8, 12, 20, 7)
mean_value = mean(data)
print(paste("Mean value is : ", mean_value))
plot(
  data,
  type = "o",
  col = "blue",
  xlab = "Index",
  ylab = "Value",
  main = "Line Plot of Data"
)
