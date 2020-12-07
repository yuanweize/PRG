def is_right(a,b,c):
    list=[a,b,c]
    to = is_int(list[0]) + is_int(list[1]) + is_int(list[2])  
    '''three numbers meet'''
    if to == 3:
        if list[0]**2 + list[1]**2 == list[2]**2 or list[0]**2 + list[2]**2 == list[1]**2 or list[2]**2 + list[1]**2 == list[0]**2:
            '''Pythagorean theorem'''
            return True
        else:
            return False
    else:
        return "Please enter a positive integer"

def is_int(ipt):
    '''Check three sides'''
    ipt = str(ipt)
    if ipt.count(".") == 0 and ipt.count('-') == 0 and ipt.isdigit(): 
        """Exclude decimals, negative numbers, letters"""
        return 1  
        """Positive integers return 1"""
    else:
        return 0   
        """otherwise return 0"""


#############################################################################################################
def is_right_1(a,b,c):
    list=[a,b,c]
    for ipt in list: 
        '''Check three sides'''
        ipt = str(ipt)
        if ipt.count(".") == 1 or ipt.count('-') == 1 or ipt.isdigit() == 'False': 
            '''Exclude illegel input'''
            return "Please enter a positive integer"        
    else:
        if list[0]**2 + list[1]**2 == list[2]**2 or list[0]**2 + list[2]**2 == list[1]**2 or list[2]**2 + list[1]**2 == list[0]**2:
            '''Pythagorean theorem'''
            return True
        else:
            return False