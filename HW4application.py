__author__ = 'Amras'
"""
Provide code and solution for Application 4
"""

DESKTOP = True

import math
import random
import urllib2
from HW4 import *
if DESKTOP:
    import matplotlib.pyplot as plt
else:
    import simpleplot


# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"



###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict




def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)

    # read in files as string
    words = word_file.read()

    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list

seq_x=read_protein(HUMAN_EYELESS_URL)
seq_y=read_protein(FRUITFLY_EYELESS_URL)
scoring_matrix=read_scoring_matrix(PAM50_URL)
align_matrix=compute_alignment_matrix(seq_x,seq_y,scoring_matrix,False)
problem_one=compute_local_alignment(seq_x,seq_y,scoring_matrix,align_matrix)
print problem_one

seq_1=problem_one[1]
seq_2=problem_one[2]
seq_1=seq_1.translate(None,'-')
seq_2=seq_2.translate(None,'-')
consesue_seq=read_protein(CONSENSUS_PAX_URL)

align_matrix_1=compute_alignment_matrix(seq_1,consesue_seq,scoring_matrix,True)
align_matrix_2=compute_alignment_matrix(seq_2,consesue_seq,scoring_matrix,True)
problem_two=compute_global_alignment(seq_1,consesue_seq,scoring_matrix,align_matrix_1)
problem_two_2=compute_global_alignment(seq_2,consesue_seq,scoring_matrix,align_matrix_2)


human_local=problem_two[1]
human_compare=problem_two[2]

fly_local=problem_two_2[1]
fly_compare=problem_two_2[2]
cout=0
for i in range(0,len(human_local)):
    if human_local[i] == human_compare[i]:
        cout+=1
percentage_1=float(cout)/float(len(human_local))
print percentage_1

cout=0
for i in range(0,len(fly_local)):
    if fly_local[i] == fly_compare[i]:
        cout+=1
percentage_2=float(cout)/float(len(fly_local))
print percentage_2


def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    scoring_distribution={}
    while num_trials != 0 :
        seq_y=list(seq_y)
        random.shuffle(seq_y)
        seq_y = ''.join(seq_y)
        align_matrix=compute_alignment_matrix(seq_x,seq_y,scoring_matrix,False)
        random_score=compute_local_alignment(seq_x,seq_y,scoring_matrix,align_matrix)
        random_score=random_score[0]
        if random_score not in scoring_distribution:
            scoring_distribution[random_score]=1
        else:
            scoring_distribution[random_score]+=1
        num_trials-=1
        print "the number of trail left is "+str(num_trials)
    return scoring_distribution

compute_distribution=generate_null_distribution(seq_x,seq_y,scoring_matrix,1000)

X_axis=[]
Y_axis=[]
for ele in compute_distribution:
    X_axis.append(ele)
    Y_axis.append(float(compute_distribution[ele])/1000.0)

plt.bar(X_axis,Y_axis)
plt.xlabel('Score distribution')
plt.ylabel('Percentage distribution')
plt.legend(['1000 trials'])
plt.title('distribution of the score')
plt.grid(True)
plt.savefig("test.png")
plt.show()

compute_mean=0;
for ele in compute_distribution:
    compute_mean+=ele*compute_distribution[ele]
compute_mean=float(compute_mean)/1000.0
print "The mean is "+str(compute_mean)
compute_divation=0.0;
for ele in compute_distribution:
    compute_divation+=(float(ele)-compute_mean)^2*float(compute_distribution[ele])

compute_divation=float(compute_divation)/1000.0;
compute_divation=math.sqrt(float(compute_divation))
print "the standard deviation is"+str(compute_divation)
score_local=problem_one[0]
print "the Z for the Question 5 is "
print (float(score_local)-float(compute_mean))/float(compute_divation)


word_list=read_words(WORD_LIST_URL)
alphabet='abcdefghijklmnopqrstuvwxyz'
scoring_matrix=build_scoring_matrix(alphabet,2,1,0)

####
def check_spelling(checked_word, dist, word_list):
    result_set=set([])
    for ele in word_list:
        align_matrix=compute_alignment_matrix(checked_word,ele,scoring_matrix,True);
        globe_alignment=compute_global_alignment(checked_word,ele,scoring_matrix,align_matrix)
        if len(checked_word)+len(ele) -globe_alignment[0] <= dist:
            result_set.add(ele)
    return result_set

a=check_spelling('humble',1,word_list)
print a
b=check_spelling('firefly',2,word_list)
print b

