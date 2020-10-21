# Rangkaian Listrik Lanjut
# Jawaban Soal Latihan
# Zulfiar Ahimsa Mahardhika 
# 0711 19 4000 0095
# ------------------------
import math
import numpy as np

# === Definisi Fungsi ===
# -----------------------
def pol2rec(absval,phdegval):
    phradval = phdegval*math.pi/180
    x, y = absval*math.cos(phradval), absval*math.sin(phradval)
    rect = x + 1j*y
    return rect

def rec2pol(rect):
    x, y = rect.real, rect.imag
    absval, phradval = math.sqrt(x*x+y*y), math.atan2(y,x) 
    phdegval = phradval * 180/math.pi
    return absval,phdegval

# === Program Utama ===
# ---------------------
Vs1 = pol2rec(120,-90)
Vs2 = pol2rec(120,-30)
Z = 80-1j*35

# Menyelesaikan persamaan dalam bentuk matriks
ZM = np.matrix([[Z, 0, -Z], [0, Z, Z], [0, 0, Z]])
VM = np.matrix([[Vs1], [Vs2], [Vs1-Vs2]])
IM = ZM.I * VM
I1 = IM[0,0]
I2 = -IM[0,0]-IM[1,0]
I3 = IM[1,0]
I4 = IM[2,0]

AI1,PI1 = rec2pol(I1)
AI2,PI2 = rec2pol(I2)
AI3,PI3 = rec2pol(I3)

print(round(AI1,4),round(PI1,4))
print(round(AI2,4),round(PI2,4))
print(round(AI3,4),round(PI3,4))