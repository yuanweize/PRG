def my_pwc_function(x):
    if x>=6:
        y=float((x-6)**2+5)
    elif 4<=x<6:
        y=5
    elif 2<=x<4:
        y=float(2.5*x-5)
    elif x<2:
        return "NA"
    return y

def get_function_values(par_lst):
    d={}
    for x in par_lst:
        d[x]=my_pwc_function(x)
    return d