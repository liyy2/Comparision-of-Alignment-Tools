import re
import pandas as pd
import numpy as np
def readsam(filename):
    col1,col2,col3,col4,col5=[],[],[],[],[]
    with open(filename,'r') as f:
        while True:
            to_be_processed=f.readline()
            if not to_be_processed: # if the end of the file
                break
            if to_be_processed[0] == '@': # we only focus on lines that not start with @
                continue
            try:
                search_obj = re.search(r"^\d::(chr\d+):(.*)-(\d*)_[\w_:]*.*?[\s]+[\d]+[\d][\s]+(\*?\w*)[\s]+(\d*)",to_be_processed)   # regex
                col1.append(search_obj.group(1))
                col2.append(search_obj.group(2))
                col3.append(search_obj.group(3))
                col4.append(search_obj.group(4))
                col5.append(search_obj.group(5))
            except AttributeError:
                print(to_be_processed)

        col1 = pd.Series(col1)
        col2 = pd.Series(col2)
        col3 = pd.Series(col3)
        col4 = pd.Series(col4)
        col5 = pd.Series(col5)
    return pd.DataFrame({"sim_chr":col1,"sim_start":col2,"sim_end":col3,"ali_chr":col4,"ali_start":col5})