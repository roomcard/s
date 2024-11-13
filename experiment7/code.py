import csv


def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row:
              data.append(row)
    return data

def pearson_correlation(x,y):
    n=len(x)
    mean_x=sum(x)/len(x)
    mean_y=sum(y)/len(y)

    numerator=0.0
    for i in range(0,len(x)):
        numerator+=((x[i]-mean_x)*(y[i]-mean_y))
    den_x =0.0
    for i in range(len(x)):
        den_x+=(x[i]-mean_x)**2
    den_y=0.0
    for i in range(len(y)):
        den_y+=(y[i]-mean_y)**2
    
    den=(den_x*den_y)**0.5

    if den==0:
        return 0
    return numerator/den
    
    

file_name = 'C:/Users/nalaw/OneDrive/Desktop/dm/experiment7/code.csv'
data = read_csv(file_name)


attribute_x = input("Enter the first attribute (e.g., 'column1'): ")
attribute_y = input("Enter the second attribute (e.g., 'column2'): ")

x= []
for row in data:
    x.append(float(row[attribute_x]))

y = [float(row[attribute_y]) for row in data]

correlation = pearson_correlation(x, y)

print(f"Pearson Correlation Coefficient between {attribute_x} and {attribute_y}: {correlation}")
