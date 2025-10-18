import argparse, json, os, pathlib
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
from .model import build_cnn

FM_LABELS = ["t-shirt/top","trouser","pullover","dress","coat","sandal","shirt","sneaker","bag","ankle_boot"]

def load_fashion_mnist():
    (x_tr, y_tr), (x_te, y_te) = tf.keras.datasets.fashion_mnist.load_data()
    x_tr = x_tr[..., None].astype("float32")
    x_te = x_te[..., None].astype("float32")
    return (x_tr, y_tr), (x_te, y_te)

def plot_confusion(y_true, y_pred, out):
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation="nearest")
    ax.figure.colorbar(im, ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    ax.set_title("Confusion Matrix")
    plt.tight_layout()
    pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out)
    plt.close(fig)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--epochs", type=int, default=5)
    ap.add_argument("--output_dir", type=str, default="./artifacts/saved_model")
    args = ap.parse_args()

    (x_tr, y_tr), (x_te, y_te) = load_fashion_mnist()
    model = build_cnn()
    model.fit(x_tr, y_tr, epochs=args.epochs, validation_split=0.1, verbose=2)

    # Evaluate
    probs = model.predict(x_te, verbose=0)
    y_pred = probs.argmax(axis=1)
    acc = float((y_pred == y_te).mean())
    prec, rec, f1, _ = precision_recall_fscore_support(y_te, y_pred, average=None, zero_division=0)

    # Save plots + metrics
    plot_confusion(y_te, y_pred, "assets/plots/confusion_matrix.png")
    metrics = {
        "accuracy": acc,
        "precision_per_class": prec.tolist(),
        "recall_per_class": rec.tolist(),
        "f1_per_class": f1.tolist(),
        "labels": FM_LABELS,
        "epochs": args.epochs,
        "seed": 42
    }
    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    # Export SavedModel
    os.makedirs(args.output_dir, exist_ok=True)
    tf.saved_model.save(model, args.output_dir)
    print(f"SavedModel exported to: {args.output_dir}")
    print(f"Test accuracy: {acc:.3f}")

if __name__ == "__main__":
    main()
