
def velocidad(d, t):
    if(d < 0 or t <= 0):
        return 0
    else:
        v = (d)/(t)
        
    return v

def distancia(v, t):
    if(v < 0 or t <= 0):
        return 0
    else:
        d = (v)*(t)
    return d

def tiempo(d, v):
    if(d < 0 or v <= 0):
        return 0
    else:
        t = (d)/(v)
    return t

