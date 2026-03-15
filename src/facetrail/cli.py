from __future__ import annotations

import argparse
from pathlib import Path

from facetrail import __version__
from facetrail.core import FaceTrailAnalyzer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="facetrail",
        description="Scan image/video libraries, extract faces, cluster similar appearances, and create privacy-safe copies.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Analyze a file or folder and export a report.")
    scan_parser.add_argument("input", help="Image, video, or folder to process.")
    scan_parser.add_argument(
        "-o",
        "--output",
        default="output",
        help="Folder where crops, reports, and redacted media will be written.",
    )
    scan_parser.add_argument(
        "--sample-every",
        type=int,
        default=5,
        help="Process every Nth frame in videos.",
    )
    scan_parser.add_argument(
        "--min-face-size",
        type=int,
        default=64,
        help="Ignore detections smaller than this size in pixels.",
    )
    scan_parser.add_argument(
        "--cluster-threshold",
        type=float,
        default=0.92,
        help="Higher values create more clusters, lower values merge more faces.",
    )
    scan_parser.add_argument(
        "--save-redacted",
        action="store_true",
        help="Write privacy-safe copies with all detected faces blurred.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "scan":
        analyzer = FaceTrailAnalyzer(
            Path(args.output),
            sample_every=args.sample_every,
            min_face_size=args.min_face_size,
            cluster_threshold=args.cluster_threshold,
            save_redacted=args.save_redacted,
        )
        summary = analyzer.analyze(Path(args.input))
        print(f"FaceTrail finished. Faces: {summary['faces_detected']} | Clusters: {summary['people_clustered']}")
        print(f"Report: {Path(args.output) / 'report' / 'gallery.html'}")
        return 0

    parser.error("Unknown command")
    return 2
