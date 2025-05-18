import csv

def csv_write(data,filename):
    with open(filename, 'w', newline='') as f:
        write = csv.writer(f)
        for sublist in data:
            write.writerow(sublist)
    print("Sauvegarde effectuer!")
    f.close()

def csv_read(filename):
    data = []
    with open(filename, newline='') as f:
        read = csv.reader(f)
        for row in read:
            temp = []
            for e in row:
                temp.append(int(e))
            data.append(temp)
    f.close()
    return data
