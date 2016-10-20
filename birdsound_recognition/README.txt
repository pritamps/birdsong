The scope of the code contained in this folder is defined by the scope of the \hyperref{https://www.kaggle.com/c/mlsp-2013-birds}{Kaggle competition}. The task is to use machine learning to automatically detect the species of bird in a recording made in the wild. The recordings are usually of short duration. However, they may contain no birds (as is the case for most of the day), or multiple birds in the same recording (as is often the case for recordings taken at dawn or dusk). 

To that end, features provided by the organizers are used (and in the future, will be augmented) to write code to classify bird sounds based on wave files.

The following python files can be run (no parameters are required):

1. data_explore.py : Generates some statistics on the data (histogram of species counts in training set, histogram of number of species present in each recording)
2. classify.py : Performs classifications and writes out results in CSV format compatible with the Kaggle contest

data_extract.py provides a method to extract the features from the features text file and also link each feature to the audio files, since each audio file can have multiple features associated with it.