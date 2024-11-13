import csv
from itertools import combinations


def read_csv(file_path):
    with open(file_path,'r') as file :
        reader =csv.reader(file)
        data =[]

        for row in reader:
            ans =set()
            for i,item in enumerate(row):
                if item and i!=0:
                     ans.add(item.strip())
            data.append(ans)

    return data


def get_itemset(transactions,level):
    a=set()
    for transaction in transactions:
        for item in combinations(sorted(transaction),level):
            a.add(item)
    return a

def get_frequent_itemset(min_support,transactions):
    level = 1
    itemsets =[]
    candidate_itemset =get_itemset(transactions,level)

    while candidate_itemset:
        freq_count ={}
        for item in candidate_itemset:
            freq_count[item]=0
        
        for transaction in transactions:
            for  item in candidate_itemset:
                if set(item).issubset(transaction):
                    freq_count[item]+=1
        
        frequent_itemset ={}
        for key,count in freq_count.items():
            if count>=min_support:
                frequent_itemset[key]=count
        
        if frequent_itemset:
            print(f"Frequent Itemsets for the level  {level} are ")
            for key ,count in frequent_itemset.items():
                print(f"itemset {key}------->support {(count*100)/len(transactions)}")
        else:
            print(f"dont found any new candidate itemset at level {level}")
            break
        
        itemsets.append(frequent_itemset)

        unique_vals=set()

        for keys in frequent_itemset.keys():
            for i in keys:
                unique_vals.add(i)
        
        candidate_itemset=set()
        level+=1
        for items in combinations(unique_vals,level):
            candidate_itemset.add(items)
    return itemsets


def get_support(subset,transactions):
    count =0
    for transaction in transactions:
        if set(subset).issubset(transaction):
            count+=1
    return count

def get_association(data ,min_support,min_confidence,transactions):
    association_rules=[]

    for level in range(1,len(data)):
        for item,support in data[level].items():
           for i in range(1,len(item)):
               subsets =list(combinations(item,i))

               for subset in subsets:
                   subset=set(subset)
                   remainder =set(item)-subset

                   if len(remainder)>0:
                       subset_support =get_support(subset,transactions)
                       confidence =support/subset_support if subset_support>0 else 0
                       if confidence>=min_confidence :
                           association_rules.append((subset,remainder,confidence))
    return association_rules
               



file_path ='C:/Users/nalaw/OneDrive/Desktop/dm/exp5_6/code.csv'

transactions = read_csv(file_path)

support_percentage = float(input("enter the min supoort in percentage"))
min_support =(support_percentage/100)*len(transactions)
confidence_percentage = float(input("Enter the minimum confidence as a percentage (e.g., 70 for 70%): "))
min_confidence = confidence_percentage / 100

itemset =get_frequent_itemset(min_support,transactions)

association_rules =get_association(itemset,min_support,min_confidence,transactions)

print(association_rules)