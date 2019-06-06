import pandas as pd

class Formats:
    def __init__(self):
        self.functions = [
            """
            df_make_rename_drop: turns any pandas.DataFrame compatible object into a DataFrame, 
            and optionally renames columns or drops columns/rows
            col_dict format is current_key:new_key
            _to_drop values are any list-like
            """
            ]

        def print_functions:
        for func in self.functions:
            print(func)

    def df_make_rename_drop(data, col_dict=None, cols_to_drop=None, rows_to_drop=None):
        try:
            df = pd.DataFrame(data).rename(columns=cols)
        except Exception as e:
            print('conversion of object {} to pd.Dataframe failed'.format(data))
            print('with exception {}'.format(e))
            return None
        if col_dict:
            try:
                df.rename(columns=col_dict)
            except Exception as e:
                print('column rename failed for DataFrame {}'.format(df))
                print('with exception {}'.format(e))
        if cols_to_drop:
            try:
                df = df.drop(cols_to_drop, axis = 1)
            except KeyError: 
                print('the columns to drop were not present in {}'.format(df))
        if rows_to_drop:
            try:
                df = df.drop(rows_to_drop, axis = 0)
            except KeyError: 
                print('the rows to drop were not present in {}'.format(df))
        return df