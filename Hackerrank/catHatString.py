def cat_hat(str):
    s_c = "cat"
    s_h = "hat"
    
    cat_count = str.count(s_c)
    hat_count = str.count(s_h)
    
    if cat_count == hat_count:
        return True
    else:
        return False
    
def cat_hat_manual(input_str: str) -> bool:
    count_cat: int = 0
    count_hat: int = 0
    length: int = len(input_str)
    
    # Manual search untuk "cat" dan "hat"
    for i in range(length - 2):  # -2 karena kita perlu 3 karakter
        # Check untuk "cat"
        if input_str[i:i+3] == "cat":
            count_cat += 1
        
        # Check untuk "hat"
        if input_str[i:i+3] == "hat":
            count_hat += 1
    
    return count_cat == count_hat

def cat_hat_manual_v2(input_str: str) -> bool:
    count_cat: int = 0
    count_hat: int = 0
    length: int = len(input_str)
    
    for i in range(1, length - 1):  # Hindari index 0 dan terakhir
        if input_str[i] == "a":
            # Check untuk "cat"
            if input_str[i-1] == "c" and input_str[i+1] == "t":
                count_cat += 1
            
            # Check untuk "hat"  
            if input_str[i-1] == "h" and input_str[i+1] == "t":
                count_hat += 1
    
    return count_cat == count_hat

cat = 0
hat = 0

string = "catinahat"
lenStr = len(string)

for i in range(1, lenStr - 1):
    if string[i] == 'a':
        if string[i - 1] == 'c' and string[i + 1] == 't':
            cat += 1
        if string[i - 1] == 'h' and string[i + 1] == 't':
            hat += 1