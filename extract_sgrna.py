#!/usr/bin/env python
from __future__ import print_function
import sys
from Bio import SeqIO


def main():
    '''Extract the 20 bp sgRNA sequence from a longer seqeuence string'''
    if len(sys.argv) < 2:
        print('Usage: {} sequence.fa'.format(sys.argv[0]), file=sys.stdout)

    record = SeqIO.read(sys.argv[1], 'fasta')

    seed = 'GTTTTAGAGC'
    index = record.seq.find(seed)
    if index == -1:
        print('Not found!\n')
    else:
        extracted = record.seq[index - 20:index]
        print('{}: {}\n'.format(index, extracted))


if __name__ == '__main__':
    main()
