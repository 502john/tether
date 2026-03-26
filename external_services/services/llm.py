from ollama import chat

def get_llm_response(conversation):
    """
    conversation: list of dicts like [{"role" : "user", "content" : "Hello World"} ,]
    """

    response = chat(
        model = "qwen2.5:14b",
        messages= conversation,
    )
    return response["message"]["content"]