class Solution:
    def ret_index(self,arr):
        even_index = []
        odd_index = []
        even_list = []
        odd_list = []
        for i in range(len(arr)):
            if i % 2 == 0:
                even_index.append(i)
                even_list.append(arr[i])
            else:
                odd_index.append(i)
                odd_list.append(arr[i])
        return even_list, odd_list
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        special_element_count = 0
        new_array = A.copy()
        n = len(A)
        for pop_ilement in range(n):
            # remove from list
            new_array.pop(pop_ilement)
            e_list, o_list = self.ret_index(new_array)

            lhs = sum(e_list)
            rhs = sum(o_list)
            if lhs == rhs:
                special_element_count = special_element_count+1
            new_array = A.copy()
        return special_element_count



s = Solution()

a = [5, 5, 2, 5, 8]


result = s.solve(a)
print("Result")
print(result)