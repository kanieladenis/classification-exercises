def get_connection(db_name):
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    
    
    
def get_titanic_data():
    import os
    file_name = 'titanic.csv'
    if os.path.isfile(file_name): # checks if file exist
        df = pd.read_csv(file_name) # assigns df to read on return
    else:
        sql = '''
        'SELECT * FROM passengers'
        '''
        url = get_connection('titanic_db')
        df = pd.read_sql(sql, url) #creates df
        df.to_csv(file_name) # converts df to csv file
    return df



def get_iris_data():
    import os
    file_name = 'iris.csv'
    if os.path.isfile(file_name):
        df = pd.read_csv(file_name)
    else:
        sql = '''
        SELECT * FROM species 
        JOIN measurements USING (species_id)
        '''
        url = get_connection('iris_db')
        df = pd.read_sql(sql,url)
        df.to_csv(file_name)
    return df



def get_telco_data():
    import os
    file_name = 'telco.csv'
    if os.path.isfile(file_name):
        df = pd.read_csv(file_name)
    else:
        sql = '''
        SELECT * FROM customers c
        JOIN contract_types ct ON ct.contract_type_id=c.contract_type_id
        JOIN internet_service_types ist ON ist.internet_service_type_id=c.internet_service_type_id
        JOIN payment_types pt ON pt.payment_type_id=c.payment_type_id
        '''
        url = get_connection('telco_churn')
        df = pd.read_sql(sql, url)
        df.to_csv(file_name)
    return df

