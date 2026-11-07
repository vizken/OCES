"""OCES CLI: oces inspect path/to/model.ifc"""
import argparse
import json
from .core import inspect_ifc

def main() -> None:
    parser = argparse.ArgumentParser(description="OCES engineering CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    inspect = sub.add_parser("inspect", help="Read IFC elements")
    inspect.add_argument("path")
    args = parser.parse_args()
    if args.command == "inspect":
        print(json.dumps(inspect_ifc(args.path), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
