import numpy as np
import random as rn

#We make the hornet nests [x, y, n]
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
    total_kills = 0
    remaining_nests = [nest[:] for nest in A]

    for i in range(12):
        n = A[i][2]
        if n >0:
            d = np.sqrt((B[0] - remaining_nests[i][0])**2 + (B[1] - remaining_nests[i][1])**2)
            kills = n * dmax / (20 * d + 0.00001)
            actual_kills = min(kills, remaining_nests[i][2])
            total_kills += actual_kills
            remaining_nests[i][2] -= np.round(actual_kills)
    return np.round(total_kills)

#30,20  70,80  80,0
B1 = [rn.randint(0,101),rn.randint(0,101)]
B2 = [rn.randint(0,101),rn.randint(0,101)]
B3 = [rn.randint(0,101),rn.randint(0,101)]

C = Kills(B1) + Kills(B2) + Kills(B3)

print(C)