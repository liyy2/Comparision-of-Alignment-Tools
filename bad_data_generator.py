import random
def random_sequence(seq_len):
    ret_seq = ''
    my_dic = {0:'A',1:'T',2:'G',3:'C'}
    for i in range(seq_len):
        ret_seq += my_dic[random.randint(0,3)]
    return ret_seq

def fa_generator(file_name,n,seq_len): # n is the number of sequence
    with open(file_name,'w+') as f:
        for i in range(n):
            ret_seq = random_sequence(seq_len)
            starting_index = random.randint(1,1000000000000) # randomly simulate a starting index
            f.write ('>{0}::chr{1}:{2}:{3}\n'.format(i+1, random.randint(1,50), starting_index, starting_index+seq_len))
            f.write(ret_seq+'\n')    