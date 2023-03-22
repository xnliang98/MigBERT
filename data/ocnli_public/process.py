from curses import raw
import os
import json


def load_txt(path, sep=None):
    print(f"Read text file from {path} ...")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if sep:
        print(f"Split each line with sep {sep}.")
        return [line.strip().split(sep) for line in lines]
    else:
        return [line.strip() for line in lines]

def save_txt(data, path, sep=" "):
    item_len = len(data[0])
    if item_len > 1 and sep is not None:
        data = [sep.join(d) for d in data]
    with open(path, "w", encoding="utf-8") as f:
        for line in data:
            f.writelines(line+"\n")
    print(f"Data has been saved to {path}.")

def load_json(path):
    print(f"Read text file from {path} ...")
    with open(path, "r", encoding="utf-8") as f:
        lines = json.load(f)
    return lines

def load_jsonl(path):
    print(f"Read text file from {path} ...")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [json.loads(line) for line in lines]

def save_jsonl(data, path):
    with open(path, "w", encoding="utf-8") as f:
        for line in data:
            f.writelines(json.dumps(line, ensure_ascii=False) + "\n")
    print(f"Data has been saved to {path}.")

def check_dirs(path):
    if not os.path.exists(path):
        print(f"{path} does not exist, creat it!")
        os.makedirs(path)
    return True



# raw_data = load_jsonl("data/ocnli_public/test.json")
# new_data = []
# for d in raw_data:
#     new_data.append({
#         "sentence1": d['sentence1'],
#         "sentence2": d['sentence2'],
#         "label": d['label'],
#     })
# save_jsonl(new_data, "data/ocnli_public/test.json")

raw_data = load_jsonl("data/ocnli_public/dev.json")
new_data = []
for d in raw_data:
    if d['label'] == '-':
        continue
    new_data.append(d)
save_jsonl(new_data, "data/ocnli_public/dev.json")

# raw_data = load_jsonl("data/ocnli_public/train.json")
# new_data = []
# for d in raw_data:
#     new_data.append({
#         "sentence1": d['sentence1'],
#         "sentence2": d['sentence2'],
#         "label": d['label'],
#     })
# save_jsonl(new_data, "data/ocnli_public/train.json")
# refs = [d['summary'] for d in raw_data]
# docs = [d['document'] for d in raw_data]

# cands = load_txt("/root/projects/bart/tmp/csds_final_large/generated_predictions.txt")
# cands = [c.replace(" ", "") for c in cands]

# save_txt(cands, "cands.txt")
# save_txt(refs, "refs.txt")

# import pandas as pd
# data = []
# for x, y, z in zip(docs, refs, cands):
#     data.append([x, y, z])

# data = pd.DataFrame(data)
# print(data.head())
# data.to_excel("csds_final_bart_large.xlsx")
