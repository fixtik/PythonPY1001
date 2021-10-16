A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))
if (A < 45 and (B and C) >= 45) or (B < 45 and (A and C) >= 45) or (C < 45 and (B and A) >= 45):
    print ("ok")