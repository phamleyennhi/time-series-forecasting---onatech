import csv

with open('Ventas_csv_file.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # sales_BAVIERA_X_1 = 0
    # sales_CCAPRESSE = 0
    for row in csv_reader:
        if line_count == 0:
            print(row[0], row[5])
            line = [row[0], row[5]]
            with open('item1.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(line)
            line_count += 1
        else:
            if (row[2] == "C. CAPRESSE"):
                print(row[0], row[5])
                line = [row[0], row[5]]
                with open('item1.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(line)
            # print(row[0], row[2], row[5])
            line_count += 1

    # print("C. CAPRESSE", sales_CCAPRESSE)
    # print("BAVIERA X 1", sales_BAVIERA_X_1)


