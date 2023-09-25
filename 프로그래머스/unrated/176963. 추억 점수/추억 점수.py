def solution(name, yearning, photo):
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    answer = []
    
    for i in range(len(photo)):
        count = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                count += dic[photo[i][j]]
        answer.append(count)
    return answer