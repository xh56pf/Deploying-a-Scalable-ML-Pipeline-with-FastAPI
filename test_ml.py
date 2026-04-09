import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from ml.data import process_data

@pytest.fixture 
def data():
    df=pd.DataFrame(
        {
            "age":[39,40,21],
            "workclass":["Self-employ","State-gov","Private"],
            "fnlgt":[77516, 77322, 213345],
            "education":["Bachelors", "Masters","HS-grad"],
            "education-num":[13,14,9],
            "marital-status":["Married","Divorced","Never-married"],
            "occupation":["Adm-clerical","Exec-managerial","Handlers-cleaners"],
            "relationship":["Not-in-family","Husband","Wife"],
            "race":["White","White","Black"],
            "sex":["Male","Male","Female"],
            "capital-gain":[2174,0,0],
            "capital-loss":[0,0,0],
            "hours-per-week":[40,13,40],
            "native-country":["United-States","United-States","Cuba"],
            "salary":["<=50K",">50K","<=50K"]
        }
    )
    return df

@pytest.fixture
def cat_features():
    return [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
        ]


# TODO: implement the first test. Change the function name and input as needed
def test_process_data_apply_labels(data, cat_features):
    """
    Tests if labels applied for the salary values (<=50K and >50K) are correctly mapped as 0 or 1, respectively
    """
    # Your code here
   
    _, y, _, _ = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=True,
    )

    #Checks if values in the label, y, are 0 or 1 as performed by LabelBinarizer
    assert y[0]==0
    assert y[1]==1
    assert y[2]==0
    


# TODO: implement the second test. Change the function name and input as needed
def test_process_data_array(data, cat_features):
    """
    # Tests that process_data outputs a 2D array
    """
    X,_,encoder,_= process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=True
    )

    #Checking if return value, X, is a 2D array

    assert isinstance(X, np.ndarray)
    assert len(X.shape)==2
    



# TODO: implement the third test. Change the function name and input as needed
def test_process_data_numerical(data, cat_features):
    """
    # Tests that process_data outputs only numerical values and not text for onehotencoded values
    """
    X,_,encoder,_= process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=True
    )

    #Checking if all values in returned array are numerical and not string for encoded categorical data
    assert np.issubdtype(X.dtype, np.number)
