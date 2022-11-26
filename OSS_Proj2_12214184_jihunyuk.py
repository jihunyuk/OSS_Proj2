# PLEASE WRITE THE GITHUB URL BELOW!
# https://github.com/jihunyuk/OSS_Project_2.git

import sys
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def load_dataset(dataset_path):
	# To-Do: Implement this function
	dataset_df = pd.read_csv(dataset_path)
	return dataset_df


def dataset_stat(dataset_df):
	# To-Do: Implement this function
	n_feats = (len(dataset_df.iloc[0, :])) - 1
	target_data = dataset_df.iloc[:, -1]
	# n_class0 = dataset_df.groupby("target")[0]
	# n_class1 = dataset_df.groupby("target")[1]
	n_class0 = 0
	n_class1 = 0
	for i in target_data:
		if i == 0:
			n_class0 = n_class0 + 1
		if i == 1:
			n_class1 = n_class1 + 1
	return n_feats, n_class0, n_class1


def split_dataset(dataset_df, testset_size):
	# To-Do: Implement this function
	X = dataset_df.drop(columns="target", axis=1)
	y = data_df["target"]
	x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=testset_size)
	return x_train, x_test, y_train, y_test


def decision_tree_train_test(x_train, x_test, y_train, y_test):
	# To-Do: Implement this function
	decision_tree = tree.DecisionTreeClassifier()
	decision_tree.fit(x_train, y_train)
	y_pred = decision_tree.predict(x_test)
	acc = accuracy_score(y_test, y_pred)
	prec = precision_score(y_test, y_pred)
	recall = recall_score(y_test, y_pred)
	return acc, prec, recall


def random_forest_train_test(x_train, x_test, y_train, y_test):
	# To-Do: Implement this function
	rft = RandomForestClassifier()
	rft.fit(x_train, y_train)
	y_pred = rft.predict(x_test)
	acc = accuracy_score(y_test, y_pred)
	prec = precision_score(y_test, y_pred)
	recall = recall_score(y_test, y_pred)
	return acc, prec, recall


def svm_train_test(x_train, x_test, y_train, y_test):
	# To-Do: Implement this function
	svm = make_pipeline(StandardScaler(), SVC(gamma='auto'))
	svm.fit(x_train, y_train)
	y_pred = svm.predict(x_test)
	acc = accuracy_score(y_test, y_pred)
	prec = precision_score(y_test, y_pred)
	recall = recall_score(y_test, y_pred)
	return acc, prec, recall

def print_performances(acc, prec, recall):
	#Do not modify this function!
	print ("Accuracy: ", acc)
	print ("Precision: ", prec)
	print ("Recall: ", recall)

if __name__ == '__main__':
	#Do not modify the main script!
	data_path = sys.argv[1]
	data_df = load_dataset(data_path)

	n_feats, n_class0, n_class1 = dataset_stat(data_df)
	print ("Number of features: ", n_feats)
	print ("Number of class 0 data entries: ", n_class0)
	print ("Number of class 1 data entries: ", n_class1)

	print ("\nSplitting the dataset with the test size of ", float(sys.argv[2]))
	x_train, x_test, y_train, y_test = split_dataset(data_df, float(sys.argv[2]))

	acc, prec, recall = decision_tree_train_test(x_train, x_test, y_train, y_test)
	print ("\nDecision Tree Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = random_forest_train_test(x_train, x_test, y_train, y_test)
	print ("\nRandom Forest Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = svm_train_test(x_train, x_test, y_train, y_test)
	print ("\nSVM Performances")
	print_performances(acc, prec, recall)