# logic : Separate positive and negative numbers then merge then alternately
# input : [-1, 2, -3, 4, 5, -6]
# ouput : [ -1, 2, -3, 4, -6,5]
a = [-1, 2, -3, 4, 5, -6]
positive = []
negative = []
for i in a:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)
result = []
for i in range(max(len(positive), len(negative))):
    if i < len(negative):
        result.append(negative[i])
    if i < len(positive):
        result.append(positive[i])
print(result)