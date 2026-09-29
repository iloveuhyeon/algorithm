subjectList = []
subjectScore = 0
for _ in range(20):
    name, score, grade = input().split()
    score = float(score)
    if grade == "A+":
        subjectList.append(float(score) * 4.5)
        subjectScore+= score
    elif grade == "A0":
        subjectList.append(float(score) * 4.0)
        subjectScore+= score
    elif grade == "B+":
        subjectList.append(float(score) * 3.5)
        subjectScore+= score
    elif grade == "B0":
        subjectList.append(float(score) * 3.0)
        subjectScore+= score
    elif grade == "C+":
        subjectList.append(float(score) * 2.5)
        subjectScore+= score
    elif grade == "C0":
        subjectList.append(float(score) * 2.0)
        subjectScore+= score
    elif grade == "D+":
        subjectList.append(float(score) * 1.5)
        subjectScore+= score
    elif grade == "D0":
        subjectList.append(float(score) * 1.0)
        subjectScore+= score
    elif grade == "F":
        subjectList.append(float(score) * 0)
        subjectScore+= score
    else :
        continue
print(round(sum(subjectList) / subjectScore , 6))