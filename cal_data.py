import csv
import re
from sys import argv

def main():
    output = list()
    file_dict = dict()
    file_name = argv[1]
    with open('output_info','r') as f:
        reader = csv.reader(f)
        for row in reader:
            file_dict[tuple(row[:-1])] = row[-1]

    with open(file_name+'.csv','r') as f:
        reader = list(csv.reader(f))
        output.append(reader[0])
        for row in reader[1:]:
            key = tuple(row[3:-1])
            with open('data/'+file_dict[key],'r') as f:
                data = f.read()
                result = re.findall(r'\d*\.\d*\sMbits/sec                  receiver', data)
                value = result[0].split()[0]
                output.append(row[:-1]+[value])
    with open(file_name +'_mininet.csv','w') as f:
        writer = csv.writer(f)
        writer.writerows(output)


if __name__ == '__main__':
    main()