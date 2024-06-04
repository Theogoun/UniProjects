import numpy as np
import random as rn

#We make the hornet nests, first element x, second y, third the number of hornets
A = []
A.append([25, 65, 100])
A.append([23, 8, 200])
A.append([7, 13, 327])
A.append([95, 53, 440])
A.append([3, 3, 450])
A.append([54, 56, 639])
A.append([67, 78, 650])
A.append([32, 4, 678])
A.append([24, 76, 750])
A.append([66, 89, 801])
A.append([84, 4, 945])
A.append([34, 23, 967])
#Through calculations we find that the maximum distance between them is (3,3) and (66,89):
dmax = 106.61

def Kills(B):
    kills = 0
    for i in range(12):
        n = A[i][2]
        d = np.sqrt(np.power(B[0] + A[i][0],2) + np.power(B[1] + A[i][1],2))
        kills += n * dmax / (20 * d + 0.00001)
    return np.round(kills)

B1 = [rn.randint(0,101),rn.randint(0,101)]
B2 = [rn.randint(0,101),rn.randint(0,101)]
B3 = [rn.randint(0,101),rn.randint(0,101)]

C = Kills(B1) + Kills(B2) + Kills(B3)

print(C)