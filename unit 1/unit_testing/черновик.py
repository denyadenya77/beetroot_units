stat = {'q1': [0, 0], 'q2': [0, 0], 'q3': [0, 0]}
results = [True, False, True]

if results[0] == True:
    stat['q1'][0] += 1
elif results[0] == False:
    stat['q1'][1] += 1
if results[1] == True:
    stat['q2'][0] += 1
elif results[1] == False:
    stat['q2'][1] += 1
if results[2] == True:
    stat['q3'][0] += 1
elif results[2] == False:
    stat['q3'][1] += 1

print(stat)