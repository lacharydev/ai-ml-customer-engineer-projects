#!/usr/bin/env bash
set -euo pipefail

# Load .env if present
if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs -d '\n' || true)
fi

if [ -z "${PROJECT_ID:-}" ] || [ -z "${LOCATION:-}" ] || [ -z "${BUCKET:-}" ]; then
  echo "Please set PROJECT_ID, LOCATION, BUCKET in .env (see env.example)."
  exit 1
fi

echo "→ Setting gcloud project: $PROJECT_ID"
gcloud config set project "$PROJECT_ID" >/dev/null

echo "→ Enabling required APIs..."
gcloud services enable aiplatform.googleapis.com storage.googleapis.com

# Create bucket if it doesn’t exist
if ! gsutil ls -b "$BUCKET" >/dev/null 2>&1; then
  echo "→ Creating bucket $BUCKET in $LOCATION..."
  gsutil mb -l "$LOCATION" "$BUCKET"
else
  echo "→ Bucket $BUCKET already exists."
fi

echo "→ (Optional) Set ADC if you haven’t before:"
echo "   gcloud auth application-default login"
echo "Done ✅"
