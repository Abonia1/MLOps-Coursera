import pickle
from main import clf


def test_accuracy():

    # Load test data
    with open("app/data/test_data.pkl", "rb") as file:
        test_data = pickle.load(file)

    # Unpack the tuple a lets testing
    X_test, y_test = test_data

    # Compute accuracy of classifier
    acc = clf.score(X_test, y_test)

    # Accuracy should be over 90%
    assert acc > 0.9
