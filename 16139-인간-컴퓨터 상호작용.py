from posixpath import split
import sys
from unittest.mock import sentinel
input = sys.stdin.readline

sentence = input().strip()
q = int(input())
question_list = []

for _ in range(q):
    question_list.append(input().strip())

sumation = 0
S = [] 
for L in (sentence):
    if L == question_list[0][0]:
        sumation += 1
    S.append(sumation)


for i in range(q):
    currnet_question = question_list[i]
    letter = currnet_question[0]
    start, end =  map(int,currnet_question[1:].split())
    if start != 0:
        print(S[end] - S[start-1])
    else:
        print(S[end])

#이거 왜 런타임 에러뜸???