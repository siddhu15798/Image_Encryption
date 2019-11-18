import sys
import random
import numpy as np
from Help import *
from PIL import Image

Image = Image.open('Encrypted_Images/' + sys.argv[1])
Pixel = Image.load()

R = []
G = []
B = []

for i in range(Image.size[0]):
    
    R.append([])
    G.append([])
    B.append([]) 
    
    for j in range(Image.size[1]):
    
        RGB_Per_Pixel = Pixel[i,j]
        R[i].append(RGB_Per_Pixel[0])
        G[i].append(RGB_Per_Pixel[1])
        B[i].append(RGB_Per_Pixel[2])

M = Image.size[0]
N = Image.size[1]

Kr = []
Kc = []

print('Enter value of Kr')
for i in range(M):
	Kr.append(int(input()))

print('Enter value of Kc')
for i in range(N):
	Kc.append(int(input()))

print('Enter value of Iter_Max')
Iter_Max = int(input())

for Iter in range(Iter_Max):
    
    #XOR For each Column
    for j in range(N):
        for i in range(M):
            if(j % 2 == 0):
                R[i][j] = R[i][j] ^ Kr[i]
                G[i][j] = G[i][j] ^ Kr[i]
                B[i][j] = B[i][j] ^ Kr[i]
            else:
                R[i][j] = R[i][j] ^ Rot_180(Kr[i])
                G[i][j] = G[i][j] ^ Rot_180(Kr[i])
                B[i][j] = B[i][j] ^ Rot_180(Kr[i])
                
    #XOR For each Row
    for i in range(M):
        for j in range(N):
            if(i % 2 == 1):
                R[i][j] = R[i][j] ^ Kc[j]
                G[i][j] = G[i][j] ^ Kc[j]
                B[i][j] = B[i][j] ^ Kc[j]
            else:
                R[i][j] = R[i][j] ^ Rot_180(Kc[j])
                G[i][j] = G[i][j] ^ Rot_180(Kc[j])
                B[i][j] = B[i][j] ^ Rot_180(Kc[j])
                
    #For each Column
    for i in range(N):  
        R_Total_Sum = 0
        G_Total_Sum = 0
        B_Total_Sum = 0
        for j in range(M):
            R_Total_Sum += R[j][i]
            G_Total_Sum += R[j][i]
            B_Total_Sum += R[j][i]
            
        R_Mod = R_Total_Sum % 2
        G_Mod = G_Total_Sum % 2
        B_Mod = B_Total_Sum % 2

        if(R_Mod == 0):
            Down_Shift(R, i , Kc[i])
        else:
            Up_Shift(R, i, Kc[i])

        if(G_Mod == 0):
            Down_Shift(G, i , Kc[i])
        else:
            Up_Shift(G, i, Kc[i])

        if(B_Mod == 0):
            Down_Shift(B, i , Kc[i])
        else:
            Up_Shift(B, i , Kc[i])
            
    #For each Row
    for i in range(M): 
        R_Total_Sum = sum(R[i])
        G_Total_Sum = sum(G[i])
        B_Total_Sum = sum(B[i])
        
        R_Mod = R_Total_Sum % 2
        G_Mod = G_Total_Sum % 2
        B_Mod = B_Total_Sum % 2

        if(R_Mod == 0):
            R[i] = np.roll(R[i], -Kr[i])
        else:
            R[i] = np.roll(R[i], Kr[i])

        if(G_Mod == 0):
            G[i] = np.roll(G[i], -Kr[i])
        else:
            G[i] = np.roll(G[i], Kr[i])

        if(B_Mod == 0):
            B[i] = np.roll(B[i], -Kr[i])
        else:
            B[i] = np.roll(B[i], Kr[i])
            
for i in range(M):
    for j in range(N):
        Pixel[i,j] = (R[i][j], G[i][j], B[i][j])

Image.save('Decrypted_Images/' + sys.argv[1])