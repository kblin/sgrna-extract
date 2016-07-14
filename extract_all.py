#!/usr/bin/env python
from __future__ import print_function
import sys
from Bio import SeqIO


def main():
    '''Extract all 20 bp sgRNA sequences from a longer seqeuence string'''
    if len(sys.argv) < 2:
        print('Usage: {} sequence.fa'.format(sys.argv[0]), file=sys.stdout)

    record = SeqIO.read(sys.argv[1], 'fasta')

    seed = 'GTTTTAGAGC'

    printed = False
    index = record.seq.find(seed)

    while index > -1:
        extracted = record.seq[index - 20:index + 10]
        print('{}: {}'.format(index, extracted))
        printed = True
        index = record.seq.find(seed, index + 1)

    if not printed:
        print('Not found!')

    # end with a newline
    print('')

if __name__ == '__main__':
    main()
