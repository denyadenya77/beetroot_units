import json

with open('stat_test.json', 'w') as file_obj:
    l = {'q1': [0, 0], 'q2': [0, 0], 'q3': [0, 0], 'comment': ['True answers', 'False answers']}
    json.dump(l, file_obj)

