#!/usr/bin/env python

string_1 = 'CGGAAGCAACAAGATGGGAGCACGCTTATTCGAGGCGGATGTCTCGTGTCGGGTTCGGATACCCGGGTACTTTAAATCCGATTGGTCACTCCGGCATTGGGTTGTTACGAGAACCGTACTGACTAGCAGCATCCTCAAGAAGTGAACCGCTGTGCCCCTACTGACAGCCCGTAGCATGCGTTGGTTGAGTCTCCTACGCAACGTACCCACGCAGTTTCCCGATGGCTAGAAACGCAGGGTGCCTCTTCTGAACTTGTGAATAAAATCTTGAATGCTAGACCAACGAAATCTGCCAATGCTTTAGCGCGCGGTGTGGGGTTATTACGTCACTCCCTTCCGCCCGAGTTCACGATTCATCGGGAGGGCATCACCTTTACTGTTTAATGGCATTTGTCAAGCAGGCCCAGTTGTCTCGCGGACTACCACTATTATTGTGCCGGACTGGCTCATATGGAGCCGACCGAATCTCAGCTTAAACGTCTACTTGCAGAAGAGGTGTATTCGCCGGCGCCTTCACCCACTGTGGTGCTACCCGGTGACGGTGTAAGAGATCTTGCCGCGCCTCTAAGGATTCAGTAGGGAAGGCGCTCACCGATGTGCCCAACGCTTGATGGGAGGGGTAAGATGATGTAAGATTATTAATGTCACTGGATGTATCGATCTGTCTGAGGTACCCGGCAGTAGCTCCTGCTCACCGCCAGATATTCACATATTGAGTTCCAAACGATCCTGTCAATGTAGACTATGCAGAACAGCGGCACAGGTGTGCTACGAAGGTCGGGTTCATTAAAAAGTAGAGGGTGGCCAAGTGACCGTAGGCCCGCTATGCTCCACCAGCAGCCACGACATGGTCTCCAGGCCCAACAGGGTGCCGGGACAGATAATATCCCGTGGCCAAGAGCAATCTTTTAGACCATTTGATCGGACTTTAATGTGCACACTGGTCCGTAGCACTATGG'
string_2 = 'CGGTAGCAGCAAGAACATATCGACAGCATAATCGGCGCACGTTGCGAGCCGATTTGTAAAGCCCGGGTTTCTTGGAGCCGGTTTACCATTATAATCGTGGAATTTAACGTCAACCGTAAAGAACTCCAGCAACCTTCTGACGTGCCCCGATTTGATCGTAGAGACACAGGTCAACGTCTGTGTCGCACGATTTCTACGCAACTTGGCAAACAAATGAGATGTGTGTGCTACCTCCGATGTTGCTTGTCTAAACGTTGGATTCGATCCTGGCCGGTTATGGTGACCCGACCTACAATCACATCTGGACCCGGTGTGGCACCTGCGCTTAAATCCTGTTGTACCGAGACAACGTACGATAGAAAGGTTTTCACTTTTATACGTTGCTTCCGTCTGTGAAGCACGGCAAGTCGCATCGAGGCCCTTGGCTATAAGTGTGACCGACCGGACAACGTGAGGCCGAGCGTAACTCAGATGTAAATTCTCAGGAAAGAATAGGTGCCATCCCGGTCGTCATGAACGTGTAAGGGGAATGCCGTCCAATGGTTATGAGCCCTGGGCGCGCCTCCAGTAATTGAGGGAGTAAAGGTCTGATCGATGTGACAAACGCTTGTTGCCGGGCGCTACATGAGGTTAGTAGATGAAGCTCTAATGAGCCCCCGAAGTGTGCGACTCATAGAGTGCCTGCTTCTGCCCTCGTCAAAAAAACCAGGGTTTAACTAGCAAGTAGTAGGTAGACGCTACAATAAGCATTGGACCGGGACGTGAGTGAAATAAGGCAAATGATCACTCAAATGTGTATGGTCGGCCATTGAGCTCTTCCTAGGGGTGTTGCATCAACGACCTCCCCATGGCCTCCTGACTCTGCATGGTCTCAGTACAGTGCAGTTCCTGGGGCCGTTGGCAATCTTCAGTCCACGACTCTAGCACATCAGAGGGCAGACTCACCTATGTTACTAAGA'

counter = 0
if len(string_1) == len(string_2):
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            counter += 1

print counter