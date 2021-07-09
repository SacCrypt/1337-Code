def valid(s):
    _ = []
    for x in s:
        try:
            if _[-1] - ord(x) == 2:
                _.pop(-1)
            else:
                return False
        except:
            pass
        _.append(ord(x))
        
        
    
        
        
        
