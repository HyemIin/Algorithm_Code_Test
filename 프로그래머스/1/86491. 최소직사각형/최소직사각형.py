def solution(sizes):
    lst_x = []
    lst_y = []
    for card in sizes:
        x = card[0]
        y = card[1]
        if x>=y:
            lst_x.append(x)
            lst_y.append(y)
        else:
            lst_x.append(y)
            lst_y.append(x)
    max_x = max(lst_x)
    max_y = max(lst_y)
    answer = max_x*max_y
    return answer