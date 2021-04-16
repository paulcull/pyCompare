import pandas as pd

def df_dict(df):
    dict = {}
    for col in df:
        dict[col] = df[col].unique().tolist() # unique method optional
    return dict


df_we = pd.read_excel('./data/word_compressions.xlsx')
# convert to dictionary
di_we = pd.Series(df_we.Expand.values,index=df_we.CODE).to_dict()

df_dd = pd.read_excel('./data/data_dictionary.xlsx')
# df_dm = pd.read_excel('./input/datamodel.xlsx',converters={'TABLE':di_we, 'Attribute':di_we})
df_dm = pd.read_excel('./input/datamodel.xlsx')
print(df_dm)

print("start with the data model...")

# for index, row in df_dm.iterrows():
#     print(row['Table'] , "." , row['Attribute'])
#     row['Table'].replace()

# df_we.set_index('CODE')
# df_dm = df_dm.set_index('TABLE').rename( columns = {'TABLE':'Expand'})

# df_we.columns=['Table','Word']
# print(df_we)
# df_exp_model = pd.merge(
# df_dm,df_we, how='left', on=["Table"]
# )
# df_we.columns=['Attribute','Word2']
# df_exp_model2 = pd.merge(
# df_exp_model,df_we, how='left', on=["Attribute"]
# )

# print(df_exp_model2)

# df_dm['Table'].map(di_we).fillna(df_dm['Table'])
df_dm['Table'].replace(di_we, inplace=True)
df_dm['Attribute'].replace(di_we, inplace=True)
print(df_dm)



