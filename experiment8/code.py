import csv

def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = []
        for row in reader:
            rows.append([float(value) for value in row])
    return header, rows

def five_number_summary(data):
    data = sorted(data)
    n = len(data)
    
    min_val = data[0]
    max_val = data[-1]
    
    if n % 2 == 0:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        median = data[n // 2]
    
    lower_half_array = data[:n // 2]
    upper_half_array = data[n // 2 + 1:] if n % 2 != 0 else data[n // 2:]

    if len(lower_half_array) % 2 == 0:
        q1 = (lower_half_array[len(lower_half_array) // 2 - 1] + lower_half_array[len(lower_half_array) // 2]) / 2
    else:
        q1 = lower_half_array[len(lower_half_array) // 2]

    if len(upper_half_array) % 2 == 0:
        q3 = (upper_half_array[len(upper_half_array) // 2 - 1] + upper_half_array[len(upper_half_array) // 2]) / 2
    else:
        q3 = upper_half_array[len(upper_half_array) // 2]

    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    if(lower_bound<0):
         lower_bound=0


    actual_min = min_val
    actual_max = max_val
    outliers = []

    for val in data:
        if val >= lower_bound and val <= upper_bound:
            if val < actual_max:
                actual_max = val
            if val > actual_min:
                actual_min = val
        else:
            outliers.append(val)

    print("Min:", min_val)
    print("Q1:", q1)
    print("Median:", median)
    print("Q3:", q3)
    print("Max:", max_val)
    print("Upper Bound:", upper_bound)
    print("Lower Bound:", lower_bound)
    print("Interquartile Range:", iqr)

    print("Outliers:", outliers)
    print()

def process_csv(file_path):
    header, rows = read_csv(file_path)
    columns = list(zip(*rows))

    for idx, col in enumerate(columns):
        print(f"Summary for Column '{header[idx]}':")
        five_number_summary(col)

input_file = 'C:/Users/nalaw/OneDrive/Desktop/Normalization/boxplot/boxplot.csv'
process_csv(input_file)
