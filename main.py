from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template="""
answer the question below

here is the conversation history:{context}

question: {question}

answer

"""

model=OllamaLLM(model="llama3")
prompt= ChatPromptTemplate.from_template(template)
chain= prompt | model

def handle_conversation():
    context=""
    print("welcome to chatbot")
    while True:
        user_input=input("you: ")
        if user_input.lower() == "exit":
            break
        result=chain.invoke({"context":context,"question":user_input})
        print("bot: ",result)
        context += f"\nUser: {user_input}\nchat:{result}"

if __name__ == "__main__":
    handle_conversation()

