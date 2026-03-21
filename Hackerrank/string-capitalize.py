# def solve(s):
#     char_list = []
#     last_char = ""
    
#     for index, char in enumerate(s):
#         if index == 0:
#             char_list.append(char.capitalize())
#             last_char = char
#             continue
        
#         if last_char == " " and char == " ":
#             char_list.append(char)
#         elif last_char.isalnum():
#             char_list.append(char)
#         elif last_char == " " and char.isalnum():
#             char_list.append(char.capitalize())
        
#         last_char = char
    
#     return "".join(char_list)      

# s : str = input()
# print(solve(s))

# Better  version
def solve(s):
    result = []
    capitalize_next = True
    
    """
    seandainya charnya adalah hello-world
    char = h, e, l, l, o
    pertama adalah h
    true and true:
    result ditambahin sama H
    
    kapital diubah ke false
    
    karena berlaku di huruf pertama, huruf selanjutnya akan masuk ke kondisi false
    untuk huruf-huruf berikutnya, maka akan ditambahkan lansgung ke list result karena tidak akan dikapitalkan.
    deteksi kapital terjadi ketika char saat ini mengandung karakter selain string, entah itu spasi atau yang lainnya.
    
    SOLVED
    
    """
    
    for char in s:
        if capitalize_next and char.isalpha():
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)
        if not char.isalnum():
            capitalize_next = True
    return "".join(result)

s: str = input()
print(solve(s))