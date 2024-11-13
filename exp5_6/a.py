import csv
from itertools import chain, combinations


def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = []

        for row in reader:
            ans = set()
            for i, item in enumerate(row):
                if item and i != 0:  
                    ans.add(item.strip())
            data.append(ans)

    return data


def get_all_itemsets(items):
    itemsets = []
    for r in range(1, len(items) + 1):
        itemsets.extend(combinations(items, r))
    return list(itemsets)


def generate_all_possible_rules(itemsets):
    rules = []
    for itemset in itemsets:
        itemset = set(itemset)

        for r in range(1, len(itemset)):
            antecedents = combinations(itemset, r)
            for antecedent in antecedents:
                antecedent = set(antecedent)
                consequent = itemset - antecedent
                
                if antecedent and consequent:
                    rules.append((antecedent, consequent))
    return rules



file_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/exp5_6/code.csv'
transactions = read_csv(file_path)
all_items = set(chain.from_iterable(transactions))
all_itemsets = get_all_itemsets(all_items)
all_rules = generate_all_possible_rules(all_itemsets)

print("All possible association rules (brute-force):")
for antecedent, consequent in all_rules:
    print(f"Rule: {antecedent} -> {consequent}")

print(len(all_rules))