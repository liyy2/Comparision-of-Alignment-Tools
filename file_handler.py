import sys
import re
ret_list = []
time_list = []
length = sys.argv[1]
file_name = sys.argv[2]
file_name_1 = sys.argv[3]
with open(file_name,'r') as f:
    while True:
        to_be_processed = f.readline()
        if not to_be_processed:
            break;
        search_obj = re.search(r'(\d*)\s\+\s\d*\smapped',to_be_processed)
        if search_obj:
            ret_list.append(search_obj.group(1))
    ret_list = [int(item) for item in ret_list]
    bwa_rec = ret_list[0]/2000000
    bwa_pre = ret_list[0]/(ret_list[0]+ret_list[1])
    bowtie2_rec = ret_list[2]/2000000
    bowtie2_pre = ret_list[2]/(ret_list[3]+ret_list[2])
    bowtie_rec = ret_list[4]/2000000
    bowtie_pre = ret_list[4]/ret_list[4]+ret_list[5]
    subread_rec = ret_list[6]/2000000
    subread_pre = ret_list[6]/(ret_list[6]+ret_list[7])
with open(file_name_1,'r') as f_1:
    while True:
        to_be_processed_1 = f_1.readline()
        if not to_be_processed_1:
            break;
        search_obj_1 = re.search(r'^real\s(.*)$',to_be_processed_1)
        if search_obj_1:
            time_list.append(search_obj_1.group(1))
with open('report','w') as f2:
    f2.write("Report\n")
    f2.write("Read length {0}\n".format(length))
    f2.write("Bwa precision {0}, recall {1}\n".format(bwa_pre,bwa_rec))
    f2.write("Time: "+"Good data "+time_list[2]+" bad data "+time_list[3]+"\n")
    f2.write("Bowtie2 precision {0}, recall {1}\n".format(bowtie2_pre,bowtie2_rec))
    f2.write("Time: "+"Good data "+time_list[4]+" bad data "+time_list[5]+"\n")
    f2.write("Bowtie precision {0}, recall {1}\n".format(bowtie_pre,bowtie_rec))
    f2.write("Time: "+"Good data "+time_list[6]+" bad data "+time_list[7]+"\n")
    f2.write("Subread precision {0}, recall {1}\n".format(subread_pre,subread_rec))
    f2.write("Time: "+"Good data "+time_list[8]+" bad data "+time_list[9]+"\n")
