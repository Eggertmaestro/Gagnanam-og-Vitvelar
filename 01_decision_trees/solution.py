# Author: Eggert Kristján Kristmundsson
# Date: 17/8/2022
# Project: Computer Exercise 1 - Decision Trees
# Acknowledgements: Prior split_data functions taken from lecture
#


from typing import Union
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree

from tools import load_iris, split_train_test


def prior(targets: np.ndarray, classes: list) -> np.ndarray:
    '''
    Calculate the prior probability of each class type  
    given a list of all targets and all class types
    '''
    samples_count = len(targets)
    class_prob = []

    for c in classes:
        class_count = 0
        for t in targets:
            if t == c:
                class_count += 1
        class_prob.append(class_count / samples_count)

    return class_prob


"""""


def main():
    x = prior([0, 0, 1], [0, 1])
    print(x)
    x = prior([0, 2, 3, 3], [0, 1, 2, 3])
    print(x)


main()
"""""


def split_data(
    features: np.ndarray,
    targets: np.ndarray,
    split_feature_index: int,
    theta: float
) -> Union[tuple, tuple]:
    '''
    Split a dataset and targets into two seperate datasets
    '''

    features_1 = features[features[:, split_feature_index] < theta, :]
    targets_1 = targets[features[:, split_feature_index] < theta]

    features_2 = features[features[:, split_feature_index] >= theta, :]
    targets_2 = targets[features[:, split_feature_index] >= theta]

    return (features_1, targets_1), (features_2, targets_2)


def part1_2():
    features, targets, classes = load_iris()
    (f_1, t_1), (f_2, t_2) = split_data(features, targets, 2, 4.65)
    return (f_1, t_1), (f_2, t_2)


(f_1, t_1), (f_2, t_2) = part1_2()
print(len(f_1))
print(len(f_2))
"""""

def gini_impurity(targets: np.ndarray, classes: list) -> float:
    '''
    Calculate:
        i(S_k) = 1/2 * (1 - sum_i P{C_i}**2)
    '''
    ...


def weighted_impurity(
    t1: np.ndarray,
    t2: np.ndarray,
    classes: list
) -> float:
    '''
    Given targets of two branches, return the weighted
    sum of gini branch impurities
    '''
    g1 = gini_impurity(...)
    g2 = gini_impurity(...)
    n = t1.shape[0] + t2.shape[0]
    ...


def total_gini_impurity(
    features: np.ndarray,
    targets: np.ndarray,
    classes: list,
    split_feature_index: int,
    theta: float
) -> float:
    '''
    Calculate the gini impurity for a split on split_feature_index
    for a given dataset of features and targets.
    '''
    ...


def brute_best_split(
    features: np.ndarray,
    targets: np.ndarray,
    classes: list,
    num_tries: int
) -> Union[float, int, float]:
    '''
    Find the best split for the given data. Test splitting
    on each feature dimension num_tries times.

    Return the lowest gini impurity, the feature dimension and
    the threshold
    '''
    best_gini, best_dim, best_theta = float("inf"), None, None
    # iterate feature dimensions
    for i in range(features.shape[1]):
        # create the thresholds
        thetas = ...
        # iterate thresholds
        for theta in thetas:
            ...
    return best_gini, best_dim, best_theta


class IrisTreeTrainer:
    def __init__(
        self,
        features: np.ndarray,
        targets: np.ndarray,
        classes: list = [0, 1, 2],
        train_ratio: float = 0.8
    ):
        '''
        train_ratio: The ratio of the Iris dataset that will
        be dedicated to training.
        '''
        (self.train_features, self.train_targets),\
            (self.test_features, self.test_targets) =\
            split_train_test(features, targets, train_ratio)

        self.classes = classes
        self.tree = DecisionTreeClassifier()

    def train(self):
        ...

    def accuracy(self):
        self.tree.fit(self.training_features, self.train_targets)

    def plot(self):
        ...

    def plot_progress(self):
        # Independent section
        # Remove this method if you don't go for independent section.
        ...

    def guess(self):
        ...

    def confusion_matrix(self):
        ...
"""""
