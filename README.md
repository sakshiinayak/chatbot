# chatbot

This project implements a conversational chatbot using LangChain and the OllamaLLM model. It maintains context across interactions, providing coherent and context-aware responses. The chatbot can handle free-form conversations and continues to learn from the dialogue history until the user exits.

### Features:  
Context-Aware Responses: Keeps track of the conversation history to generate relevant replies.  
LLM Integration: Utilizes the OllamaLLM model (llama3) for natural language processing.  
Customizable Prompting: Includes a prompt template to control the model's behavior.   
Simple Interface: A command-line interface (CLI) for easy interaction.  

### How It Works:  
A chat prompt template defines how the conversation history and user input are passed to the model.  
The chatbot listens for user input and appends responses to the conversation history.  
The chatbot stops when the user types exit.  
