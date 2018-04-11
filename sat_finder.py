"""
This finds the most probably satellite subfamily for each
read in a fasta file
"""
from file_loading import *
from utils import *
from classify import *
import numpy as np
import matplotlib.pyplot as plt

def sat_finder(name):
    print("calculating distribution for "+name)
    #load and process files
    subfamilies = load_subfamilies("subfamilies.txt")
    mers = load_mers("24mers.txt")
    probs = get_probs(mers,subfamilies)
    reads = load_reads(name+".sat")
    lookup = subfamilies.keys()

    #classify each read
    num = np.zeros(15)
    prob_list = []
    all_list = []
    len_list = []
    len_sub =[]
    len_uncat = []
    for i in range(14):
        prob_list += [[]]
    unclassified = 0
    i = 0
    for read in reads:
        pred = classify(read.seq,probs)
        if pred[0] != 0.071428571428571425:
            i = np.argmax(pred)
            num[i] += 1
            prob_list[i] += [pred[i]]
            all_list += [pred[i]]
            length = float(len(read.seq)-read.seq.count('N'))/len(read.seq)
            len_sub += [length]
            len_list += [length]
        else:
            num[14] += 1
            all_list += [pred[0]]
            length = float(len(read.seq)-read.seq.count('N'))/len(read.seq)
            len_uncat += [length]
            len_list += [length]
        i += 1
    lookup += ["Unclassified"]

    plt.scatter(len_list, all_list,s=[.1]*len(all_list),c=np.random.rand(len(all_list)))
    plt.xlabel('Fraction of read that is repetitive')
    plt.ylabel('Confidence in subfamily prediction')
    plt.show()
    plt.hist([len_uncat,len_sub],10,(0,1),stacked=True)
    plt.xlabel('Fraction of read that is repetitive')
    plt.ylabel('Number of reads')
    plt.show()

    #plt.figure(figsize=(20,12))
    #for i in range(14):
    #    prob_list[i]
    #    plt.subplot(3,5,i+1)
    #    plt.hist(np.nan_to_num(prob_list[i]),100,(0,1))
    #    plt.title(lookup[i])
    #plt.savefig("Confidence_"+name)

    return num
