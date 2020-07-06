import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

#read in the ITEM ID and description
description = pd.read_csv(r'C:\Users\960060\Documents\CF\items_design_v1\input_data\MTL_SYSTEM_ITEMS_B.csv', low_memory = False, encoding='ISO-8859-1')
#drop nas
description = description.dropna()

def closest_full_match(word,word_list):
    """this function returns full word matches when given a word and a list"""

    #initiate list
    closest_full_match = []

    for i in range(len(word_list)):
        if fuzz.ratio(word,word_list.iloc[i]) > 90:
            #looking at full match
            closest_full_match.append(str(description["ITEM_ID"].iloc[i]) + "-" + str(word_list.iloc[i]))

    return closest_full_match

description["nearest"]=""

for i in range(len(description["description"])):
    print(i)
    description["nearest"].iloc[i] = closest_full_match(description["description"].iloc[i],description["description"])

def seperate_string_number(string):
    previous_character = string[0]
    groups = []
    newword = string[0]
    for x, i in enumerate(string[1:]):
        if i.isalpha() and previous_character.isalpha():
            newword += i
        elif i.isnumeric() and previous_character.isnumeric():
            newword += i
        else:
            groups.append(newword)
            newword = i

        previous_character = i

        if x == len(string) - 2:
            groups.append(newword)
            newword = ''
    return groups

description_cleansed = pd.read_csv(r'C:\Users\960060\Documents\CF\items_design_v1\desc_clean.csv', low_memory = False, encoding = 'ISO-8859-1')

description_cleansed["new_split"]

"""unpivot"""

# how many items are there in the dataframe
dummy["number of nearest"] = dummy.nearest.map(len)

# how many rows do we need?
rows_unpivot = dummy["number of nearest"].sum()

# create empty dataframe
dummy_unpivot = pd.DataFrame(columns=["invalid descriptions", "nearest"], index=[i for i in range(rows_unpivot)])

# create "invalid descriptions" unpivot
unpiv_col = []

# unpivot "invalid descriptions" data
for i in range(len(dummy.nearest)):
    for j in range(len(dummy["nearest"].iloc[i])):
        unpiv_col.append(dummy["invalid descriptions"].iloc[i])

# add into empty dataframe
dummy_unpivot.loc[:, "invalid descriptions"] = unpiv_col

# unpivot "nearest"
unpiv_col_n = []

for i in range(len(dummy.nearest)):
    for j in range(len(dummy["nearest"].iloc[i])):
        unpiv_col_n.append(dummy["nearest"].iloc[i][j])

# add into empty dataframe
dummy_unpivot.loc[:, "nearest"] = unpiv_col_n


""""""""""""""""""""""""


# how many items are there in the dataframe
description["number of nearest"] = description.nearest.map(len)

# how many rows do we need?
rows_unpivot = description["number of nearest"].sum()

# create empty dataframe
dummy_unpivot = pd.DataFrame(columns=["description","ITEM_ID", "nearest"], index=[i for i in range(rows_unpivot)])

# create "invalid descriptions" unpivot
unpiv_col = []
unpiv_col1 = []

# unpivot "invalid descriptions" data
for i in range(len(description.nearest)):
    for j in range(len(description["nearest"].iloc[i])):
        unpiv_col.append(description["description"].iloc[i])
        unpiv_col1.append(description["ITEM_ID"].iloc[i])

# add into empty dataframe
dummy_unpivot.loc[:, "description"] = unpiv_col
dummy_unpivot.loc[:, "ITEM_ID"] = unpiv_col1

# unpivot "nearest"
unpiv_col_n = []

for i in range(len(description.nearest)):
    for j in range(len(description["nearest"].iloc[i])):
        unpiv_col_n.append(description["nearest"].iloc[i][j])

# add into empty dataframe
dummy_unpivot.loc[:, "nearest"] = unpiv_col_n