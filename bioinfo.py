from Bio import SeqIO

file = "sequence.fasta"
for i in SeqIO.parse(file,'fasta'):
    protien_sequence = i.seq.translate()
    print(protien_sequence)