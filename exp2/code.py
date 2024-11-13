import csv

file_path = 'C:/Users/nalaw/OneDrive/Desktop/dm_exp/binning/code.csv'

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = []
        for row in reader:
            if row:
                data.append(float(row[0]))
    return header, data

def divide_data_into_bins(data, no_of_bins):
    bin_size = len(data) // no_of_bins 
    if len(data) % no_of_bins != 0:
        bin_size += 1
    
    index = 0
    bins = {}
    count = 1
    while index < len(data):
        bin = []
        for j in range(bin_size):
            if index + j < len(data):
                bin.append(data[index + j])
        bins[count] = bin
        index += bin_size 
        count += 1
    
    return bins

def bin_by_mean(actual_bin_count, bins):
    ans = []
    for i in range(1, actual_bin_count + 1):
        bin = bins[i]
        mean = sum(bin) / len(bin)
        new_bin = [round(mean, 2)] * len(bin) 
        ans.append(new_bin)
    return ans

def bin_by_median(actual_bin_count, bins):
    ans = []
    for i in range(1, actual_bin_count + 1):
        bin = bins[i]
        n = len(bin)
        median = (bin[n // 2] + bin[n // 2 - 1]) / 2 if n % 2 == 0 else bin[n // 2]
        new_bin = [round(median, 2)] * len(bin)  
        ans.append(new_bin)
    return ans

def output_csv(output_file_path, bins_mean, bins_median):
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["bin by mean"])
        
        for i in range(0,len(bins_mean)):
            label =f"bin {i+1}"
            writer.writerow([label])
            writer.writerow(bins_mean[i])
        
        writer.writerow([])

        writer.writerow(["bin by median"])

    
        
        for i in range(0,len(bins_median)):
            label =f"bin {i+1}"
            writer.writerow([label])
            writer.writerow([bins_median[i]])
        

    
# Paths
file_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/exp2/code.csv'
output_file_path = 'C:/Users/nalaw/OneDrive/Desktop/dm/exp2/output.csv'

# Read CSV and get data
header, data = read_csv(file_path)

# Binning
print('We are binning the data into bins')
no_of_bins = int(input("Enter the number of bins: "))
bins = divide_data_into_bins(data, no_of_bins)

# Bin by mean and median
bins_mean = bin_by_mean(no_of_bins, bins)
bins_median = bin_by_median(no_of_bins, bins)

# Output to CSV
output_csv(output_file_path, bins_mean, bins_median)
