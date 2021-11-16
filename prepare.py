import pandas as pd
from sklearn.model_selection import train_test_split
import acquire

def prep_iris():
    df = acquire.get_iris_data()
    df = df.drop(columns=['species_id','measurement_id'])
    df = df.rename(columns={'species_name':'species'})
    df_species = pd.get_dummies(df.species, prefix='is')
    df = pd.concat([df, df_species], axis=1)
    return df



def prep_titanic():
    df = acquire.get_titanic_data()
    drop_col = ['embarked','fare', 'class', 'deck', 'age']
    df = df.drop(columns = drop_col)
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    dummy_cols = pd.get_dummies(df[['sex', 'embark_town']], drop_first=True)
    df = pd.concat([df, dummy_cols], axis=1)
    return df



def prep_telco():
    df = acquire.get_telco_data()
    # id cols to drop
    drop_cols = ['internet_service_type_id',
             'internet_service_type_id.1',
             'contract_type_id',
             'contract_type_id.1',
             'payment_type_id',
             'payment_type_id.1']
    # drop columns
    df = df.drop(columns=drop_cols)
    # replace blank spaces with zeros
    df['total_charges'] = df.total_charges.replace(' ', '0')
    # convert total charges from object to float
    df.total_charges = df.total_charges.astype(float)
    # id columns for dummy variables
    dummies_cols = [
 'gender',
 'senior_citizen',
 'partner',
 'dependents',
 'phone_service',
 'multiple_lines',
 'online_security',
 'online_backup',
 'device_protection',
 'tech_support',
 'streaming_tv',
 'streaming_movies',
 'paperless_billing',
 'churn',
 'contract_type',
 'internet_service_type',
 'payment_type']
    # creaet dummy variables and assign to variable
    dummies_df = pd.get_dummies(df[dummies_cols], drop_first=True)
    # concat df with dummy variable columns
    df = pd.concat([df, dummies_df], axis=1)
    return df



def split_titanic(df):
    train_validate, test = train_test_split(df, 
                                             test_size=.2, 
                                             random_state=123, 
                                             stratify=df.survived)
    train, validate = train_test_split(train_validate,
                                      test_size=.3,
                                      random_state=123,
                                      stratify=train_validate.survived)
    return train, validate, test



def split_iris(df):
    train_validate, test = train_test_split(df, 
                                             test_size=.2, 
                                             random_state=123, 
                                             stratify=df.species)
    train, validate = train_test_split(train_validate,
                                      test_size=.3,
                                      random_state=123,
                                      stratify=train_validate.species)
    return train, validate, test



def split_telco(df):
    train_validate, test = train_test_split(df, 
                                             test_size=.2, 
                                             random_state=123, 
                                             stratify=df.churn)
    train, validate = train_test_split(train_validate,
                                      test_size=.3,
                                      random_state=123,
                                      stratify=train_validate.churn)
    return train, validate, test





