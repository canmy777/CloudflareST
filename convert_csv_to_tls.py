import csv
import sys

def convert_csv_to_tls(csv_filename, output_filename):
    with open(csv_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        next(reader)  # 跳过标题行（如果有的话）
        for row in reader:
            ip = row[0]
            outfile.write(ip + '\n')

if __name__ == "__main__":
    csv_filename = 'result.csv'
    output_filename = 'notls.txt' if len(sys.argv) > 1 and sys.argv[1] == 'notls' else 'TLS.txt'
    convert_csv_to_tls(csv_filename, output_filename)