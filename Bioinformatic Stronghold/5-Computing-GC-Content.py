#!/usr/bin/env python
import sys
from operator import itemgetter

def main(*args):
    dna_data = {}
    current_fasta = ''
    gc_percentages = []
    with open(args[1]) as dataset:
        for line in dataset:
            if line[0] == '>':
                current_fasta = line[1:].strip('\n')
                dna_data[current_fasta] = ''
            else:
                dna_data[current_fasta] += line.strip('\n')
    for fasta_name, dna_string in dna_data.iteritems():
        gc_occurences = 0
        for i in dna_string:
            if any([i == 'G', i == 'C']):
                gc_occurences += 1
        gc_percentages.append([fasta_name, 100 * (float(gc_occurences) / float(len(dna_string)))])
        sorted_gc = sorted(gc_percentages, key=itemgetter(1), reverse=True)
    print sorted_gc[0][0]
    print sorted_gc[0][1]

main(*sys.argv)