def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        elif signs[i] == False:
            answer -= absolutes[i]
    return answer

#zip에 활용 방법에 대해서