#https://realpython.com/introduction-to-python-generators/
#D:\\odLIve\\OneDrive\\Documents\\createFirstApp\\OlympicsData_seed.csv
#C:\\Users\\haroldk\\Downloads\\techcrunch.csv
#use double \ to handle this error:
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
#https://sebhastian.com/syntaxerror-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-truncated-escape/

def csv_reader(file_name):
    file=open(file_name)
    result=file.read().split("\n")
    return result
    for row in open(file_name,"r"):
        yield row

myfile="C:\\Users\\haroldk\\Downloads\\techcrunch.csv"
data = csv_reader(myfile)
print(data)


csv_gen = csv_reader(myfile)
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")

