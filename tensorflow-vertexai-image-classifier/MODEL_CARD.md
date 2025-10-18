# Model Card — TensorFlow CNN (Fashion-MNIST)

**Owner:** Lakshmi Achary  
**Intended Use:** Educational/portfolio demo of image classification + Vertex AI deployment.  
**Not for** medical, safety, or high-stakes decisions.

## Data
- Source: Fashion-MNIST (10 classes, 28×28 grayscale).
- Risks: grayscale, centered clothing items; not representative of real e-commerce photos.

## Model
- Architecture: Small CNN (Conv→Pool→Conv→Pool→Dense).
- Loss: SparseCategoricalCrossentropy. Optimizer: Adam.
- Export: TensorFlow SavedModel.

## Evaluation
- Reported on Fashion-MNIST test split.
- Metrics: accuracy, per-class precision/recall/F1 (see `metrics.json`), confusion matrix plot.

## Limitations
- Sensitive to lighting, cropping, non-centered objects.
- Class imbalance effects if transferring to custom datasets.

## Ethical Considerations
- Bias risk if retrained on human images or brand-specific data.
- Do not use for surveillance or any personally identifying classification.

## Versioning
- Model display name: `${MODEL_DISPLAY_NAME}`
- Artifact URI: `gs://<bucket>/models/v1/`
