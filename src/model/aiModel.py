import ollama


SELECTED_MODEL = 'qwen2.5-coder:0.5b'

# Function to get response from the AI model
def get_response(content):
    response = ollama.chat(
        model=SELECTED_MODEL,
        messages=[
            {
                'role': 'user', 
                'content': content
            }
        ]
    )
    return response['message']['content']