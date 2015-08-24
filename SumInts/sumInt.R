file <- commandArgs(trailingOnly=TRUE)[[1]]

ints <- readLines(file)
ints <- as.numeric(ints)

cat(sum(ints, na.rm=TRUE))
