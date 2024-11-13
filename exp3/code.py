import csv
import math


def read_csv(file_path):
    with open(file_path,'r') as file:
        reader =csv.DictReader(file)
        data =[]
        for row in reader :
            data.append(row)
    return data

def cal_entropy(target,data):
    label={}

    for row in data:
        if row[target] in label:
            label[row[target]]+=1
        else :
            label[row[target]]=1
    entropy=0.0

    for key ,count in label.items():
        probalitity = (count/len(data))
        entropy+=(-probalitity*math.log2(probalitity))
    
    return entropy

def cal_info_gain(attribute,target,data,total_entropy):

    label ={}

    for row in data:
        if row[attribute] in label:
            label[row[attribute]]+=1
        else :
            label[row[attribute]]=1

    total_subset_entropy=0.0
    
    for keys,count in label.items():
        
        probability = (count/len(data))

        subset =[]

        for row in data :
            if row[attribute]==keys :
                subset.append(row)
        
        subset_entropy =cal_entropy(target,subset)

        total_subset_entropy+=(probability*subset_entropy)
    
    return total_entropy-total_subset_entropy

file_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/exp3/code.csv'

data =read_csv(file_path)

target = input("enter the target attribute name (play)")

features =data[0].keys()-{target}

total_entropy=cal_entropy(target,data)
print(total_entropy)

for feature in features :
    information_gain = cal_info_gain(feature,target,data,total_entropy)
    print(f"information gain for featue {feature} is {information_gain}")
    


