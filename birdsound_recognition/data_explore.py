import matplotlib.pyplot as plt
import numpy as np

# Import functions from extract_data.py
from data_extract import extract_data

# Extract the data
features_train, features_test, labels_train, test_ids = extract_data()

# Initialize variables
N_SPECIES = 19
species_names = range(N_SPECIES)
MAX_SPECIES_IN_RECORDING = 7
species_count = [0] * N_SPECIES
x = [0] * MAX_SPECIES_IN_RECORDING

pos = np.arange(len(species_names))
width = 1.0

# Generate the histogram
for labels_i in labels_train:
    print labels_i
    n_labels = 0
    for i in range(len(labels_i)):
        if labels_i[i] == 1:
            species_count[i] += 1
            n_labels += 1
    x[n_labels] += 1

# ax = plt.axes()
# ax.set_xticks(pos + (width/3))
# ax.set_xticklabels(species_names)
# locs, labels = plt.xticks()
# plt.figure(0)
# plt.setp(labels, rotation=45)
# plt.xlabel('Species index')
# plt.ylabel('Count in training set')
# plt.bar(species_names, species_count)
# print species_count
# print species_names
# plt.show()

plt.figure(1)
print x
plt.bar(range(MAX_SPECIES_IN_RECORDING), x)
pos = np.arange(MAX_SPECIES_IN_RECORDING)

# Generate axes and ticks
ax = plt.axes()
# Center the X-axis ticks on the boxes
ax.set_xticks(pos + width/3)
ax.set_xticklabels(range(MAX_SPECIES_IN_RECORDING))

# Generate axes labels
plt.xlabel("Number of species present in recording")
plt.ylabel("Count in training set")
width = 1.0

# Show plot!
plt.show()
