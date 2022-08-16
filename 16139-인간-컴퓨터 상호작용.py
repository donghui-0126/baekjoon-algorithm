import sys
input = sys.stdin.readline

sentence = input().strip()
q = int(input())
question_list = [list(input().split()) for _____ in range(q)]


S = [0 for ___ in range(26)]
Letter = []

for i in range(q):     
    li = []
    sumation = 0
    if question_list[i][0] not in Letter:
        for L in sentence:
            if L == question_list[i][0]:
                sumation += 1         
            li.append(sumation)
        S[ord(question_list[i][0])-97] = li
        Letter.append(question_list[i][0])

for j in range(q):
    currnet_question = question_list[j]
    letter = currnet_question[0]
    start, end =  int(currnet_question[1]), int(currnet_question[2])
    if start != 0:
        print(S[ord(question_list[i][0])-97][end] - S[ord(question_list[i][0])-97][start-1])
    else:
        print(S[ord(question_list[i][0])-97][end])

#여기까지는 50점 
# list.index 메소드 때문에 아무래도 50점 밖에 못받은 것 같다.
# 악 오류뜸... 근데 이렇게 하는 건 맞댱...
# 너무 하기가 싫어서 여기까지..!