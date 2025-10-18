import argparse, os, subprocess, sys
from dotenv import load_dotenv

def main():
    load_dotenv()
    ap = argparse.ArgumentParser()
    ap.add_argument("--model_dir", required=True, help="Path to local SavedModel dir")
    ap.add_argument("--gcs_uri", required=False, help="gs://bucket/path for model")
    args = ap.parse_args()

    bucket = os.getenv("BUCKET")
    if not args.gcs_uri:
        if not bucket:
            print("Set BUCKET in .env or pass --gcs_uri", file=sys.stderr)
            sys.exit(1)
        args.gcs_uri = f"{bucket}/models/v1/"
    print(f"→ Uploading {args.model_dir} to {args.gcs_uri}")
    subprocess.check_call(["gsutil", "-m", "cp", "-r", args.model_dir, args.gcs_uri])
    print("Done ✅")

if __name__ == "__main__":
    main()
