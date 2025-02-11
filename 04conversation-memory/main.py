import os
import time
import sys
from typing import List, Tuple, TypedDict
from dotenv import load_dotenv
from colorama import Fore, Style, init
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


load_dotenv()
# チャットモデルの初期化
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)
 

class State(TypedDict):
    messages: list[BaseMessage]


def chatbot_node(state: State) -> State:
    messages = state["messages"]
    response = llm.invoke(messages)
    new_state = {"messages": messages + [response]}
    return new_state


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


memory = MemorySaver()
app = graph_builder.compile(checkpointer=memory)


def print_typing_effect(text: str, delay: float = 0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def run_conversation():
    if not os.getenv("OPENAI_API_KEY"):
        print("エラー: OPENAI_API_KEYが環境変数に設定されていません")
        return

    config={"configurable": {"thread_id": "default"}}
    state={"messages": [SystemMessage(content="あなたは親切なAIアシスタントです。日本語で応答してください。")]}
    init()
    print(f"{Fore.GREEN}Assistant: こんにちは！何かお手伝いできることはありますか？{Style.RESET_ALL}")

    while True:
        user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}")
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"{Fore.GREEN}Assistant: さようなら！{Style.RESET_ALL}")
            break
            
        state["messages"].append(HumanMessage(content=user_input))
        state = app.invoke(state, config)
        
        print(f"{Fore.GREEN}Assistant: {Style.RESET_ALL}", end='')
        print_typing_effect(state["messages"][-1].content)

if __name__ == "__main__":
    run_conversation() 