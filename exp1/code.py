import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)        
        data = []
        for row in reader:
            data.append(float(row[0]))
    return header, data 

def write_csv(output_file, data):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for val in data:
            writer.writerow([val])  

def min_max(data):
    print("original data ", data)

    min_value = min(data)
    max_value = max(data)

    new_min = int(input("Enter new minimum value: "))
    new_max = int(input("Enter new maximum value: "))

    normalized_data = []

    for value in data:
        val = round(((value - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min, 2)
        normalized_data.append(val)
    
    return normalized_data

def z_score(data):
    mean_data = sum(data) / len(data)
    variance = sum((value - mean_data) ** 2 for value in data)
    stddev = (variance / len(data)) ** 0.5

    normalized_data = []
    for value in data:
        val = round((value - mean_data) / stddev, 2)
        normalized_data.append(val)
    return normalized_data


file_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/exp1/code.csv'
output_min_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/exp1/min.csv'
output_z_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/exp1/z.csv'

header, data = read_csv(file_path)

print("Min-Max normalization for header:", header[0])
min_max_data = min_max(data)
write_csv(output_min_path, min_max_data)

print("Z-Score normalization for header:", header[0])
z_score_data = z_score(data)
write_csv(output_z_path, z_score_data)