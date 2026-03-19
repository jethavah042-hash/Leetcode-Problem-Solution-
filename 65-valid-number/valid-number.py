class Solution(object):
    def isNumber(self, s):
        s = s.strip()   # remove leading & trailing spaces
        
        if not s:
            return False
        
        num_seen = False   # digit found
        dot_seen = False   # '.' found
        e_seen = False     # 'e' or 'E' found
        
        for i, ch in enumerate(s):
            
            # Case 1: digit
            if ch.isdigit():
                num_seen = True
            
            # Case 2: sign + or -
            elif ch in ['+', '-']:
                # valid only at start OR just after e/E
                if i != 0 and s[i-1] not in ['e', 'E']:
                    return False
            
            # Case 3: decimal point
            elif ch == '.':
                # only one dot allowed and not after exponent
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            
            # Case 4: exponent
            elif ch in ['e', 'E']:
                # exponent must appear once and after number
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False   # must see digit after e
            
            # Case 5: invalid character
            else:
                return False
        
        return num_seen