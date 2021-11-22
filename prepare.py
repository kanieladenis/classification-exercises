import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")

#----------------------------IRIS---------------------------------------



def prep_iris():
    df = acquire.get_iris()
    df = df.drop(columns=['species_id','measurement_id'])
    df = df.rename(columns={'species_name':'species'})
    df_species = pd.get_dummies(df.species, prefix='is')
    df = pd.concat([df, df_species], axis=1)
    return df



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

#---------------------------TITANIC----------------------------------------


def clean_titanic(df):
    '''
    This function will clean the data prior to splitting.
    '''
    
    # Drops any duplicate values
    df = df.drop_duplicates()
    
    # Reduce obvious noise
    df = df.set_index("passenger_id")
    
    # Uses one-hot encoding to create dummies of string columns for future modeling 
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], dummy_na=False, drop_first=[True, True])
    df = pd.concat([df, dummy_df], axis=1)
    
    # Fills the small number of null values for embark_town with the mode
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    
    # Drops columns that are already represented by other columns
    cols_to_drop = ['deck', 'embarked', 'class']
    df = df.drop(columns=cols_to_drop)
        
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



def impute_titanic_mode(train, validate, test):
    '''
    Takes in train, validate, and test, and uses train to identify the best value to replace nulls in embark_town
    Imputes that value into all three sets and returns all three sets
    '''
    imputer = SimpleImputer(missing_values = np.nan, strategy='most_frequent')
    
    train[['embark_town']] = imputer.fit_transform(train[['embark_town']])
    
    validate[['embark_town']] = imputer.transform(validate[['embark_town']])
    
    test[['embark_town']] = imputer.transform(test[['embark_town']])
    
    return train, validate, test



def impute_mean_age(train, validate, test):
    '''
    This function imputes the mean of the age column for
    observations with missing values.
    Returns transformed train, validate, and test df.
    '''
    # create the imputer object with mean strategy
    imputer = SimpleImputer(strategy = 'mean')
    
    # fit on and transform age column in train
    train['age'] = imputer.fit_transform(train[['age']])
    
    # transform age column in validate
    validate['age'] = imputer.transform(validate[['age']])
    
    # transform age column in test
    test['age'] = imputer.transform(test[['age']])
    
    return train, validate, test



def prep_titanic(df):
    '''
    Combines the clean_titanic_data, split_titanic_data, and impute_mean_age functions.
    '''
    df = clean_titanic(df)

    train, validate, test = split_titanic(df)    
  
    train, validate, test = impute_mean_age(train, validate, test)

    return train, validate, test





#----------------------------TELCO---------------------------------------

def prep_telco():
    df = acquire.get_telco()
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
    df.columns = [col.lower().replace('.','_') for col in df]
    return df



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

#-------------------------------------------------------------------







