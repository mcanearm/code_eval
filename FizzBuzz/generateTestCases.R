# Quick test file script
val1 <- sample(1:20, 20)
val2 <- sample(1:20, 20)
val3 <- sample(21:100, 20)

testLines <- cbind.data.frame(val1, val2, val3)
write.table(testLines, file='./FizzBuzz/test_cases.txt', row.names=FALSE, col.names=FALSE)

