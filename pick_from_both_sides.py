class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        new_array = A + A[0:B]
        print("New Array ",new_array)
        n = len(A)

        sum_values = sum(A[:B])
        max_sum = sum_values

        for i in range(B):
            print("------")
            print("Max Sum:", max_sum)
            print("Index ",i)
            sum_values = sum(new_array[(n-B)+i:(n+i)])
            if sum_values > max_sum:
                max_sum = sum_values


        return max_sum

s = Solution()

a = [5, -2, 3 , 1, 2, -4, 1]
b = 7
result = s.solve(a,b)
print("Result")
print(result)
# print(len(a))

# v = sum(a[6:]) + sum(a[:2])
# v= sum(a[3:3+47])
# print(v)
