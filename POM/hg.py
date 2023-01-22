def numOfIncSubseqOfSizeK(arr, n, k):
    dp = [[0 for i in range(n)]
          for i in range(k)]
    for i in range(n):
        dp[0][i] = 1
    for l in range(1, k):
        for i in range(l, n):
            dp[l][i] = 0
            for j in range(l - 1, i):
                if (arr[j] < arr[i]):
                    dp[l][i] += dp[l - 1][j]
    Sum = 0
    for i in range(k - 1, n):
        Sum += dp[k - 1][i]
    return Sum
arr = [3,2,5,10,15]
n = 3
k = 2

print("Number of Increasing Subsequences is"
      , "=", numOfIncSubseqOfSizeK(arr, n, k))

