class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_array = list(str(x))
        x_array_reverse = list(str(x))
        x_array_reverse.reverse()

        if x_array == x_array_reverse:
            return print(True)
        else:
            return print(False)


if __name__ == '__main__':
    main = Solution()
    main.isPalindrome(121)