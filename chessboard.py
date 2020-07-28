class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if (A == 1 and B >= 1) or (B == 1 and A >= 1) or (A == 8 and B >= 1) or (B == 8 and A >= 1):
            return 7
        if (A == 2 and B >= 1) or (B == 2 and A >= 1) or (A == 7 and B >= 1) or (B == 7 and A >= 1):
            return 9
        if (A == 3 and B >= 1) or (B == 3 and A >= 1) or (A == 6 and B >= 1) or (B == 6 and A >= 1):
            return 11
        if (A == 4 and B >= 1) or (B == 4 and A >= 1) or (A == 5 and B >= 1) or (B == 5 and A >= 1):
            return 13


s = Solution()

result = s.gcd(2, 2)
print("Result")
print(result)