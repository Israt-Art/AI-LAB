"""Problem 3: List Processing
1 Given scores = [55,78,62,49,85,91,73].
2 Create a new list containing only scores greater than 70.
3 Calculate the average score.
4 Find the maximum and minimum scores."""


scores = [55, 78, 62, 49, 85, 91, 73]


high_scores = []
for i in range(len(scores)):
    if scores[i] > 70:
        high_scores.append(scores[i])
print("Scores greater than 70:", high_scores)


total = 0
for i in range(len(scores)):
    total += scores[i]
average_score = total / len(scores)
print("Average score:", average_score)


max_score = scores[0]
min_score = scores[0]
for i in range(1, len(scores)):
    if scores[i] > max_score:
        max_score = scores[i]
    if scores[i] < min_score:
        min_score = scores[i]
print("Maximum score:", max_score)
print("Minimum score:", min_score)