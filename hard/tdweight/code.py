def read_csv(input_file):
    with open(input_file, 'r') as f:
        # Read the header
        header = f.readline().strip().split(',')
        columns = header[1:] 
        
        # Read data
        companies = []
        values = []
        
        for line in f:
            parts = line.strip().split(',')
            company = parts[0]
            companies.append(company)
            row_values = list(map(int, parts[1:]))
            values.append(row_values)
    
    return companies, columns, values

def calculate_totals(values):
    row_totals = [sum(row) for row in values]
    col_totals = [sum(col) for col in zip(*values)]
    grand_total = sum(row_totals)
    return row_totals, col_totals, grand_total

def write_output(output_file, companies, columns, values, row_totals, col_totals, grand_total):
    with open(output_file, 'w') as f:
      
        f.write(" Column\\row  ")
        for col in columns:
            f.write(f",{col}, ,")
        f.write(", total \n")

        f.write("Count ")
        for i in range(len(columns)):
            f.write(",t-weight ,d-weight ")
            if i < len(columns) - 1:
                f.write(",Count ")
        f.write(",Count ,t-weight ,d-weight \n")

        # Write data rows
        for i, company in enumerate(companies):
            f.write(company)
            for j in range(len(columns)):
                t_weight = (values[i][j] * 100.0) / row_totals[i] if row_totals[i] != 0 else 0
                d_weight = (values[i][j] * 100.0) / col_totals[j] if col_totals[j] != 0 else 0
                f.write(f",{values[i][j]},{t_weight }% ,{d_weight}%")
            
            row_percentage = (row_totals[i] * 100.0) / grand_total if grand_total != 0 else 0
            f.write(f",{row_totals[i]},100%,{row_percentage:.2f}%\n")
        
        f.write("Total")
        for j in range(len(columns)):
            col_percentage = (col_totals[j] * 100.0) / grand_total if grand_total != 0 else 0
            f.write(f",{col_totals[j]},{col_percentage:}%,100%")
        
        f.write(f",{grand_total},100%,100%\n")

# File paths
input_file = 'C:/Users/nalaw/OneDrive/Desktop/dm/hard/tdweight/code.csv'
output_file = 'C:/Users/nalaw/OneDrive/Desktop/dm/hard/tdweight/outpu.txt'

# Process CSV data
companies, columns, values = read_csv(input_file)

# Calculate totals
row_totals, col_totals, grand_total = calculate_totals(values)

# Write output to file
write_output(output_file, companies, columns, values, row_totals, col_totals, grand_total)
