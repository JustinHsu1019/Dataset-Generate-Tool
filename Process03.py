# 運行這支程式前，請先手動處理完 output.json
# 運行這支程式將 dataset.json 和 output.json 合併起來

import json

with open('DataTest/dataset.json', 'r', encoding='utf-8') as file:
    dataset_data = json.load(file)

with open('DataTest/output.json', 'r', encoding='utf-8') as file:
    output_data = json.load(file)

merged_data = dataset_data + output_data

with open('DataTest/merge_dataset.json', 'w', encoding='utf-8') as file:
    json.dump(merged_data, file, ensure_ascii=False, indent=4)

print("合併完成，輸出檔案為 merge_dataset.json")
