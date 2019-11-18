import numpy as np

def Up_Shift(a, index, n):
    
    Col = []
    
    for j in range(len(a)):
        Col.append(a[j][index])
    
    Shift_Col = np.roll(Col,-n)
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(j == index):
                a[i][j] = Shift_Col[i]

def Down_Shift(a, index, n):
    
    Col = []
    
    for j in range(len(a)):
        Col.append(a[j][index])
    
    Shift_Col = np.roll(Col,n)
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(j==index):
                a[i][j] = Shift_Col[i]

def Rot_180(n):
    
    bits = "{0:b}".format(n)
    return int(bits[::-1], 2)