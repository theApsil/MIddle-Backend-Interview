'''
https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/
'''

def findTheLongestBalancedSubstring(s: str) -> int:
    zero_cnt, one_cnt, ans = 0, 0, 0

    for i in range(len(s)):
        if s[i] == '0':
            if one_cnt == zero_cnt:
                ans = max(zero_cnt, one_cnt)
            one_cnt = 0
            zero_cnt += 1
        else:
            one_cnt += 1
            if one_cnt <= zero_cnt:
                ans = max(zero_cnt, one_cnt)
            if i + 1 < len(s) and s[i + 1] != s[i]:
                zero_cnt = 0

    return ans * 2


print(findTheLongestBalancedSubstring("01000111"))
print(findTheLongestBalancedSubstring("0011"))
print(findTheLongestBalancedSubstring("111"))
