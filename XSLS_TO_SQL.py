# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:40:23 2018

@author: paprasad
"""




import pandas as pd
import numpy as np
folder = 'd:\Profiles\paprasad\PROJECT'
file_name='\MET_Config1.xlsx'
path = folder+file_name
xl = pd.ExcelFile(path)
 
def Attach_alias(alias,columns):
    temp = ""
    for col in columns:
        temp = temp+alias+"."+col+", "
    temp = temp[:-2]
    return temp    
        

def Set_Column(columns):
    temp =""
    columns=columns.tolist()
    columns.pop(0)
    for col in columns:
        temp = temp+" T."+col+"="+" S."+col+" ,"+"\n"
    temp = temp.rsplit(' ',1)[0]     
    return temp
def Create_Merge(sheet,sql,columns):
    join = "T."+columns[0]+"="+"S."+columns[0]
    update_col = Set_Column(columns)
    merge_sql = "MERGE INTO "+ sheet +" T "+"\n"+"USING (" + "\n"+sql+"\n"+") S"+"\n"+"ON ( "+join+" )"+"\n"+"WHEN MATCHED THEN UPDATE SET"+"\n"+update_col+"\n"+"WHEN NOT MATCHED THEN INSERT ( "+Attach_alias("T",columns)+" )"+" VALUES ( "+Attach_alias("T",columns)+" )"
    sql_file = open(folder+"\\"+sheet+".sql","w+")
    sql_file.write(merge_sql)
    sql_file.close()
    
   
def Create_SQl(sheet):
    df = xl.parse(sheet)
    df = df.replace(np.nan, '', regex=True)
    columns = df.columns.values
    print(columns.size)
    sql=""
    for index, row in df.iterrows():
        concat = "SELECT"
        temp = ""
        for i in range(columns.size):
            if (type(row[i])==str):
                temp = temp+" '"+str(row[i])+"' AS "+  columns[i]  +","
            else:
                temp  = temp+" "+str(row[i])+" AS "+  columns[i]  +","
        temp = temp[:-1]
        concat = concat + temp +" FROM DUAL UNION" +"\n"  
        sql = sql+" "+concat
    sql = sql.rsplit(' ',1)[0] 
    Create_Merge(sheet,sql,columns)    
for sheet in xl.sheet_names:
    table_name = sheet
    Create_SQl(sheet)
    