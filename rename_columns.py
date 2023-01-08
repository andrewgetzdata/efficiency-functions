import re 
from unidecode import unidecode

def rename_columns(df):
    """Standardizes the column name of any DataFrame to snake_case pattern.
    """
    for col in df.columns:
        new_col_name = re.sub('\W','',unidecode(col.lower().strip().replace(' ','_')))
        df.rename(columns = {col:new_col_name}, inplace = True)

# Understanding the code:
# re.sub('\W','','string!@#') -- remove any non alphanumeric character. Return 'string'
# unidecode('áçê') -- Remove accents and special character. Return 'ace'
# 'STRING'.lower() -- transform to lowercase. Return 'string'
# ' string '.strip() -- remove whitespaces at the beginning and end of the string. Return 'string'
# 'my string'.replace(' ','_') -- replace all ' ' for '_'. Return 'my_string'
