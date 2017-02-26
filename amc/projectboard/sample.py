import csv
i=0
with open('/home/sony/Desktop/als.csv') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
        print(row['name'])
        print(row['forenama'])