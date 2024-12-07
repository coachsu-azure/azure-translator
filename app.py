#  參考文件
#  https://learn.microsoft.com/en-us/python/api/overview/azure/ai-translation-text-readme?view=azure-python-preview
import os
from dotenv import load_dotenv
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

# 取得環境變數
load_dotenv()
REGION = os.getenv('REGION')
KEY = os.getenv('KEY')
ENDPOINT = os.getenv('ENDPOINT')

# Azure 翻譯服務參數
SRC_LANG = "en"
DST_LANG = ["zh-hant","ja"]
TARGETS =  ["Cloud computing service is fun.", "Welcome to Soochow University"]

text_translator = TextTranslationClient(
    endpoint=ENDPOINT,
    credential=TranslatorCredential(KEY, REGION)
)

src = SRC_LANG # 來源語言
dst = DST_LANG # 目標語言(可多個)
targets = []
for target in TARGETS:
    targets.append(InputTextItem(text=target)) # 目標文字(可多個)

responses = text_translator.translate(content=targets, to=dst, from_parameter=src)

for response in responses:
    print(response)
