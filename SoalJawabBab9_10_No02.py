# Rangkaian Listrik Lanjut
# Jawaban soal no 2
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
w = 1000
Vs1 = pol2rec(10,0)
Vs2 = pol2rec(20,-90)
R, L, C = 2000, 0.4, 1e-6
ZR, ZL, ZC = R, 1j*w*L, 1/(1j*w*C)
print(ZR,ZL,ZC)

ZM = np.matrix([[ZR+ZL, -ZL], [-ZL, ZL+ZC]])
VM = np.matrix([[Vs1], [-Vs2]])
IM = ZM.I * VM
Io = IM[0,0]-IM[1,0]
AIo,PIo = rec2pol(Io)
print(ZM)
print(VM)
print(IM)
print(Io)
print(round(AIo,4),round(PIo,4))