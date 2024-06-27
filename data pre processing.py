
'''Load the dataset, display the ten first lines, store the results in a variable called 'client_0_bills'.
What is the data type of the 'client_0_bills' variable ?
Display the general information of the dataset and try to answer the following questions : 
How many rows and columns do we have in this dataset ?
How many categorical features are present in the dataset ?
How much memory space does the dataset consume ?
Inspect the dataset for potential missing values.
Select your strategy to handle missing values, and tell us why you had made that choice.
Run a descriptive analysis on numeric features (columns).
Select the bills records for the client with an id ='train_Client_0', using 2 methods.
Transform the 'counter_type' feature to a numeric variable using the encoder of your choice.
Delete the 'counter_statue' feature from the Dataframe'''
import pandas as pd
import numpy as np
#load the dataset, display the ten first lines, store the results in a variable called 'client_0_bills'.
data_set=pd.read_csv("STEG_BILLING_HISTORY.csv")
client_0_bills=data_set.head(10)
#print(client_0_bills)
#What is the data type of the 'client_0_bills' variable ?
#print(type(client_0_bills))
#Display the general information of the dataset and try to answer the following questions :
#print(client_0_bills.info())
#print(len(client_0_bills))
# we have 16 columns and 10 rows and the memory usage is 1.4+ KB
#Inspect the dataset for potential missing values. 
#null=client_0_bills.isnull().sum().sum()
# there no missing values in the data set
#How many categorical features are present in the dataset ? we have 3 categorical fetures in the dataset 
#print(null)
#Select your strategy to handle missing values, and tell us why you had made that choice.
#there no missing values and if there were there I would have replaced them with the mean if there were integers value and if they were not integer values I would have drop the whole row


#Run a descriptive analysis on numeric features (columns).
#print(client_0_bills.describe())

#Select the bills records for the client with an id ='train_Client_0', using 2 methods.
#print(client_0_bills.loc[client_0_bills['client_id']=='train_Client_0',:])
#print(client_0_bills.query('client_id =="train_Client_0"'))

#transform the 'counter_type' feature to a numeric variable using the encoder of your choice.
# we are going to perform the categorical numerical transformation
from sklearn.preprocessing import LabelEncoder 
le=LabelEncoder()
#z=client_0_bills[['counter_type']=le.fit_transform(client_0_bills['client_id'])]
client_0_bills['counter_type']=le.fit_transform(client_0_bills['counter_type'])
print(client_0_bills['counter_type'])
#print(client_0_bills['counter_type'])
#Delete the 'counter_statue' feature from the Dataframe
client_0_bills.drop('counter_statue',axis=1,inplace=True)
print(client_0_bills.columns)

