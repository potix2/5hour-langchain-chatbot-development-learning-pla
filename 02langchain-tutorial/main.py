import os
from typing import List
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def main():
    # Load environment variables
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables")
        return

    try:
        # Initialize the chat model
        chat = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7
        )

        # Create messages
        messages: List = [
            SystemMessage(content="You are a helpful AI assistant."),
            HumanMessage(content="What is LangChain?")
        ]

        # Get response
        response = chat(messages)
        print(response.content)

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main() 