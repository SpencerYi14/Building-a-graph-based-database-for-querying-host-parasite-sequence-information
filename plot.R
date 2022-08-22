library(ggplot2)
setwd('/Users/bodomting119/Desktop')
bc <- read.table('bc.txt', header = TRUE, sep = "", dec = ".")
ggplot(data=bc, aes(x=Entity, y=Time, fill=Database)) +
  geom_bar(stat="identity", position=position_dodge()) +
  scale_fill_brewer(palette="Reds") +
  ylab("Time (ms)") +
  coord_flip() +
  geom_text(aes(label=Time), position=position_dodge(width=1), vjust=0.5) +
  labs(title="Query performance comparison") +
  theme(plot.title = element_text(hjust = 0.5))

