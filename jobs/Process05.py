# 從 Taiwan-LLama HuggingFace 下載訓練集 JSON (改名叫 trans.json)
# 處理 Taiwan-LLama 資料，並取出前 N 筆 (根據我所擴充的資料取 1:5, 我的資料1, Taiwan-LLama 資料5)

import json

with open('DataTest/trans.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

TopN = int(input("你要取出前幾筆>> "))

new_data = []

for item in data:
    conversations = item["conversations"]
    human_value = ""
    gpt_value = ""
    for convo in conversations:
        if convo["from"] == "human":
            human_value = convo["value"]
        elif convo["from"] == "gpt":
            gpt_value = convo["value"]
    new_data.append({"input": human_value, "output": gpt_value})

subset_data = new_data[:TopN]

with open('DataTest/output_trans.json', 'w', encoding='utf-8') as outfile:
    json.dump(subset_data, outfile, ensure_ascii=False, indent=4)
