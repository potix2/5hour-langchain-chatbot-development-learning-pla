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
    template="""あなたは多言語に精通した関西人の翻訳者です。
以下のテキストを{language}に翻訳してください。翻訳は関西弁で、親しげな口調にしてください。

テキスト: {text}

翻訳:"""
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
    # ユーザーからテキストを入力
    text_to_translate = input("翻訳したい英語のテキストを入力してください: ")
    target_language = "Japanese"
    
    translated_text = translate_text(text_to_translate, target_language)
    print("\n=== 翻訳結果 ===")
    print(f"原文: {text_to_translate}")
    print(f"日本語訳: {translated_text}")
