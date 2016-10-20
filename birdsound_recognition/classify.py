
from sklearn.ensemble import RandomForestRegressor

# Import functions in extract_data.py
from data_extract import extract_data

# Extract the data from the provided files
features_train, features_test, labels_train, test_ids = extract_data()

# The estimators to iterate over. This is used for both the manual
# grid search and to compare algorithms
ESTIMATORS = {
    # "RFG": RandomForestRegressor(n_estimators=100, max_features=32,
    #                                    random_state=0),
    "RFG_1": RandomForestRegressor(n_estimators=10, max_features=16,
                                   random_state=0),
    "RFG_2": RandomForestRegressor(n_estimators=50, max_features=16,
                                   random_state=0),
    "RFG_3": RandomForestRegressor(n_estimators=100, max_features=16,
                                   random_state=0),
    "RFG_4": RandomForestRegressor(n_estimators=10, max_features=32,
                                   random_state=0),
    "RFG_5": RandomForestRegressor(n_estimators=50, max_features=32,
                                   random_state=0),
    "RFG_6": RandomForestRegressor(n_estimators=100, max_features=32,
                                   random_state=0),
    "RFG_7": RandomForestRegressor(n_estimators=10, max_features=100,
                                   random_state=0),
    "RFG_8": RandomForestRegressor(n_estimators=50, max_features=100,
                                   random_state=0),
    "RFG_9": RandomForestRegressor(n_estimators=100, max_features=100,
                                   random_state=0),
    # "K-nn": KNeighborsRegressor(),
    # "LR": LinearRegression(),
    # "Ridge": RidgeCV(),
    # "DT": tree.DecisionTreeClassifier(),
}

### Perform the classification by iterating through the algorithms
### in ESTIMATORS()
y_test_predict = dict()
for name, estimator in ESTIMATORS.items():

    # Fit the model using the current algorithm
    estimator = estimator.fit(features_train, labels_train)
    # Predict
    y_test = estimator.predict(features_test)

    # Write the results to a named csv file based on the results
    # required by Kaggle
    with open('results' + name + '.csv', 'w') as results_file:
        results_file.write("Id,Probability\n")
        for i in range(len(test_ids)):
            for j in range(19):
                results_file.write(str(test_ids[i] * 100 + j) + "," +
                                   str(y_test[i][j]) + "\n")
