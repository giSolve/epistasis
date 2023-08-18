#!/usr/bin/env python3
import numpy as np

index_to_base = {0: 'A', 1: 'C', 2: 'U', 3: 'G'}
base_to_number={'A':0, 'C':1, 'U':2, 'G':3, 'T':2}
db_to_bin = {'.': '00', '(': '10', ')': '01', '_': '00', '[': '10', ']': '01'}


def sequence_to_structure(seq, GPmap):
   return get_dotbracket_from_int(GPmap[sequence_str_to_int(seq)])

def sequence_str_to_int(sequence):
   """convert between sequence representations:
   from biological four-letter string to a tuple of integers from 0-3;
   motive: these integers can be used as array tuples"""
   return tuple([base_to_number[b] for b in sequence])

def get_dotbracket_from_int(structure_int):
   """ retrieve the full dotbracket string from the integer representation"""
   dotbracketstring = ''
   bin_to_db = {'10': '(', '00': '.', '01': ')'}
   structure_bin = bin(structure_int)[3:] # cut away '0b' and the starting 1
   assert len(structure_bin) % 2 == 0
   for indexpair in range(0, len(structure_bin), 2):
      dotbracketstring = dotbracketstring + bin_to_db[structure_bin[indexpair]+structure_bin[indexpair+1]]
   return dotbracketstring
##################################################################################################
##################################################################################################
print("RNA GP map: save data")
##################################################################################################
##################################################################################################

L = 13

#################################################
#print("load")
#################################################
GPmap = np.load('/Users/soli/Desktop/studienstiftung/leyin_2023/epistasis/GPmap_L'+str(L)+'mfe.npy')

#################################################
#print("now we can use the GP map")
#################################################
seq_test = ''.join([np.random.choice(['A', 'G', 'C', 'G']) for i in range(L)])
#print('this is how we can look up the structure for a sequence', seq_test, sequence_to_structure(seq_test, GPmap))