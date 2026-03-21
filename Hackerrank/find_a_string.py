# Concept
string = "delissesu"
for i in range(0, len(string)):
    print(string[i])

def count_substring(string : str, sub_string : str, count : int = 0) -> int:
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)