def colect_cases(correct_columns=True, correct_rows=True, name_csv=None):
    #Retrieves the notified cases in Brazilian boletins found in 
    #https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time.csv
    # correct_columns -> whether or not to rearrange the columns and rename them
    # Correct_rows -> whether or not to remove the total cases by date, which would duplicate the values per day
    # name_csv -> string withe name of the csv file to save the content of the Data Frame. If name_csv equals to None, no file is saved
    
    
    # loads the CSV data into df_cases
    df_cases = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time.csv', ) 

    
    # if correct_columns == True, it rearranges the columns orders and renames them    
    if correct_columns == True:
        df_cases = df_cases[['ibgeID', 'city', 'state', 'date', 'newCases', 'totalCases']].rename(columns={'ibgeID':'cod_mun', 'city':'municipio', 'state':'estado', 'date':'data', 'newCases':'novos_casos', 'totalCases':'casos_total'})    
    
    # if correct_rows == True, it removes the rows that show the total cases by date, which would duplicate the values per day    
    if correct_rows == True:
        filter_cases_total = df_cases.loc[df_cases.estado == 'TOTAL']
        df_cases.drop(filter_cases_total.index, axis=0, inplace=True)

    # removes the state name in the municipality column
    df_cases.municipio = df_cases.municipio.apply(lambda a_corrigir: a_corrigir.split('/')[0]) 
        
    # if name_csv contains the name of a csv file, a file will be created in the current directory 
    #or in the specified directory 
    if name_csv != None:
        df_cases.to_csv(name_csv, encoding='utf-8')
        

    
    return df_cases