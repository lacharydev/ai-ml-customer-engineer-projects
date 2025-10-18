import argparse, base64, json, os
from io import BytesIO
from PIL import Image
import numpy as np
from dotenv import load_dotenv
from google.cloud import aiplatform

def preprocess_28x28(path):
    # convert to 28x28 grayscale to match training
    img = Image.open(path).convert("L").resize((28, 28))
    arr = np.array(img, dtype=np.float32)[..., None]  # H,W,1
    return arr

def main():
    load_dotenv()
    ap = argparse.ArgumentParser()
    ap.add_argument("--endpoint_id", required=True)
    ap.add_argument("--image_path", required=True)
    args = ap.parse_args()

    project = os.getenv("PROJECT_ID")
    location = os.getenv("LOCATION", "us-central1")
    if not project:
        raise SystemExit("Set PROJECT_ID in .env")

    client = aiplatform.gapic.PredictionServiceClient(
        client_options={"api_endpoint": f"{location}-aiplatform.googleapis.com"}
    )

    arr = preprocess_28x28(args.image_path)
    # base64 encode bytes; Vertex prebuilt TF container expects instances shaped like the model input
    instance = arr.tolist()  # send raw array (SavedModel signature will map)

    endpoint = f"projects/{project}/locations/{location}/endpoints/{args.endpoint_id}"
    response = client.predict(endpoint=endpoint, instances=[instance])
    preds = np.array(response.predictions)[0]
    top = int(np.argmax(preds))
    labels = ["t-shirt/top","trouser","pullover","dress","coat","sandal","shirt","sneaker","bag","ankle_boot"]
    print(json.dumps({
        "top_label": labels[top],
        "confidence": float(preds[top]),
        "raw": preds.tolist()
    }, indent=2))

if __name__ == "__main__":
    main()
