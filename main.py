import pandas as pd

# function to expand all columns in a frame with a substitution dictionary
def df_expand(df, di):
    notfirstcol = False
    for col in df:
        print(col)
        print(notfirstcol)
        if  notfirstcol:
            df[col].replace(di, inplace=True)
        notfirstcol = True
    return df

def df_collapse(df,name):
    df[name] = df[df.columns[1:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
    return df


df_we = pd.read_excel('./data/word_compressions.xlsx')
# convert to dictionary
di_we = pd.Series(df_we.Expand.values,index=df_we.CODE).to_dict()

df_dd = pd.read_excel('./data/data_dictionary.xlsx')
df_dm = pd.read_excel('./input/datamodel.xlsx')
print(df_dm)

print("start with the data model...")

df_dm_table = pd.concat([df_dm['Table'], df_dm['Table'].str.split('_', expand=True)], axis=1)
df_dm_attribute = pd.concat([df_dm['Attribute'], df_dm['Attribute'].str.split('_', expand=True)], axis=1)
print(df_dm_table)
print(df_dm_attribute)

df_expand(df_dm_table,di_we)
df_expand(df_dm_attribute,di_we)

print(df_dm_table)
print(df_dm_attribute)

df_collapse(df_dm_table,'exp table')
df_collapse(df_dm_attribute,'exp attr')

print(df_dm_table)
print(df_dm_attribute)

df_dm_expand = pd.concat([df_dm_table,df_dm_attribute],axis=1)
print(df_dm_expand)

retain_col_list = ['Table','Attribute','exp table','exp attr']
df_dm_expand = df_dm_expand[retain_col_list]
print(df_dm_expand)


