import pandas as pd
import os



def get_connection(db_name):
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

#-------------------------------------------------------------------    

def new_titanic():
    sql = '''
        'SELECT * FROM passengers'
        '''
    url = get_connection('titanic_db')
    df = pd.read_sql(sql, url)
    return df

#-------------------------------------------------------------------        
    
def get_titanic():
    file_name = 'titanic.csv'
    if os.path.isfile(file_name): # checks if file exist
        df = pd.read_csv(file_name, index_col=0) # assigns df to read on return
    else:
        df = new_titanic() # pull data using function
        df.to_csv(file_name) # converts df to csv file
    return df

#-------------------------------------------------------------------

def new_iris():
    sql = '''
        SELECT * FROM species 
        JOIN measurements USING (species_id)
        '''
    url = get_connection('iris_db')
    df = pd.read_sql(sql,url)
    return df

#-------------------------------------------------------------------

def get_iris():
    file_name = 'iris.csv'
    if os.path.isfile(file_name):
        df = pd.read_csv(file_name, index_col=0)
    else:
        df = new_iris()
        df.to_csv(file_name)
    return df

#-------------------------------------------------------------------

def new_telco():
    sql = '''
        SELECT * FROM customers c
        JOIN contract_types ct ON ct.contract_type_id=c.contract_type_id
        JOIN internet_service_types ist ON ist.internet_service_type_id=c.internet_service_type_id
        JOIN payment_types pt ON pt.payment_type_id=c.payment_type_id
        '''
    url = get_connection('telco_churn')
    df = pd.read_sql(sql, url)

#-------------------------------------------------------------------

def get_telco():
    file_name = 'telco.csv'
    if os.path.isfile(file_name):
        df = pd.read_csv(file_name, index_col=0)
    else:
        df = get_telco()
        df.to_csv(file_name)
    return df

#-------------------------------------------------------------------


