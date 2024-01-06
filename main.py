import csv

data = open("../example.csv", encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines[10][3])
for line in data_lines[:5]:
    print(line)

all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])

print(all_emails)

file_to_output = open("to_save_file.csv",mode="w",newline="")
csv_writer = csv.writer(file_to_output, delimiter=",")
csv_writer.writerow(["a","b","c"])
csv_writer.writerows([["1","2","3"], ["4","5","6"]])
file_to_output.close()

f = open("to_save_file.csv", mode="a",newline="")
csv_writer = csv.writer(f)
(csv_writer.writerows(["1","2","3"]))