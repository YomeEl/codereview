def count_numbers(K, N):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(pos, prev_zero_count, is_start):
        if pos == N:
            return 1
        total = 0
        for digit in range(0 if not is_start else 1, K):
            new_zero_count = prev_zero_count + 1 if digit == 0 else 0
            if new_zero_count <= 3:
                total += dp(pos + 1, new_zero_count, False)
        return total

    return dp(0, 0, True)

K, N = map(int, input().split())
print(count_numbers(K, N))