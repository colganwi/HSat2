from Bio.Seq import Seq
from file_loading import *

name = "CHR1_11321M"
datafile = name+".2.7.7.80.10.50.50.dat"
seqfile = name


reads = load_reads(seqfile)
masks = []
satregions = None

with open(datafile,'r') as file:
   for line in file:
       line = line.strip('/n').split()
       if len(line) == 0:
           None
       elif line[0] == "Sequence:":
           if satregions != None and len(satregions) != 0:
               for i in reversed(range(1,len(satregions))):
                   if satregions[i][0] - satregions[i-1][1] <= 100:
                       region = (satregions[i-1][0],satregions[i][1])
                       del satregions[i]
                       satregions[i-1] = region
               seq = ''
               for i in range(len(read)):
                   masked = True
                   for region in satregions:
                       if i > region[0] and i < region[1]:
                           masked = False
                   if masked == True:
                       seq += 'N'
                   else:
                       seq += read[i]
               if direction < 0:
                   read._set_seq(Seq(str(seq)).reverse_complement())
               else:
                   read._set_seq(Seq(str(seq)))
               masks += [read]
           satregions = []
           direction = 0
           read = reads.next()
       elif len(line) == 15:
           if 'CATTC' in line[13]:
               satregions += [(int(line[0]),int(line[1]))]
               direction += 1
           if 'GAATG' in line[13]:
               satregions += [(int(line[0]),int(line[1]))]
               direction -= 1

SeqIO.write(masks, open(name+".sat",'w'), "fasta")
