import numpy as np

#locate all the blanks
zero_row_loc , zero_col_loc = np.where(board_pd.values == 0)

list(zip(board_pd.index[zero_row_loc],board_pd.columns[zero_col_loc]))

#added line
