import csv

def read_csv(file_path):
    with open(file_path,'r') as file:
       reader =csv.reader(file)

       transactions =[]
       for row in reader:
           a= set()
           for item in row:
               a.add(item.lower().strip())
           transactions.append(a)
       return transactions

def calculate_support(transactions,x):
    count=0
    for transaction in transactions:
        if set(x).issubset(transaction):
          count+=1
    return (count/len(transactions))


x=input("Enter x side of the association rule values to be separated by the , like (Bread,Tak)").lower().split(',')
y=input("Enter y side of the association rule values to be separated by the , like (Bread,Tak)").lower().split(',')
print(x)
file_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/exp5_6/code.csv'
data =read_csv(file_path)

support =calculate_support(data,x+y)
