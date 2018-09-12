import csv
import sys

with open('MuseQB.csv', newline='') as qb:
    with open('GL65150.csv', newline='') as bw:
        reader_qb = csv.DictReader(qb)
        reader_bw = csv.DictReader(bw)
        exceptions=[]
        for row in reader_qb:
            print(f"Attempting to find match for date {row['Date']}")
            match = False
            for row_bw in reader_bw:
                if row['Date'] != row_bw['trandate']:
                    print('.')
                else:
                    print(f"Matching Date found for {row['Date']}")
                    if row['Name'] != row_bw['note']:
                        print('.')
                    else:
                        print("Matching Name / note found")
                        if row['Debit'] != row_bw['debit']:
                            print('.')
                        else:
                            print('Matching debit entry found.')
                            match = True
                            break
            if not match:
                print('No matching entry found')
                exception_entry = (row['Date'], row['Debit'])
                exceptions.append(exception_entry)
            else:
                print(f"Full matching entry found for {row['Date']}")
        print("The following entries were not found:")
        if len(exceptions) == 0:
            print("There are no exceptions")
        else:
            print(exceptions)


#for row in reader_qb:
#    print(row['Date'], row['Name'], row['Debit'])
#for row in reader_bw:
#    print(row['trandate'], row['note'], row['debit'])
