#import sys 
import pandas as pd 

base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

def solution():
    """ Print solution for the sudoku"""
    for line in board:
        print(line)

board_pd = pd.DataFrame(board)

#Get rid of numbers 
Numbers_on_grid = 81
#Numbers_of_blanks = input('Number_of_blanks:')
Numbers_of_blanks = 45

Index = 0
samples = [(x,y) for x in range(9) for y in range(9)]
while (Numbers_on_grid >= 17 and Index < int(Numbers_of_blanks)):
    select = sample(samples,1)[0]
    samples.remove(select)
    board_pd.iloc[select] = 0
    Index = Index + 1
    Numbers_on_grid = Numbers_on_grid - 1

print('Index:',Index,'No. on grid',Numbers_on_grid)
print(board_pd.to_string(index=False))

###########################################################################
import numpy as np

#locate all the blanks
zero_row_loc , zero_col_loc = np.where(board_pd.values == 0)
zero_loc = list(zip(board_pd.index[zero_row_loc],board_pd.columns[zero_col_loc]))

#Create a dictionary with index as keys and possible values as dictionary value
pos_values = {}
for i in zero_loc:
    pos_values[i] = list(range(1,10))

#print(pos_values)
pos_index ={
    'first':[0,1,2],
    'second':[3,4,5],
    'third':[6,7,8]
    }
    
def check_3x3(loc):
    """
    Check within the square for invalid values
    """
    for values in pos_index:
        if loc[0] in pos_index[values]:
            square_row_index = pos_index[values]
        if loc[1] in pos_index[values]:
            square_col_index = pos_index[values]

    index_to_check = [(row,col) for row in square_row_index for col in square_col_index]
    #print('square_row_index:',square_row_index)
    #print('square_col_index:',square_col_index)
    #print('index_to_check:',index_to_check)
    
    invalid_num = []
    for index in index_to_check:
        value = board_pd.iloc[index]
        if value > 0:
            invalid_num.append(value)
        #print(invalid_num)
    #print(invalid_num)
    pos_values[loc] = list(set(pos_values[loc]) - set(invalid_num))

def check_row(loc):
    """
    Check the row for invalid values
    """    
    index_to_check = list(zip(tuple(np.repeat(loc[0],9)),tuple(range(9))))

    #print('index_to_check:',index_to_check)

    invalid_num = []
    for index in index_to_check:
        value = board_pd.iloc[index]
        if value > 0:
            invalid_num.append(value)
        #print(invalid_num)
    #print(invalid_num)
    pos_values[loc] = list(set(pos_values[loc]) - set(invalid_num))


def check_col(loc):
    """
    Check the col for invalid values
    """    
    index_to_check = list(zip(tuple(range(9)),tuple(np.repeat(loc[1],9))))

    #print('index_to_check:',index_to_check)

    invalid_num = []
    for index in index_to_check:
        value = board_pd.iloc[index]
        if value > 0:
            invalid_num.append(value)
        #print(invalid_num)
    #print(invalid_num)
    pos_values[loc] = list(set(pos_values[loc]) - set(invalid_num))

def run_checks():
    """ Run all three checks and remove from ps_value if theres a value for the missing square"""
    inserted = 0
    keys_to_remove = []
    for blanks in pos_values:
        #print('Check:',blanks)
        check_3x3(blanks)
        #print('check_3x3 complete')
        check_row(blanks)
        #print('check_row complete')
        check_col(blanks)
        #print('check_col complete')

        if len(pos_values[blanks]) == 1:
            board_pd.iloc[blanks] = int(pos_values[blanks][0])
            keys_to_remove.append(blanks)
            inserted += 1
            #print('Well Done you found one! :D')

    #print('Total Insert:',inserted)

    for keys in keys_to_remove:
        del pos_values[keys]


    return(inserted)

def solve():
    """ Solve the suduko"""
    prev_insert = 0
    num_of_runs = 0 
    while len(pos_values.keys()) > 0:
        insert = run_checks()
        if insert != 0:
            num_of_runs += 1
        else:
            print(board_pd)
            return (print("Sorry this solver is smart enough :( "),str(num_of_runs))
    print(board_pd)
    return(print("Congrats you solved in "+str(num_of_runs)+' steps'))
 
def check_3x3_adv(loc):
    """Check for unique candidates"""
    for values in pos_index:
        if loc[0] in pos_index[values]:
            square_row_index = pos_index[values]
        if loc[1] in pos_index[values]:
            square_col_index = pos_index[values]

    index_to_check = [(row,col) for row in square_row_index for col in square_col_index]

    #check which square is missing
    missing_squares = list(set(index_to_check) & set(pos_values.keys()))
    #print(missing_squares)

    #Get the possible values of the missing squares
    #Get freq of possible values 
    sub_dict = {k: pos_values[k] for k in pos_values.keys() & set(missing_squares)}
    
    val =[]
    for lists in sub_dict.values():
        for values in lists:
            val.append(values)

    freq = dict((x,val.count(x)) for x in set(val))   

    inserted = 0
    for key in freq.keys():
        if freq[key] == 1:
            for missing_square in missing_squares:
                if int(key) in pos_values[missing_square]:
                    inserted += 1
                    print("Found one at "+ str(missing_square))
                    board_pd.iloc[missing_square] = int(key)
                    del pos_values[missing_square]

    return(inserted)

def check_naked_subset(row):
    """ Find and remove naked subset"""
    #check the last row ((X,8))
    index_to_check =  list(zip(tuple(range(9)),tuple(np.repeat(row,9))))

    missing_squares = list(set(index_to_check) & set(pos_values.keys()))

    sub_dict = {k: pos_values[k] for k in pos_values.keys() & set(missing_squares)}

    #compare all list of pos values 
    for key_1 in sub_dict:
        for key_2 in sub_dict:
            #only coding for scenrio with 2 values, can be expanded to 3 or more... its unlikely irl to have more than 3
            if sub_dict[key_1] == sub_dict[key_2] and key_1 != key_2 and len(sub_dict[key_1]) == 2:
                naked_subset = sub_dict[key_1]
                naked_keys = [key_1,key_2]
                print(naked_subset,naked_keys)
                for amend_value_key in sub_dict:
                    if amend_value_key not in [key_1,key_2]:
                        sub_dict[amend_value_key] = list(set(sub_dict[amend_value_key]) - set(naked_subset))

def run_adv():
    for blank in list(pos_values.keys()):
        insert = check_3x3_adv(blank)
        print(blank,insert)
    return()


#sudoku = [[6, 0, 4, 0, 8, 1, 0, 0, 9], [5, 0, 9, 0, 4, 6, 1, 0, 8], [1, 0, 8, 0, 9, 5, 0, 0, 4],
#          [2, 9, 6, 4, 1, 3, 0, 8, 0], [7, 8, 5, 9, 6, 2, 3, 4, 1], [3, 4, 1, 8, 5, 7, 2, 9, 6],
#          [8, 0, 2, 6, 3, 9, 4, 0, 0], [4, 0, 7, 0, 2, 8, 9, 0, 3], [9, 0, 3, 0, 7, 4, 8, 0, 0]]

#sudoku_pd = pd.DataFrame(sudoku)
#board_pd = sudoku_pd
