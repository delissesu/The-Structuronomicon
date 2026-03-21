string = "kamelia"
string = string[:5] + "dan" + string[2:]
print(string)

liststring = list(string)
liststring[2] = "delion"
string = ' '.join(liststring)
print(string)

def mutate_string(string : str, position : int, character : str) -> str:
    return string[:position] + character + string[position + 1:]

if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

