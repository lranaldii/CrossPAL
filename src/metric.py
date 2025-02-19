import os
import re
import numpy as np
import fire
from utils.metric import compute_result as mm
from utils.select_metric import compute_result as cm


DATA_DICT = {
    "mgsm": {
        "LANG_DICT": {
            "bn": "Bengali", 
            "de": "German",
            "es": "Spanish",
            "fr": "French",
            "ja": "Japanese",
            "ru": "Russian",
            "sw": "Swahili",
            "te": "Telugu",
            "th": "Thai",
            "zh": "Chinese"
        },
        "CrossPAL": {
            "data_path": "./mgsm/",
            "metric_mode": "CrossPAL"
        },
        "SCrossPAL": {
            "data_path": "./mgsm/",
            "metric_mode": "SCrossPAL"
        },
    },
}

def get_pred_max(data_list):
    pred_max = {}
    for j, data in enumerate(data_list):
        mes = data["message"][-1]["content"].split("A:")[-1].replace(",", "")
        pred_list = re.findall(r'-?\d+\.?\d*', mes)
        if not pred_list:
            continue
        pred = str(float(pred_list[-1]))
        pred_max.setdefault(pred, []).append({"source": j, "value": pred})
    return pred_max

def extract_max(pred_max):
    max_index, max_data = max(pred_max.items(), key=lambda item: len(item[1]), default=(None, []))
    return max_index, len(max_data)

def judge_equal(pred, answer):
    return np.isclose(float(pred), float(answer), atol=0.01)

def compute_result(input_dir, lang, mode="clsp"):
    data_all = []
    lang_list = ["en"] if mode == "CrossPAL" else ["en", "de", "es", "fr", "ja", "ru", "zh"] if mode == "SCrossPAL" else [lang]

    for lang2 in lang_list:
        for idx, x in enumerate(read_jsonl(os.path.join(input_dir, f"{lang}/{lang2}.jsonl"))):
            if len(data_all) <= idx:
                data_all.append([x])
            else:
                data_all[idx].append(x)

    total = len(data_all)
    correct = 0

    for data_list in data_all:
        pred_max = get_pred_max(data_list)
        pred, _ = extract_max(pred_max)
        answer = data_list[0]["origin"]["answer"].replace(",", "")
        if judge_equal(pred, answer):
            correct += 1

    return (correct * 100.0 / total, total) if total else (0, 0)

def main(input_dir=None, metric_mode=None, dataset_name="mgsm", exp_name="SCrossPAL"):
    exp = DATA_DICT[dataset_name][exp_name]
    LANG_DICT = DATA_DICT[dataset_name]["LANG_DICT"]
    acc = 0
    
    if input_dir is None:
        input_dir = exp["data_path"]
        metric_mode = exp["metric_mode"]
        
    results = [["Language", "Acc", "Total"]]
    compute_fn = mm if dataset_name == "mgsm" else cm
    
    for lang, lang_name in LANG_DICT.items():
        accuracy, total = compute_fn(input_dir, lang, mode=metric_mode)
        acc += accuracy
        results.append([lang_name, round(accuracy, 1), total])
    
    results.append(["AVG", round(acc / len(LANG_DICT), 1), "-"])
    
    for row in results:
        print("{:<10} {:<10} {:<10}".format(*row))

if __name__ == '__main__':
    fire.Fire(main)
