# 使用 GPT 進行訓練集資料擴充
# 這邊產生的資料需手動進行修正

import json
import configparser
import logging
import logging.config
from openai.error import RateLimitError
from langchain.schema import HumanMessage
from langchain.chat_models import AzureChatOpenAI

LOGGING_CONFIG = 'logs/logging.ini'
logging.config.fileConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['OpenAI']

config = load_config()

def do_openai(messages, retry_count=3):
    if retry_count <= 0:
        logger.error("Max retry attempts reached. Exiting.")
        print("Max retry attempts reached. Exiting.")
        return "系統發生錯誤，請通知系統管理員!"

    openAI = AzureChatOpenAI(
        openai_api_base=config['openai_api_base'],
        openai_api_version=config['openai_api_version'],
        deployment_name=config['completions_model'],
        openai_api_key=config['openai_azure_api_key'],
        openai_api_type=config['openai_api_type'],
        temperature=0,
        max_tokens=4096
    )
    try:
        res = openAI(messages)
        return res.content
    except RateLimitError:
        logger.warning("get rate limit, run again")
        print("get rate limit, run again")
        return do_openai(messages, retry_count-1)
    except Exception as e:
        logger.error(f"get error: {e}")
        print(f"get error: {e}")
        return "系統發生錯誤，請通知系統管理員!"

with open('DataTest/dataset.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

logger.info("start!")
print("start!")

for item in data:
    messages = f"""
[輸入]: {item['input']}
[輸出]: {item['output']}

幫我將 [輸入] 和 [輸出] 各自換句話說，製作 5 項
每一項都跟原始的[輸入], [輸出]很像，但是會整體來說會有所不同，就是要換句話說

範例格式:
{{  
    "input": "",
    "output": ""
}},
{{
    "input": "",
    "output": ""
}},
{{
    "input": "",
    "output": ""
}},
{{
    "input": "",
    "output": ""
}},
{{
    "input": "",
    "output": ""
}}
    """
    try:
        output = do_openai([HumanMessage(content=messages)])
        logger.info("one question")
        print("one question")
        with open('DataTest/output.json', 'a', encoding='utf-8') as f:
            f.write(str(output))
    except:
        logger.error("Error while processing one question")
        print("Error while processing one question")
