"""
Unsupervised Example
Example code to load the data and write a test submission, as well as evaluate 
a simple output using AUC. Output should be a file with one number per line, 
one for each corresponding test line, each denoting the probability of "FAKE".
"""
import csv
import numpy as np

with open('data/train1.csv', 'r') as f:
    reader = csv.reader(f)
    tweets_train = list(reader)
print ('train size', len(tweets_train))

with open('data/test1.csv', 'r') as f:
    reader = csv.reader(f)
    tweets_test1 = list(reader)
print('test size', len(tweets_test1))

# Parse data
X_train = [t[0] for t in tweets_train]
X_test = [t[0] for t in tweets_test1]

# Some example tweets
[tweet for tweet in X_train][:5]


## Example: predict fake using some simple heuristics

def get_y_score(X):
    y_score = []
    for tweet in X:
        if np.mod(np.char.count(tweet, "\""), 2) != 0 or np.mod(np.char.count(tweet, "'"), 2) != 0:
            # Check for uneven " and '
            y_score += [1.]
        else:
            y_score += [0.]
    return y_score

# Example writing output
y_score = get_y_score(X_test)
with open("output1.csv", "w") as f:
    for y in y_score:
        f.write('%f\n' % y)
