from itertools import permutations
import math

def solution(numbers):
    num = []
    for i in range(len(numbers)):
        num.append(numbers[i])
    
    history = []
    answer = 0
    for i in range(1,len(numbers)+1):
        per = list(permutations(num,i))
        for j in range(len(per)):
            target = "".join(per[j])
            sosu = False
            if int(target) not in history:
                history.append(int(target))
                for k in range(2,int(math.sqrt(int(target)))+1):
                    if int(target)%k == 0:
                        sosu = True
                if sosu == False and int(target) != 0 and int(target) != 1:
                    answer += 1
                

    return answer