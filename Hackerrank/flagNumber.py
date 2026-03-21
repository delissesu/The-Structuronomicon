class Solution:
    def checkStatus(self, a, b, flag):
        # Case 1: Either a or b (not both) is non-negative and flag is false
        if not flag and (a >= 0) != (b >= 0):
            return True
        
        # Case 2: Both a and b are negative and flag is true
        if flag and a < 0 and b < 0:
            return True
        
        return False
    
class Solution2:
    def checkStatus(self, a, b, flag):
        # Manual check semua kombinasi
        if flag == False:
            # Either a or b (not both) is non-negative
            if a >= 0 and b < 0:  # a non-negative, b negative
                return True
            elif a < 0 and b >= 0:  # a negative, b non-negative
                return True
            else:
                return False
        elif flag == True:
            # Both a and b are negative
            if a < 0 and b < 0:
                return True
            else:
                return False
        else:
            return False