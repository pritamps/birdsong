import numpy as np
import pandas as pd

# This import is necessary to convert the MIML problem to a binary relevance
# problem
from sklearn.preprocessing import MultiLabelBinarizer


def extract_data():
    """
    Read the data files and extract data from them (training and test features,
    ids of test files, training labels
    :return: A list: ]features_train, features_test, labels_train, test_ids]
    """

    with open("essential_data/rec_labels_test_hidden.txt") as f:
        lines = f.readlines()

    labels_train = []
    training_ids = []
    test_ids = []
    for line in lines[1:]:
        if "?" not in line:
            x = map(int, line.split(','))
            labels_train.append(x[1:])
            training_ids.append(x[0])
        else:
            x = int(line.split(',')[0])
            test_ids.append(x)

    # Transform training_labels to nice format
    labels_train = MultiLabelBinarizer().fit_transform(labels_train)

    # Get the features from the files
    features_all = np.array(pd.read_csv
                            ('supplemental_data/histogram_of_segments.txt',
                             skiprows=1,
                             index_col=0,
                             header=None).values)
    features_train = features_all[training_ids]
    features_test = features_all[test_ids]

    # FOR DEBUGGING: Make sure sizes match
    print "Data size: " + str(len(lines[1:]))
    print "Feature set size: " + str(features_all.shape)
    print "Test size: " + str(len(test_ids))
    print "Training size: " + str(len(training_ids))
    print "Training feature set size: " + str(features_train.shape)
    print "Test feature set size: " + str(features_test.shape)
    return features_train, features_test, labels_train, test_ids
