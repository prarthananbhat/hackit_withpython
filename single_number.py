#Given an array of integers, every element appears thrice except for one which occurs once.

#Find that element which does not appear thrice.

# Note: Your algorithm should have a linear runtime complexity.
#
# Could you implement it without using extra memory?

# Constraints:

# 2 <= N <= 5 000 000
# # 0 <= A[i] <= INT_MAX
import math

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        A.sort()
        print(A)
        i=0
        r = math.ceil(len(A)/3)

        for i in range(r):
            j= i*3+2
            if j>len(A):
                return(A[-1:][0])
            if A[j] - A[i*3] !=0:
                index=i
                return A[j+1]
            else:
                pass
        return None



# a = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# a=[1,0,1,0]
#
# s = Solution()
#
# result = s.singleNumber(a)
# print("Result")
# print(result)


A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
first = []
second = []
for i in range(len(A)):
    print(i)
    if i==0:
       first.append(A[i])

    else:
        if len(first)!=0:
            print("length",len(first))
            if (A[i] in set(first)):
                if len(second) != 0:
                    if A[i] in set(second):
                        first.remove(A[i])
                        second.remove(A[i])
                    else:
                        second.append(A[i])
                else:
                    second.append(A[i])
            else:
                first.append(A[i])
        else:
            first.append(A[i])
    print(first)
    print(second)
    print()
print(first[0])
