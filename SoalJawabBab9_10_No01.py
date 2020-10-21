# Rangkaian Listrik Lanjut
# Jawaban soal no 1
# ------------------------
import math

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

def parallel(Z1,Z2):
    Z = Z1*Z2/(Z1+Z2)
    return Z

# === Program Utama ===
# ---------------------
w = 5
Vs = pol2rec(4,0)
R, L, C = 2, 1, 0.05
ZR, ZL, ZC = R, 1j*w*L, 1/(1j*w*C)
print(ZR,ZL,ZC)

ZP = parallel(ZR,ZC)
Io = Vs / (ZL + ZP)
AIo, PIo = rec2pol(Io)
print(ZP)
print(Io)
print(round(AIo,4),round(PIo,4))