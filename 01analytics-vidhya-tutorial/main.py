import os
import time
from typing import List, Tuple
import sys
from dotenv import load_dotenv
from colorama import Fore, Style, init
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferWindowMemory
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda


def format_message(role: str, content: str) -> str:
    return f"{role.capitalize()}: {content}"


def get_chat_history(memory) -> List[Tuple[str, str]]:
    return [(msg.type, msg.content) for msg in memory.chat_memory.messages]


def print_typing_effect(text: str, delay: float = 0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def run_chatgpt_chatbot(system_prompt='', history_window=30, temperature=0.3):
    # Load environment variables
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables")
        return

    try:
        #Initialize the ChatOpenAI model
        model = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=temperature
        )
        
        #Set the system prompt
        if system_prompt:
            SYS_PROMPT = system_prompt
        else:
            SYS_PROMPT = "Act as a helpful AI Assistant"
            
        #Create the chat prompt template
        prompt = ChatPromptTemplate.from_messages([
            ('system', SYS_PROMPT),
            MessagesPlaceholder(variable_name='history'),
            ('human', '{input}')
        ])

        memory = ConversationBufferWindowMemory(
            k=history_window,
            return_messages=True
        )

        chain = (
            RunnablePassthrough.assign(
                history=lambda x: get_chat_history(x["memory"])
            ) 
            | prompt 
            | model
        )

        init()  # Initialize colorama
        print(f"{Fore.GREEN}Assistant: こんにちは！何かお手伝いできることはありますか？{Style.RESET_ALL}")

        while True:
            user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(f"{Fore.GREEN}Assistant: さようなら！{Style.RESET_ALL}")
                break
            elif user_input.strip().upper() == 'HISTORY':
                chat_history = get_chat_history(memory)
                print("\n Chat History ")
                for role, content in chat_history:
                    print(format_message(role, content))
                print(" End of History \n")
                continue
            elif user_input.strip().upper() == 'CLEAR':
                memory.clear()
                print("Chat history cleared")
                continue
            user_inp = {'input': user_input}
            start_time = time.time()
            response = chain.invoke({
                "input": user_inp,
                "memory": memory
            })
            end_time = time.time()
            
            memory.chat_memory.add_user_message(user_input)
            memory.chat_memory.add_ai_message(response.content)
            
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            print(f"{Fore.GREEN}Assistant: {Style.RESET_ALL}", end='')
            print_typing_effect(response.content)
            memory.save_context(user_inp, {'output': response.content})

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    run_chatgpt_chatbot()