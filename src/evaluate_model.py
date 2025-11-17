import os
import json
import argparse
from sklearn.metrics import f1_score
from sklearn.datasets import make_classification
from joblib import load

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--timestamp", type=str, required=True,
                        help="Timestamp used to load model")
    args = parser.parse_args()

    timestamp = args.timestamp
    model_path = f"models/model_{timestamp}_dt_model.joblib"

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found: {model_path}")

    model = load(model_path)

    # Generate evaluation dataset
    X_eval, y_eval = make_classification(
        n_samples=800,
        n_features=8,
        n_informative=4,
        n_classes=2,
        random_state=99
    )

    # Predict and compute F1 Score
    y_pred = model.predict(X_eval)
    f1 = f1_score(y_eval, y_pred)

    metrics = {
        "timestamp": timestamp,
        "F1_Score": float(f1)
    }

    os.makedirs("metrics", exist_ok=True)

    metrics_path = f"metrics/{timestamp}_metrics.json"
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)

    print(f"✔ Evaluation complete. Metrics saved: {metrics_path}")
