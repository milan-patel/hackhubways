require(ggplot2)
theme_set(theme_bw())


HubwaySept2018 = read.csv("~/projects/hackhubways/out.csv", header=FALSE)

headings <- c("Duration", "Date", "Start Time", "Start ID", "End ID", "Type", "Birth Year", "Gender")

names(HubwaySept2018) <- headings


ggplot(aes(x = HubwaySept2018$`Start Time`, y = HubwaySept2018$`Duration`), data = HubwaySept2018) + geom_point()

