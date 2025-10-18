import argparse, os
from dotenv import load_dotenv
from google.cloud import aiplatform

# Prebuilt TF serving container (works for TF 2.x SavedModel)
# You can change version later if needed.
DEFAULT_SERVING_IMAGE = "us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-13:latest"

def main():
    load_dotenv()
    ap = argparse.ArgumentParser()
    ap.add_argument("--model_uri", required=True, help="gs:// path to SavedModel directory")
    ap.add_argument("--display_name", default=os.getenv("MODEL_DISPLAY_NAME", "tf-cnn-fmnist-v1"))
    ap.add_argument("--min_replicas", type=int, default=1)
    ap.add_argument("--max_replicas", type=int, default=1)
    ap.add_argument("--serving_image", default=DEFAULT_SERVING_IMAGE)
    args = ap.parse_args()

    project = os.getenv("PROJECT_ID")
    location = os.getenv("LOCATION", "us-central1")
    if not project:
        raise SystemExit("Set PROJECT_ID in .env")

    aiplatform.init(project=project, location=location)

    print("→ Uploading model to Vertex AI Model Registry...")
    model = aiplatform.Model.upload(
        display_name=args.display_name,
        artifact_uri=args.model_uri,
        serving_container_image_uri=args.serving_image,
    )
    model.wait()

    print("→ Creating endpoint...")
    endpoint = aiplatform.Endpoint.create(display_name=f"{args.display_name}-endpoint")
    endpoint.wait()

    print("→ Deploying model to endpoint...")
    endpoint = model.deploy(
        endpoint=endpoint,
        machine_type="n1-standard-2",
        min_replica_count=args.min_replicas,
        max_replica_count=args.max_replicas,
        traffic_split={"0": 100},
    )

    print("✅ Deployed!")
    print(f"Endpoint resource name: {endpoint.resource_name}")
    print(f"Endpoint ID: {endpoint.name.split('/')[-1]}")

if __name__ == "__main__":
    main()
