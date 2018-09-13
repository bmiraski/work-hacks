import csv
import sys


def createQBList(file):
    entries = []
    data = open(file, newline='')
    qb_data = csv.reader(data)
    row_idx = 0
    for row in qb_data:
        if row_idx == 0:
            row_idx += 1
            continue
        else:
            credit = '0'
            if row[7] != "":
                credit = row[7]
            entries.append((row[1], row[3], row[6], credit))
    data.close
    return entries


def createBWList(file):
    entries = []
    data = open(file, newline='')
    qb_data = csv.reader(data)
    row_idx = 0
    for row in qb_data:
        if row_idx == 0:
            row_idx += 1
            continue
        elif row_idx == 1:
            row_idx +=1
            continue
        else:
            entries.append((row[2], row[10], row[7], row[8]))
    data.close
    return entries



reader_qb = createQBList(sys.argv[1])
reader_bw = createBWList(sys.argv[2])

xi = 0
yi = 0

exceptions_qb = []

while True:
    if yi >= len(reader_bw):  # Same again, but swap roles
        exceptions_qb.append(reader_qb[xi])
        xi += 1
        yi = 0

    if xi >= len(reader_qb):  # If xs list is finished,
        break       # And we're done.

    # Both lists still have items, compare item to result.
    if reader_qb[xi] == reader_bw[yi]:
        xi += 1
        yi = 0

    else:
        yi += 1

print(exceptions_qb)

xi = 0
yi = 0

exceptions_bw = []

while True:
    if xi >= len(reader_qb):  # If xs list is finished,
        exceptions_bw.append(reader_bw[yi])
        xi = 0
        yi += 1

    if yi >= len(reader_bw):  # Same again, but swap roles
        break

    # Both lists still have items, compare item to result.
    if reader_qb[xi] == reader_bw[yi]:
        xi += 0
        yi += 1

    else:
        xi += 1

print(exceptions_bw)

if len(exceptions_qb) == len(exceptions_bw) == 0:
    print("No Exceptions found")
else:
    with open('exceptions.txt', 'w') as output:
        output.write("Entries from Quickbooks missing: \n")
        for item in exceptions_qb:
            output.write(str(item) + '\n')
        output.write("\n")
        output.write("Entries from BrokerWolf missing: \n")
        for item in exceptions_bw:
            output.write(str(item) + '\n')






#exceptions = []
#for row in reader_qb:
#    match = False
#    while not match:
#        for row_bw in reader_bw:
#            if row['Date'] != row_bw['trandate']:
#                print('.')
#            else:
##                if row['Name'] != row_bw['note']:
#                    print('.')
#                else:
#                    print("Matching Name / note found")
###                    else:
#                        print('Matching debit entry found.')
#                        print(f"Full matching entry found for {row['Date']}")
#                        break
#        print('No matching entry found')
#        exception_entry = (row['Date'], row['Debit'])
#        exceptions.append(exception_entry)
#        break
#print("The following entries were not found:")
#if len(exceptions) == 0:
#    print("There are no exceptions")
# else:
#    print(exceptions)


# for row in reader_qb:
#    print(row['Date'], row['Name'], row['Debit'])
# for row in reader_bw:
#    print(row['trandate'], row['note'], row['debit'])
