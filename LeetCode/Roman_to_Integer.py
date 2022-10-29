class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        d2={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        output=0
        for i,j in enumerate(s):
            if s[i:i+2]in d2:
                output -= d[j]
            else:
                output+=d[j]
        return output


if __name__ == '__main__':
    main = Solution()
    main.isPalindrome(121)