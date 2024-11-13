import csv

with open('C:/Users/nalaw/OneDrive/Desktop/dm/experiment11/output.txt', 'w') as output_file:
    
    def read_csv(file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data

    def calculate_gini(attribute, target_attribute, data):

        output_file.write(f"<----------------calculating gini index for {attribute}------------>\n")

        val_frequency = {}

        for row in data:
            if row[attribute] in val_frequency:
                val_frequency[row[attribute]] += 1
            else:
                val_frequency[row[attribute]] = 1
        
        gini = 0.0
        for item, count in val_frequency.items():
            weighted_probability = count / len(data)

            output_file.write(f"probability for {item} in the data is {count}/{len(data)}\n")

            subset = [row for row in data if row[attribute] == item]
            subset_gini = 1.0

            unique_count = {}
            for sub in subset:
                if sub[target_attribute] in unique_count:
                    unique_count[sub[target_attribute]] += 1
                else:
                    unique_count[sub[target_attribute]] = 1
                
            for itemss, count in unique_count.items():
                
                prob = round(count / len(subset),2)
                output_file.write(f"P({itemss}/{item}) is {prob}\n")
                subset_gini -= prob ** 2
                
            gini += weighted_probability * subset_gini

        return gini

    file_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/experiment11/code.csv'
    target_attribute = 'play'

    data = read_csv(file_path)
    features = [feature for feature in data[0].keys() if feature != target_attribute]

    for feature in features:
        gini = calculate_gini(feature, target_attribute, data)
        
        output_file.write(f"Gini index for {feature}: {gini}\n")

    print("Gini index values written to output.txt")
