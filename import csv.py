import csv
import pandas as pd
header = ["Name","Age","City"]
data = [
    ["Alice",30,"Newyork"],
    ["Bob",25,"London"],
    ["Charlie",35,"Paris"]
]
csv_name = "mydata.csv"
with open(csv_name,'w',newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    csv_writer.writerows(data)
print(f"Csv file '{csv_name}' created sucessfully")
df = pd.read_csv('mydata.csv')
print(df)