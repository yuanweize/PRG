def is_right(a,b,c):
    list=[a,b,c]
    for ipt in list: #Check three sides
        ipt = str(ipt)
        if ipt.count(".") == 1 or ipt.count('-') == 1 or ipt.isdigit() == 'False': #Exclude illegel input
            return "Please enter a positive integer"        
    else:
        if list[0]**2 + list[1]**2 == list[2]**2 or list[0]**2 + list[2]**2 == list[1]**2 or list[2]**2 + list[1]**2 == list[0]**2:#Pythagorean theorem
            return True
        else:
            return False