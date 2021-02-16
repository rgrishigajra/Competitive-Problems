function f(n, k){
  let dp = new Array(n + 1)
  for (let i=0; i<n+1; i++)
    dp[i] = new Array(k + 1).fill(0)
  dp[0][0] = 1
  
  for (let i=1; i<=n; i++)
    for (let j=1; j<=Math.min(i, k); j++)
      dp[i][j] = dp[i - j][j] + dp[i - 1][j - 1]

  return dp[n][k]
}

console.time('time taken')
console.log(f(1000, 10))
console.timeEnd('time taken')