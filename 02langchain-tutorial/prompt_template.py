from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# 環境変数を読み込む
load_dotenv()

# プロンプトテンプレートを定義
translate_template = PromptTemplate(
    input_variables=["language", "text"],
    template="Translate this text to {language}: {text}"
)

def translate_text(text: str, target_language: str) -> str:
    try:
        # ChatGPTモデルを初期化
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        
        # チェーンを作成
        chain = LLMChain(llm=llm, prompt=translate_template)
        
        # 翻訳を実行
        result = chain.run(language=target_language, text=text)
        return result
    
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        return None

if __name__ == "__main__":
    # 使用例
    text_to_translate = "Hello, how are you today?"
    target_language = "Japanese"
    
    translated_text = translate_text(text_to_translate, target_language)
    print(f"Original text: {text_to_translate}")
    print(f"Translated to {target_language}: {translated_text}")
