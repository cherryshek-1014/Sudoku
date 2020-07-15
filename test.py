import pandas as pd 

sudoku = [[6, 0, 4, 0, 8, 1, 0, 0, 9], [5, 0, 9, 0, 4, 6, 1, 0, 8], [1, 0, 8, 0, 9, 5, 0, 0, 4],
          [2, 9, 6, 4, 1, 3, 0, 8, 0], [7, 8, 5, 9, 6, 2, 3, 4, 1], [3, 4, 1, 8, 5, 7, 2, 9, 6],
          [8, 0, 2, 6, 3, 9, 4, 0, 0], [4, 0, 7, 0, 2, 8, 9, 0, 3], [9, 0, 3, 0, 7, 4, 8, 0, 0]]

sudoku_pd = pd.DataFrame(sudoku)

#check the last row ((X,8))
index_to_check =  list(zip(tuple(range(9)),tuple(np.repeat(8,9))))

missing_squares = list(set(index_to_check) & set(pos_values.keys()))

sub_dict = {k: pos_values[k] for k in pos_values.keys() & set(missing_squares)}

#compare all list of pos values 
for key_1 in sub_dict:
    for key_2 in sub_dict:
        if sub_dict[key_1] == sub_dict[key_2] and key_1 != key_2:
            naked_subset = sub_dict[key_1]
            naked_keys = [key_1,key_2]
            for amend_value_key in sub_dict:
                if amend_value_key not in [key_1,key2]:
                    sub_dict[amend_value_key] = list(set(sub_dict[amend_value_key]) - set(naked_subset))
