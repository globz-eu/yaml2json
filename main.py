#!/usr/bin/python3
import argparse
import json
import yaml
from pathlib import Path, PurePath

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert YAML file to JSON file', prog='yaml2json')
    parser.add_argument('input', type=str)
    parser.add_argument('--output', '-o', type=str, default=None)
    args = parser.parse_args()
    input = PurePath(args.input)
    if args.output:
        output = args.output
    else:
        output = input.with_suffix('.json')
    yaml_file = Path(input).open()
    json_file = Path(output).open('w')
    json.dump(yaml.safe_load(yaml_file), json_file, indent=2)
