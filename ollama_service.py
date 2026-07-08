from ollama import Client

client = Client("http://localhost:11434")

def chat(model: str, messages: list):

    response = client.chat(
        model=model,
        messages=messages
    )

    return response["message"]["content"]

def getModels():
    models = client.list();
    model_names = [model.model for model in models.models]
    return model_names

def connected():
    try:
        client.list()
        return True
    except:
        return False