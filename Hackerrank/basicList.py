if __name__ == '__main__':
    n: int = int(input())
    numbers: list[int] = []
    
    for _ in range(n):
        command: str = input().strip()
        
        if command == 'print':
            print(numbers)
        elif command == 'sort':
            numbers.sort()
        elif command == 'pop':
            numbers.pop()
        elif command == 'reverse':
            numbers.reverse()
        elif command.startswith('insert'):
            parts: list[str] = command.split()
            index: int = int(parts[1])
            value: int = int(parts[2])
            numbers.insert(index, value)
        elif command.startswith('remove'):
            parts: list[str] = command.split()
            value: int = int(parts[1])
            numbers.remove(value)
        elif command.startswith('append'):
            parts: list[str] = command.split()
            value: int = int(parts[1])
            numbers.append(value)