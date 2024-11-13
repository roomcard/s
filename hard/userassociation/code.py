import csv

def read_csv(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a = set()
            for item in row:
                if item.strip():  
                    a.add(item.strip())  # Add the item to the set
            transactions.append(a)
    return transactions

def calculate_support(itemset, transactions):
    itemset = set(itemset)
    count = sum(1 for transaction in transactions if itemset.issubset(transaction))
   
    return count / len(transactions)

def calculate_confidence(antecedent, consequent, transactions):
    antecedent = set(antecedent)
    consequent = set(consequent)
    support_ab = calculate_support(antecedent.union(consequent), transactions)
    support_a = calculate_support(antecedent, transactions)
    if support_a > 0:
        return support_ab / support_a
    else:
        return 0

def association_rule_mining(file_path):
    transactions = read_csv(file_path)
    antecedent_input = input("Enter the antecedent (comma-separated items): ").split(',')
    consequent_input = input("Enter the consequent (comma-separated items): ").split(',')
    support = calculate_support(antecedent_input + consequent_input, transactions)
    confidence = calculate_confidence(antecedent_input, consequent_input, transactions)
    print(f"Support for the rule {antecedent_input} -> {consequent_input}: {support * 100:.2f}%")
    print(f"Confidence for the rule {antecedent_input} -> {consequent_input}: {confidence * 100:.2f}%")

file_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/exp5_6/code.csv'
association_rule_mining(file_path)
