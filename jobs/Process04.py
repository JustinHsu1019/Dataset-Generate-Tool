# 檢測擴充的資料是否都具有 input 和 output 屬性
# 並 print 出沒有符合需求的項目，方便手動修改或刪除該項

import json

def check_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        invalid_items = []
        for index, item in enumerate(data):
            if not ('input' in item and 'output' in item):
                invalid_items.append((index, item))

        if invalid_items:
            print("以下項目不符合要求：")
            for index, item in invalid_items:
                print(f"項目 {index + 1}: {item}")
        else:
            print("所有項目都符合要求")

filename = "DataTest/merge_dataset.json"
check_json_file(filename)
