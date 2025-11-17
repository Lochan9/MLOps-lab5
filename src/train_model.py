import os
import pickle
import argparse
from joblib import dump
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--timestamp", type=str, required=True,
                        help="Timestamp for versioning")
    args = parser.parse_args()

    timestamp = args.timestamp

    # Generate synthetic dataset
    X, y = make_classification(
        n_samples=1200,
        n_features=8,
        n_informative=4,
        n_classes=2,
        random_state=42
    )

    os.makedirs("data", exist_ok=True)

    with open("data/data.pickle", "wb") as f:
        pickle.dump(X, f)
    with open("data/target.pickle", "wb") as f:
        pickle.dump(y, f)

    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)

    os.makedirs("models", exist_ok=True)

    model_path = f"models/model_{timestamp}_dt_model.joblib"
    dump(model, model_path)

    print(f"✔ Model trained and saved: {model_path}")
