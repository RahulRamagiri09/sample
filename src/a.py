import requests

def knowledge_base_qa(question: str):
    url = f"https://neoai.bilvantis.com/kbmsapi/answer"
    
    # Prepare form data
    form_data = {
        "question": question,
        "answer_config": "Chroma"
    }
    response = requests.post(url, data=form_data)
    return response.json().get("text2")

if __name__ == "__main__":
    question = "What is automated code"
    response = knowledge_base_qa(question)
    print(response)
