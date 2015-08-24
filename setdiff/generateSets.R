generateSetString <- function() {
    set1 <- sample(1:20, 10, replace=FALSE)
    set2 <- sample(1:20, 10, replace=FALSE)
    
    string <- paste(
        paste(set1, collapse=','),
        ';',
        paste(set2, collapse=','),
        sep='')
    return(string)
}

strings <- replicate(100, generateSetString())
cat(paste(strings, collapse='\n'), file='setdiff/_test.txt')

