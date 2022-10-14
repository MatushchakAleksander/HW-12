import json
from collections import defaultdict

A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}

C = defaultdict(list)

for key in set(list(A.keys()) + list(B.keys())):
    if key in A:
        C[key].append(A[key])
    if key in B:
        C[key].append(B[key])
print(C)

result = json.dumps(C)
with open("result.json", "w") as f:
    f.write(result)
    
f.close()
