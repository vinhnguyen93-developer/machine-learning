
import csv

input_file = r"./data/letters_CG.txt"
output_file = r"./data/letters_CG.csv"

in_txt = csv.reader(open(input_file, 'r'), delimiter = ' ')
out_csv = csv.writer(open(output_file, 'w'))

out_csv.writerows(in_txt)

del out_csv



