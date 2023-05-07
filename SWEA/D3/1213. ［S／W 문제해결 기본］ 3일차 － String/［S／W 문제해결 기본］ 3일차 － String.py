for j in range(10):
    t = int(input())
    word = input()
    sentence = input()
    count = 0
    for i in range(len(sentence)-len(word)+1):
        same = ""
        for k in range(len(word)):
            same += sentence[i+k]
        if same == word:
            count +=1
    print("#"+f"{j+1}",count)