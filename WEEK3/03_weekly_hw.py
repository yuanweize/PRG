def compute_time_diff(h1,m1,h2,m2):
    m3 = m2 - m1
    h3 = h2 - h1
    if m3 < 0:
        m3 = m3 + 60
        h3 = h3 - 1
    return h3,m3
        
h,m = compute_time_diff(13,20,15,10)
print(h,m)