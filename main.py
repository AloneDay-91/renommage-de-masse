import csv

with open("Classeur1.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        sortedlist = sorted(reader, reverse=False)
        print(', '.join(row), sortedlist)
        with open('main.csv', 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(sortedlist)
            f.close()