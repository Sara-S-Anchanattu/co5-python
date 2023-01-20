import csv
csv_string="""1,2,3
           4,5,6
           7,8,9"""
print("original string:")
print(csv_string)
lines=csv_string.splitlines()
print("list of csv formatted strings:")
print(lines)
reader=csv.reader(lines)
parsed_csv=list(reader)
print("/n list representation of the csv file:")
print(parsed_csv)