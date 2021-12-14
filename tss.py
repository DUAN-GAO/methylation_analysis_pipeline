import sys
import re
import shelve
in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file) as f,open(out_file,"w") as w:
    dicc = {}
    for i in f:
        chr_pos = i.split("\t")[2]
        length = len(range(int(i.split("\t")[4]),int(i.split("\t")[5])))
        gene = i.split("\t")[12]
        if chr_pos not in dicc.keys():
            dicc[chr_pos] = {}
        else:
            if gene not in dicc[chr_pos].keys():
                dicc[chr_pos][gene] = range(int(i.split("\t")[4]),int(i.split("\t")[5]))
            else:
                if len(dicc[chr_pos][gene]) < length:
                    dicc[chr_pos][gene] = range(int(i.split("\t")[4]),int(i.split("\t")[5]))
                else:
                    pass
    print(dicc)
    with shelve.open('ucsc') as db:
        db['ucsc'] = dicc 
