highscore = [64, 56, 74, 72, 89]
print ("High score:")
for i, score in enumerate(highscore):
    print (i+1, ".", score)
# New high score
a = int(input("Enter a new score:"))
highscore.append(a)
for i, score in enumerate(highscore):
    print (i+1, ".", score)