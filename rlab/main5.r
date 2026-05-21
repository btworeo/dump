?plot
?chickwts

data(chickwts)
plot(chickwts$feed)

feeds = table(chickwts$feed)

barplot(feeds[order(feeds, decreasing = TRUE)])
