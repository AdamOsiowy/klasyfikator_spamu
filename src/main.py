import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, precision_score, accuracy_score

if __name__ == "__main__":
    data = pd.read_csv('../data/data_clean.csv', delimiter='\t', dtype={'email': 'string', 'label': 'int'})
    # print(data.shape)
    X_train, X_test, y_train, y_test = train_test_split(data['email'], data['label'], test_size=0.1, random_state=88)
    vectorizer = TfidfVectorizer(binary=True)
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    classifier = LogisticRegression(max_iter=1500, solver='liblinear', penalty='l1', random_state=0, C=6, verbose=1)
    classifier.fit(X_train, y_train)
    y_predicted = classifier.predict(X_test)
    precission = precision_score(y_test, y_predicted)
    recall = recall_score(y_test, y_predicted)
    accuracy = accuracy_score(y_test, y_predicted)
    print(f"preccision score: {precission}")
    print(f"recall score: {recall}")
    print(f"accuracy score: {accuracy}")
