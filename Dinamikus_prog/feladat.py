def substringDiff(k, s1, s2):
    n = len(s1)
    max_len = 0

    # Create a DP table initialized to zero
    # dp[i][j][d] represents longest substring ending at s1[i] and s2[j] with exactly d mismatches
    dp = []
    for _ in range(n + 1):
        dp_2D = []
        for _ in range(n + 1):
            dp_1D = []
            for _ in range(k + 1):
                dp_1D.append(0)
            dp_2D.append(dp_1D)
        dp.append(dp_2D)


    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for d in range(k + 1):
                # If characters match, inherit the longest substring length from previous characters
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j][d] = dp[i - 1][j - 1][d] + 1
                # If characters don't match, check if we can use one of the allowed mismatches
                elif d > 0:
                    dp[i][j][d] = dp[i - 1][j - 1][d - 1] + 1

                # Update the result with the maximum length found
                max_len = max(max_len, dp[i][j][d])

    return max_len

