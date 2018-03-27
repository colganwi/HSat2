"""
This finds the most probably satellite subfamily for each
read in a fasta file
"""
from file_loading import *
from utils import *
from classify import *
import numpy as np
import matplotlib.pyplot as plt

name = "CHR1_11321M"
#load and process files
subfamilies = load_subfamilies("subfamilies.txt")
mers = load_mers("24mers.txt")
probs = get_probs(mers,subfamilies)
reads = load_reads(name+".sat")
lookup = subfamilies.keys()

#classify each read
num = np.zeros(14)
prob_list = []
for i in range(14):
    prob_list += [[]]

for read in reads:
    pred = classify(read.seq,probs)
    i = np.argmax(pred)
    num[i] += 1
    prob_list[i] += [pred[i]]

for i in range(14):
    print(lookup[i]+ ": " +str(num[i]))
    plt.figure(i)
    prob_list[i]
    plt.hist(np.nan_to_num(prob_list[i]),100)
    plt.title("Confidence "+name+" "+lookup[i])
    plt.show()
