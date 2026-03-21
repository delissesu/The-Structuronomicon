def friends_in_trouble(j_angry, s_angry):
    # Case 1: Both angry
    if j_angry and s_angry:
        return True
    # Case 2: Both not angry  
    elif not j_angry and not s_angry:
        return True
    # Case 3: Only one angry
    else:
        return False
    
def friends_in_trouble2(j_angry, s_angry):
    # You're in trouble if both have same state (both angry OR both not angry)
    return j_angry == s_angry