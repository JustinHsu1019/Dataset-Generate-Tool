# 將整個訓練集進行隨機打亂

import json
import random

with open('DataTest/final_dataset.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

random.shuffle(data)

with open('DataTest/dataset_shuffle.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("已隨機打亂並保存到 dataset_shuffle.json")
