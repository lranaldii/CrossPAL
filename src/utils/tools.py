import json
import os


def read_jsonl(data_path):
    input_data = []
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf8") as f:
            for line in f:
                input_data.append(json.loads(line.strip()))
    else:
        print(f"Missing {data_path}")
    return input_data


def write_jsonl(save_path, save_object, mode="a"):
    with open(save_path, mode, encoding="utf8") as f:
        for obj in save_object:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")