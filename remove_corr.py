def remove_corr(df,corr_limit=.9):
  column_list = df.select_dtypes('number').columns
  duplicates=[]

  seen=[]

  for i in column_list:

      if i not in seen:

          seen.append(i)

          for j in column_list:

              if j not in seen:

                  if abs(df.fillna(0)[i].corr(df.fillna(0)[j]))>corr_limit:

                      print(i,j,df.fillna(0)[i].corr(df.fillna(0)[j]))

                      duplicates.append(j)

                      seen.append(j)
return df.drop(duplicates,axis=1)

