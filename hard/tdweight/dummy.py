import csv

def read_csv(file_path):
    with open(file_path,'r') as file:
        headers = file.readline().strip().split(',')
        columns =[]
        for i in range(0,len(headers)):
            if i!=0:
                columns.append(headers[i])
     
        companies =[]
        values =[]
        for row in file:
            
            items =row.strip().split(',')
            companies.append(items[0])
            ans =[]
            for i,value in enumerate(items):
                if i!=0:
                    ans.append(float(value))
            values.append(ans)
        return companies,columns,values

def calculate_totals(values):
    row_totals=[]
    for i in values:
        row_totals.append(sum(i))
    col_totals=[]
    for i in zip(*values):
        col_totals.append(sum(i))
    
    grand_total=sum(row_totals)
    return row_totals,col_totals,grand_total

def write_into_file(output_file,comapnies,columns,values,row_totals,col_totals,grand_total):
    with open(output_file,'w') as file:
        file.write(f"(company\product)")
        for i,items in enumerate(columns):
                  file.write(f"        {items}          ")
        file.write(f"        total     \n")
        file.write("        ")
        for i in range(0,len(columns)+1):
            file.write("        count t-w d-w       ")
        file.write("\n")

        for i,company in enumerate(comapnies):
            file.write(f"{company}")
            for j,product in enumerate(columns):
                t_weight = round((values[i][j]/row_totals[i])*100,2)
                d_weight =round((values[i][j]/col_totals[i])*100,2)
                file.write(f"       ({values[i][j]} {t_weight}% {d_weight}%)     ")
            t_weight =100.00
            d_weight=round((row_totals[i]/grand_total)*100,2)
            file.write(f"   {row_totals[i]} {t_weight}%  {d_weight}")
            file.write("\n")
        
        file.write("Total")
        for i,part in enumerate(comapnies):
            t_weight=round((col_totals[i]/grand_total)*100,2)
            d_weight=100
            file.write(f"   {col_totals[i]} {t_weight} {d_weight}      ")
        file.write(f"{grand_total} 100% 100%")

        file.write("/n")

    return 

input_file = 'C:/Users/nalaw/OneDrive/Desktop/dm/hard/tdweight/code.csv'
output_file = 'C:/Users/nalaw/OneDrive/Desktop/dm/hard/tdweight/output.txt'
comapnies,columns, values=read_csv(input_file)
row_totals,col_totals,grand_total =calculate_totals(values)
print(row_totals)
print(col_totals)

write_into_file(output_file,comapnies,columns,values,row_totals,col_totals,grand_total)
