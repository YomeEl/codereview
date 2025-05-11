def count_numbers(K, N):
    MOD = 10**9 + 7
    dp = [[[0]*4 for _ in range(N)] for _ in range(K)]
    
    # Base case initialization: single-digit numbers
    for k in range(K):
        dp[k][0][0] = 1
    
    # Dynamic programming transition
    for pos in range(1, N):
        for prev_digit in range(K):
            for zero_count in range(4):
                next_zero_count = zero_count + 1 if prev_digit == 0 else 0
                if next_zero_count > 3:
                    continue
                for digit in range(K):
                    dp[digit][pos][next_zero_count] += dp[prev_digit][pos-1][zero_count]
                    dp[digit][pos][next_zero_count] %= MOD
                    
    total_count = sum(dp[d][N-1][z] for d in range(K) for z in range(4)) % MOD
    return total_count

# Example usage
K = 8   # base of the number system
N = 15  # number of digits
result = count_numbers(K, N)
print(result)