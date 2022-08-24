#python3
#stats.py - statistics on my dear 2048 player.

import time, sys, math

scoresFile = open('scores.txt', 'r')

scores = []
times = []
numberOfScores = len(scoresFile.readlines())
highScore = int()
highScoreTime = str()
lowScore = 100000
lowScoreTime = str()
averageScore = int()
avgDeviation2 = 0
scoresFile.close()
scoresFile = open('scores.txt', 'r')

for v in scoresFile.readlines():
    score, time1 = v.split(' - ')
    score = int(score)
    time1 = time1.rstrip('\n')
    scores.append(score)
    times.append(time1)
    averageScore += (score/numberOfScores)
    if score > highScore:
        highScore = score
        highScoreTime = time1
    if score < lowScore:
        lowScore = score
        lowScoreTime = time1
scoresFile.close()

scoresFile = open('scores.txt','r')
# std dev calculation
for v in scoresFile.readlines():
    score, time1 = v.split(' - ')
    score = int(score)
    deviation = abs(averageScore - score)
    deviation2 = deviation*deviation
    avgDeviation2 += (deviation2/numberOfScores)
    


stdDev = round(math.sqrt(avgDeviation2))
averageScore = round(averageScore)
scoresFile.close()
print(f'''---2048PLAYER.PY STATISTICS---
# of games played: {numberOfScores}
High score: {highScore}
High score date: {highScoreTime}
Low score: {lowScore}
Low score date: {lowScoreTime}
Average score: {averageScore}
Standard deviation: {stdDev}''')

print('\n\nHit enter to close window.')
while True:
    i = input()
    if i == '':
        break
    else:
        print('Invalid input, try again.')
        continue

    
sys.exit()




