
# n = 5

# def function (n):
#     if n == 0:
#         return 1

#     return n * function(n-1)

# print(function(5)) 

class Solution:
    def checkString(self, s):
        v = 0
        c = 0

        vowels = "aeiou"

        for ch in s:
            if ch in vowels:
                v += 1
            else:
                c += 1

        if v > c:
            print("Yes")
        elif v < c:
            print("No")
        else:
            print("Same")


s = input()
obj = Solution()
obj.checkString(s)


class Solution:
    def removeChars(self, s):
        result = ""

        for ch in s:
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                result += ch

        return result