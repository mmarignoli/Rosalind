#!/usr/bin/env python
dataset = 'TGTGGTTGAACCGTACCCGGTGCAGCGCGTTTGTGAAACCCCAAAAATGAATTCCACTTACCTCCTCGAGAGGTTGTAAGGATCCTGTTATTACTCTGATTAAATGTTGAATGTCAAAAGAACTGGATTGATTAATATATCCCTTCGGTGGTTTCACGGCACCCGACTGGAGAGTAGCAGGGTTTTCCAATAGCGACCAATTTGTAGAAGAGGTACGTTACTCTCATGACTCATGGCGCGAGAAGAGGACCGCTCTCATGTCTTACGCCGCAGCTTGAGCCTCCTATACGAGCAGACCAGTGAGGTTACATATTTACGCGTAAGACATTCGCCATATTTCGTTGGATAAGACACTAGAATTACAAGCCGGAATTCCCGCATGGATTGTTTTCGGGCCGCAAGTTAGAGGGCCGGAGCGTACACTAGCGCGGAGTCTCGGCTCCAACCAGCTTGCTTACGACGTTGTTCGATTCAGGAGGTTACACTATAACGCCATCGATGGAAACGAAATTGAAAACACTCATCGCAGATTTATCACTACCCTTGTTTAACACGGTCCTACTATTTTAAATAGCCAGCTTCAGAAGTTGGCAACCGACGAAATGGTGTCGAACAAAAGGGTAATCCGTACCTGACGCCACCCGCACGGTACATGCGGGTATGTTATTTCCTAATGTGCGCCGGCGTAAAGGGTGAGTAAATAGATCGGCCAAACCCCGTGCTATTACTCGGGACTACGTACCCTCGAAGGACTTCACAGATCCATTGGTCGCTTACCACGATGGCCTCTGATATTTGCTCTTAGAGGCGGAATTTAGAAAGTCGTAATGGGGATTTATTCTGGGAAGTAGGTTAGGCTCTTGTTCCTATTAGAGAAGTTATCCACTCCTAGGGTCCTAGGAGGAGCCCGTGTAGTTAGGCCCACTAAACAGCCGCTCCGGCCT'
converted = ''
for i in dataset:
    if i == 'T':
        converted += 'U'
    else:
        converted += i

print converted