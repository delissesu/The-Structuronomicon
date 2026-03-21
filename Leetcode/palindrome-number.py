# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

num : int = int(input())

# 1 2 1 -> 1 2 1
# -1 2 1 -> 1 2 -1

# print(1234// 10);print(1//10)

"""
IDE:
1. karena ada "-", kemungkinan ini convert ke string, bisa juga int tapi dibagi saja.
2. inputan angka diconvert ke string dulu
3. Seandainya pakai cara ambil digit, kesannya sedikit memaksa karena ada simbol.
"""

# Two Pointer
def isPalindrome(x: int) -> bool:
    s = str(x)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    return True

CHECK_RES = isPalindrome(num)
print(CHECK_RES)

# Bagi Sebagian Saja
def isPalindrome2(x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False
        counter : int = 0
        while x > counter:
            counter = counter * 10 + (x % 10)
            x //= 10
        return x == counter or x == counter // 10

CHECK_RES2 = isPalindrome2(num)
print(CHECK_RES2)

# Bagi Keseluruhan
def isPalindrome3(x : int) -> bool:
    if x < 0: return False
    if x % 10 == 0 and x != 0: return False
    ctr_rv : int = 0        
    temp_num : int = x 
    while x:
        ld : int = x % 10
        ctr_rv = ctr_rv * 10 + ld
        x //= 10
    
    return ctr_rv == temp_num

CHECK_RES3 = isPalindrome3(num)
print(CHECK_RES3)

# Tes: Apakaah sama?
def isPalindromeTest(x : int) -> bool:
    if x < 0: return False
    if x % 10 == 0 and x != 0: return False
    ctr_rv : int = 0        
    temp_num : int = x
    print(temp_num, x, ctr_rv)
    while temp_num:
        ld : int = temp_num % 10
        ctr_rv = ctr_rv * 10 + ld
        temp_num //= 10
    
    print(temp_num, x, ctr_rv)
    return ctr_rv == x

CHECK_RES_TEST = isPalindromeTest(num)
print(CHECK_RES_TEST)