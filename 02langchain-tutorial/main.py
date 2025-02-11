import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage

# 環境変数を読み込む
load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY not found in environment variables")
    exit(1)

model = init_chat_model("gpt-4o-mini", model_provider="openai")

response = model.invoke(
    [
    HumanMessage(content="Hi! I'm Bob."),
    AIMessage(content="Hi Bob! How can I assist you today?"),
    HumanMessage(content="What's my name?")
    ]
    )
print(response.content)
