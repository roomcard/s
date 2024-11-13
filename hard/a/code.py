from itertools import chain, combinations


transactions = [
    {'A', 'B'},
    {'A'},
    {'B'},
    {'A', 'B'},
    {'A', 'B'}
]


all_items = set(chain.from_iterable(transactions))


def get_all_itemsets(items):
    return list(chain.from_iterable(combinations(items, r) for r in range(1, len(items) + 1)))

all_itemsets = get_all_itemsets(all_items)


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


all_rules = generate_all_possible_rules(all_itemsets)


print("All possible association rules (brute-force):")
for antecedent, consequent in all_rules:
    print(f"Rule: {antecedent} -> {consequent}")

print(len(all_rules))
