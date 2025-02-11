import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# 環境変数を読み込む
load_dotenv()


workflow = StateGraph(state_schema=MessagesState)
model = init_chat_model("gpt-4o-mini", model_provider="openai")

def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
config = {"configurable": {"thread_id": "abc123"}}

query = "Hi! I'm Bob."
input_messages = [HumanMessage(content=query)]
output = app.invoke({"messages":input_messages}, config)
output["messages"][-1].pretty_print()

config = {"configurable": {"thread_id": "abc234"}}
query = "What's my name?"
input_messages = [HumanMessage(content=query)]
output = app.invoke({"messages":input_messages}, config)
output["messages"][-1].pretty_print()