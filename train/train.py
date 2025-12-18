import pandas as pd

df = pd.read_csv("train.csv")

fc = 0 # Total no of females
fs = 0 # Number of females survived
fns = 0 # Number of females not survived
mc = 0 # Total no of males
ms = 0 # Total no of males survived
mns = 0 # Total no of males not survived

for index, row in df.iterrows():
    sex = row['Sex']
    age = row['Age']
    survived = row['Survived']
    if sex == 'female' and age < 20:
        fc += 1
        if survived == 1:
            fs += 1
        else:
            fns += 1

    if sex == 'male' and age > 40:
        mc += 1
        if survived == 1:
            ms += 1
        else:
            mns += 1

print("Females < 20:", fc)
print("   Survived:", fs)
print("   Not Survived:", fns)

print("\nMales > 40:", mc)
print("   Survived:", ms)
print("   Not Survived:", mns)
