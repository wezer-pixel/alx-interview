def minOperations(n):
    if n <= 0:
        return 0

    # Initialize variables to store the minimum operations for each position
    dp = [float('inf')] * (n + 1)

    # Base case: 0 operations needed for 1 character
    dp[1] = 0

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Try to find the factors of i
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                # Update the minimum operations for i if possible
                dp[i] = min(dp[i], dp[j] + i // j, dp[i // j] + j)

    # Return the minimum operations needed for n characters
    return dp[n] if dp[n] != float('inf') else 0

