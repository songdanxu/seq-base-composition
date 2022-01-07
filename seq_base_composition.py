'''
Auther:Qi Guangyuan
Data:2022-1-6
Contact:qiguangyuan0406@163.com
Calculate overall base composition and (A+T) or (C+G) of a sequence.
Example: python seq_base_composition.py --input 1.fas --output 1.txt
'''
import argparse
from Bio import SeqIO

parse = argparse.ArgumentParser(description='Input and output file path.')

parse.add_argument('--input', '-i', help='The input file path.')
parse.add_argument('--output', '-o', help='The output file path.')
args = parse.parse_args()

for seq_infor in SeqIO.parse(args.input, "fasta"):
    id = seq_infor.id
    my_seq = seq_infor.seq
    lenth = len(seq_infor)
a = 100 * my_seq.count("A") / lenth
t = 100 * my_seq.count("T") / lenth
c = 100 * my_seq.count("C") / lenth
g = 100 * my_seq.count("G") / lenth
_at = 100 * float(my_seq.count("A") + my_seq.count("T")) / lenth
_cg = 100 * float(my_seq.count("C") + my_seq.count("G")) / lenth
print(f"A:{a}%\n"
      f"T:{t}%\n"
      f"C:{c}%\n"
      f"G:{g}%\n"
      f"A+T bias:{_at}%\n"
      f"C+G bias:{_cg}%")
with open(args.output, 'w') as f:
    f.write(f"A:{a}%\n"
            f"T:{t}%\n"
            f"C:{c}%\n"
            f"G:{g}%\n"
            f"A+T bias:{_at}%\n"
            f"C+G bias:{_cg}%")
