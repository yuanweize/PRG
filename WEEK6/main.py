import mymath
def get_trig_series(lst):
    cc=[]
    ss=[]
    for f in lst:
        c=mymath.cos(f)
        s=mymath.sin(f)
        cc.append(c)
        ss.append(s)
    return cc,ss