#sumInt.R
file <- commandArgs(trailingOnly=TRUE)[[1]] 

ints <- readLines('SumInts/_test.txt', warn=FALSE)
ints <- as.numeric(ints)
print(sum(ints))
