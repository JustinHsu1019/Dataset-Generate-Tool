# 運行這支程式將 output_trans.json 和 merge_dataset.json 合併起來
# (將 Taiwan-LLama 的通用訓練資料和我們自行處理的資料作合併)

import json

with open('DataTest/output_trans.json', 'r', encoding='utf-8') as file:
    output_trans = json.load(file)

with open('DataTest/merge_dataset.json', 'r', encoding='utf-8') as file:
    merge_dataset = json.load(file)

final_dataset = output_trans + merge_dataset

with open('DataTest/final_dataset.json', 'w', encoding='utf-8') as file:
    json.dump(final_dataset, file, ensure_ascii=False, indent=4)

print("合併完成，輸出檔案為 final_dataset.json")
