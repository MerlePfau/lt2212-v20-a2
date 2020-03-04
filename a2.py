import argparse
import random
from sklearn.datasets import fetch_20newsgroups
from sklearn.base import is_classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.decomposition import TruncatedSVD
random.seed(42)


###### PART 1
#DONT CHANGE THIS FUNCTION
def part1(samples):
    #extract features
    X = extract_features(samples)
    assert type(X) == np.ndarray
    print("Example sample feature vec: ", X[0])
    print("Data shape: ", X.shape)
    return X


def word_extractor(text):
    # splits text into words > lowercase > isalpha
    words = text.split()
    cleaned_words = [w.lower() for w in words if w and w.isalpha()]
    return cleaned_words


def my_tokenizer(text):
    # creates list of all tokens in sample
    tokens = []
    w = word_extractor(text)
    tokens.extend(w)
    tokens = list(set(tokens))
    return tokens


def bag_of_words(columns, wordlist, index_overview):
    # creates vector for a given sample
    bag_vector = np.zeros(columns)
    for word in wordlist:
        index = index_overview[word]
        bag_vector[index] += 1
    return bag_vector


def extract_features(samples):
    print("Extracting features ...")
    index_overview = {}
    list_of_sample_words = []
    i = 0
    # saves all words as indices
    for sample in samples:
        wordlist = my_tokenizer(sample)
        list_of_sample_words.append(wordlist)
        for word in wordlist:
            if word not in index_overview:
                index_overview[word] = i
                i += 1
    all_words = index_overview.keys()
    columns = len(all_words)
    rows = len(samples)
    # initiate the array
    features = np.zeros((rows, columns), dtype=np.uint16)
    sample_number = 0
    for wordlist in list_of_sample_words:
        features[sample_number, :] = bag_of_words(columns, wordlist, index_overview)
        sample_number += 1
    low_freq = []
    col_sums = np.sum(features, axis=0)
    # removes all words with counts <5
    for i in range(len(col_sums)):
        if col_sums[i] < 5:
            low_freq.append(i)
    extracted_features = np.delete(features, low_freq, axis=1)
    return extracted_features



##### PART 2
#DONT CHANGE THIS FUNCTION
def part2(X, n_dim):
    #Reduce Dimension
    print("Reducing dimensions ... ")
    X_dr = reduce_dim(X, n=n_dim)
    assert X_dr.shape != X.shape
    assert X_dr.shape[1] == n_dim
    print("Example sample dim. reduced feature vec: ", X[0])
    print("Dim reduced data shape: ", X_dr.shape)
    return X_dr


def reduce_dim(X, n=10):
    svd = TruncatedSVD(n_components=n, n_iter=7, random_state=42)
    return svd.fit_transform(X)
#    pca = PCA(n_components=n)
#    return pca.fit_transform(X)



##### PART 3
#DONT CHANGE THIS FUNCTION EXCEPT WHERE INSTRUCTED
def get_classifier(clf_id):
    if clf_id == 1:
        clf = KNeighborsClassifier(n_neighbors=10)
    elif clf_id == 2:
        clf = DecisionTreeClassifier()
    else:
        raise KeyError("No clf with id {}".format(clf_id))

    assert is_classifier(clf)
    print("Getting clf {} ...".format(clf.__class__.__name__))
    return clf

#DONT CHANGE THIS FUNCTION
def part3(X, y, clf_id):
    #PART 3
    X_train, X_test, y_train, y_test = shuffle_split(X,y)

    #get the model
    clf = get_classifier(clf_id)

    #printing some stats
    print()
    print("Train example: ", X_train[0])
    print("Test example: ", X_test[0])
    print("Train label example: ",y_train[0])
    print("Test label example: ",y_test[0])
    print()


    #train model
    print("Training classifier ...")
    train_classifier(clf, X_train, y_train)


    # evaluate model
    print("Evaluating classifier ...")
    evaluate_classifier(clf, X_test, y_test)


def shuffle_split(X, y):
    shuffle = train_test_split(X, y, test_size=0.20, random_state=42)
    return shuffle


def train_classifier(clf, X, y):
    assert is_classifier(clf)
    clf.fit(X, y)
    return clf


def evaluate_classifier(clf, X, y):
    assert is_classifier(clf)
    prediction = clf.predict(X)
    accuracy = accuracy_score(y, prediction)
    f = f1_score(y, prediction, average='weighted')
    recall = recall_score(y, prediction, average='weighted')
    precision = precision_score(y, prediction, average='weighted')
    print('accuracy: ', accuracy, ', precision: ', precision, ', recall: ', recall, ', F1 score: ', f)
    return (accuracy, precision, recall, f1_score)


######
#DONT CHANGE THIS FUNCTION
def load_data():
    print("------------Loading Data-----------")
    data = fetch_20newsgroups(subset='all', shuffle=True, random_state=42)
    print("Example data sample:\n\n", data.data[0])
    print("Example label id: ", data.target[0])
    print("Example label name: ", data.target_names[data.target[0]])
    print("Number of possible labels: ", len(data.target_names))
    return data.data, data.target, data.target_names


#DONT CHANGE THIS FUNCTION
def main(model_id=None, n_dim=False):

    # load data
    samples, labels, label_names = load_data()


    #PART 1
    print("\n------------PART 1-----------")
    X = part1(samples)

    #part 2
    if n_dim:
        print("\n------------PART 2-----------")
        X = part2(X, n_dim)

    #part 3
    if model_id:
        print("\n------------PART 3-----------")
        part3(X, labels, model_id)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n_dim",
                        "--number_dim_reduce",
                        default=False,
                        type=int,
                        required=False,
                        help="int for number of dimension you want to reduce the features for")

    parser.add_argument("-m",
                        "--model_id",
                        default=False,
                        type=int,
                        required=False,
                        help="id of the classifier you want to use")

    args = parser.parse_args()
    main(   
            model_id=args.model_id, 
            n_dim=args.number_dim_reduce
            )
