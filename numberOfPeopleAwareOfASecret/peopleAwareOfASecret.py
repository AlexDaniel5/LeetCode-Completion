class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0

        for i in range(2, n + 1):
            # People who learned the secret 'delay' days ago can now start sharing
            if i - delay > 0:
                share = (share + dp[i - delay]) % MOD
            # People who learned the secret 'forget' days ago forget it and stop sharing
            if i - forget > 0:
                share = (share - dp[i - forget] + MOD) % MOD
            dp[i] = share # New people who learn the secret today

        # Sum up all people who still remember the secret on the last 'forget' days
        total = 0
        for i in range(n - forget + 1, n + 1):
            total = (total +dp[i]) % MOD
        return total
        
print(Solution().peopleAwareOfSecret(6, 2, 4)) # 5