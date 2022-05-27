###FASTA reader, maybe make gc_content into class method?

with open("rosalind_gc (1).txt", "r") as f:
    name_and_seq = {}
    info = f.readlines()
    name_indices = []

    for i in range(len(info)):
        info[i] = info[i].rstrip()
        if info[i][0] == ">":
            name_indices.append(i)

    name_indices.append(len(info))
    
    #create dictionary with key = Taxon, value = sequence
    for index in name_indices[:-1]:
        if index == name_indices[-2]:
            name_and_seq[info[index].replace(">","")] = "".join(info[index + 1:name_indices[-1]])
        else:
            name_and_seq[info[index].replace(">","")] = "".join(info[index + 1: name_indices[name_indices.index(index) + 1]])
    
    gc = []

    for seq in name_and_seq.values():
        seq_length = len(seq)
        gc_content = 0
        for base in seq:
            if base == "G" or base == "C":
                gc_content += 1

        gc.append(100 * gc_content / len(seq))

#print out name of sequence with max GC and the amount (in percent)
print(list(name_and_seq.keys())[gc.index(max(gc))], "\n" + str(max(gc)))
