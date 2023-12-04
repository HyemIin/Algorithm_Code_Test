def solution(array, commands):
    answer = []
    for command in commands:
        arr = array[command[0]-1:command[1]]
        lst = sorted(arr)
        ans = lst[command[2]-1]
        answer.append(ans)
    return answer