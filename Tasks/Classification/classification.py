import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

from ast import literal_eval

def load_and_preprocess_data():
    train_df = pd.read_csv('/train2021.csv')
    test_df = pd.read_csv('/test2021.csv')

    columns = ['image_embeddings', 'embeddings_caption', 'embeddings_title']
    for column in columns:
        train_df[column] = train_df[column].apply(literal_eval)
        test_df[column] = test_df[column].apply(literal_eval)

    train_features = np.array([np.concatenate((img, title, caption)) for img, title, caption in 
                               zip(train_df['image_embeddings'], train_df['embeddings_title'], train_df['embeddings_caption'])])
    test_features = np.array([np.concatenate((img, title, caption)) for img, title, caption in 
                              zip(test_df['image_embeddings'], test_df['embeddings_title'], test_df['embeddings_caption'])])

    scaler = StandardScaler()
    train_features_scaled = scaler.fit_transform(train_features)
    test_features_scaled = scaler.transform(test_features)

    train_labels = train_df['label']
    test_labels = test_df['label']

    return train_features_scaled, test_features_scaled, train_labels, test_labels

def train_svm(train_features, train_labels, test_features, test_labels):
    svm_model = SVC(kernel='linear')
    svm_model.fit(train_features, train_labels)
    predictions = svm_model.predict(test_features)
    print("Accuracy:", accuracy_score(test_labels, predictions))
    print("Classification Report:\n", classification_report(test_labels, predictions))

def train_mnb(train_features, train_labels, test_features, test_labels):
    mnb_model = MultinomialNB()
    mnb_model.fit(train_features, train_labels)
    predictions = mnb_model.predict(test_features)
    print("Accuracy:", accuracy_score(test_labels, predictions))
    print("Classification Report:\n", classification_report(test_labels, predictions))
def train_logreg(train_features, train_labels, test_features, test_labels):
    logreg_model = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=5000)
    logreg_model.fit(train_features, train_labels)
    predictions = logreg_model.predict(test_features)
    print("Accuracy:", accuracy_score(test_labels, predictions))
    print("Classification Report:\n", classification_report(test_labels, predictions))
def train_logreg(train_features, train_labels, test_features, test_labels):
    logreg_model = LogisticRegression(multi_class='multinomial',solver='newton-cg',max_iter=5000)
    logreg_model.fit(train_features, train_labels)
    predictions = logreg_model.predict(test_features)
    print("Accuracy:", accuracy_score(test_labels, predictions))
    print("Classification Report:\n", classification_report(test_labels, predictions))
def train_mlp(train_features, train_labels, test_features, test_labels):
    mlp_model = MLPClassifier(hidden_layer_sizes=(200,), max_iter=10000, activation='relu', solver='adam', random_state=42)
    mlp_model.fit(train_features, train_labels)
    predictions = mlp_model.predict(test_features)
    print("Accuracy:", accuracy_score(test_labels, predictions))
    print("Classification Report:\n", classification_report(test_labels, predictions))

def main(args):
    train_features, test_features, train_labels, test_labels = load_and_preprocess_data()
    
    if args.model_type == 'svm':
        train_svm(train_features, train_labels, test_features, test_labels)
    elif args.model_type == 'mnb':
        train_mnb(train_features, train_labels, test_features, test_labels)
    elif args.model_type == 'logreg':
        train_logreg(train_features, train_labels, test_features, test_labels)
    elif args.model_type == 'mlp':
        train_mlp(train_features, train_labels, test_features, test_labels)
    else:
        print("Model type not supported.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train and evaluate a classification model on the dataset.')
    parser.add_argument('model_type', choices=['svm', 'mnb','logreg','mlp'], help='Type of model to train SVM, MultiNB, Logistic Regressio, MLP ')
    args = parser.parse_args()
    main(args)
