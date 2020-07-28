"""Given the array of strings A,
you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
and S2.

For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
"""

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        longstring = ""
        flag = True
        while flag:
            tempstring = []
            for string in A:
                print(string)
                tempstring.append(string[0])
                print(tempstring)
                string = string[1:]
            unq_string = set(tempstring)
            if len(unq_string) == 1:
                print(unq_string)
                v=unq_string.pop()
                print(v)
                longstring=longstring+str(v)

            else:
                flag = False
        return longstring


s = Solution()
a = ["aab", "aabc", "aabcd"]
result = s.longestCommonPrefix(a)
print("Result")
print(result)