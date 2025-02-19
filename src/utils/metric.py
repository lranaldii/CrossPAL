import os
import re
import numpy as np
from utils.tools import read_jsonl

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
    max_data = 0
    max_index = None
    for x in pred_max:
        if len(pred_max[x]) > max_data:
            max_data = len(pred_max[x])
            max_index = x
    return max_index, max_data

def judge_equal(pred, answer):
    return np.isclose(float(pred), float(answer), atol=0.01)

def compute_result(input_dir, lang, mode="clsp"):
    data_all = []
    if mode in ["direct", "CrossPAL", "SCrossPAL"]:
        lang_list = ["en"] if mode == "CrossPAL" else ["en", "de", "es", "fr", "ja", "ru", "zh"] if mode == "SCrossPAL" else [lang]
        for lang2 in lang_list:
            for idx, x in enumerate(read_jsonl(os.path.join(input_dir, f"{lang}/{lang2}.jsonl"))):
                if len(data_all) <= idx:
                    data_all.append([x])
                else:
                    data_all[idx].append(x)
    else:
        for idx, x in enumerate(read_jsonl(os.path.join(input_dir, f"{lang}.jsonl"))):
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
