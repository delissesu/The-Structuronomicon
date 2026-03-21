def countSubstring_bruteforce(s: str) -> int:
    count = 0
    n = len(s)
    
    # Check all possible substrings
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            
            if 'a' in substring and 'b' in substring and 'c' in substring:
                count += 1
    
    return count

# List of strings
strings = ['abcde', 'aabbcc', 'abac']

# Count substrings for each string in the list
total_count = 0
for s in strings:
    count = countSubstring_bruteforce(s)
    total_count += count
print(total_count)
