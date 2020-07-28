import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        maxval = max(A,B)
        minval = min(A,B)
        if A==0 or B == 0:
            return max(A,B)
        if A==B:
            return A
        factor = []
        b_factor = []
        gcd = 1
        for i in range(1, math.ceil(maxval/2)):
            if maxval % i == 0:
                if (i <= minval) and (minval % i == 0) and (i > gcd):
                    print(i)
                    gcd = i
        return gcd


s = Solution()



result = s.gcd(2,2)
print("Result")
print(result)