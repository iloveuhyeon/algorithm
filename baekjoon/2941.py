value = input()
croatia = ["c=", "c-", "dz=","d-","lj","nj","s=","z="]
for i in croatia:
    value = value.replace(i,"*")
print(len(value))