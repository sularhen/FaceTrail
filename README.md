# FaceTrail

![FaceTrail banner](assets/banner.svg)

FaceTrail is a cross-platform CLI for face extraction, clustering, visual reports, and privacy-safe media exports. It turns a folder of images or videos into a practical review workspace, and it was rebuilt from the original `PythonFaceTracker` idea into something cleaner, easier to install, and actually ready to share.

## Why this is useful

- Review who appears across a media folder without manually scrubbing files.
- Keep the sharpest crop of each repeated face-like appearance.
- Generate HTML and JSON reports for audits, curation, or small local datasets.
- Produce redacted copies before sharing footage publicly.

## Features

- Works with single images, full folders, and videos.
- Uses OpenCV bundled Haar cascades automatically.
- Extracts face crops and scores sharpness.
- Clusters similar detections into reusable groups.
- Exports `gallery.html`, `summary.json`, and `detections.csv`.
- Saves blurred privacy-safe image or video copies when requested.

## Installation

Linux and macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

## Release Packages

This repository now includes a release packer that always generates:

- `dist/facetrail-windows-vX.Y.Z.zip`
- `dist/facetrail-linux-vX.Y.Z.tar.gz`

Build them with:

```bash
python scripts/build_release.py
```

## Quick start

```bash
facetrail scan ./media --output ./output --save-redacted
```

Tune it for your library:

```bash
facetrail scan ./media --output ./output --sample-every 10 --min-face-size 96 --cluster-threshold 0.95 --save-redacted
```

## Output structure

- `output/faces/`: extracted face crops.
- `output/redacted/`: optional blurred image or video copies.
- `output/report/gallery.html`: visual review gallery.
- `output/report/summary.json`: machine-readable summary.
- `output/report/detections.csv`: spreadsheet-friendly manifest.

## Command reference

```text
facetrail scan INPUT [--output OUTPUT] [--sample-every N] [--min-face-size PX] [--cluster-threshold FLOAT] [--save-redacted]
```

Recommended defaults:

- `--sample-every 5` for balanced speed on videos.
- `--min-face-size 64` for everyday phone and webcam footage.
- `--cluster-threshold 0.92` for conservative grouping.

## Practical use cases

- Privacy pass before sending event footage to clients or friends.
- Media triage for creators, journalists, and researchers.
- Local photo review to find repeated people quickly.
- Lightweight preparation step before a more advanced vision pipeline.

## Limitations

- Clustering is appearance-based and lightweight. It is not a biometric identity system.
- Haar cascades are fast and portable, but they are not state-of-the-art detectors.
- Performance depends on lighting, face angle, and source quality.

## Spanish README

The Spanish version is available in [README.es.md](README.es.md).
