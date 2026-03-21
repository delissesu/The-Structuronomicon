def searchSubstring(string: str, target: str) -> tuple[int, list[int]]:
    wsize: int = len(target)
    counter: int = 0
    len_string: int = len(string)
    positions: list[int] = []  # Simpan posisi, bukan substring
    
    for i in range(len_string - wsize + 1):
        if string[i:i+wsize] == target:
            counter += 1
            positions.append(i)  # Simpan index posisi
    
    return counter, positions

text: str = input().strip()
target: str = input().strip()

count, pos = searchSubstring(text, target)
print(f"Found {count} occurrences at positions: {pos}")