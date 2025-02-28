import ollama

SELECTED_MODEL = 'qwen2.5-coder:0.5b'

response = ollama.chat(
    model=SELECTED_MODEL,
    messages=[
        {
            'role': 'user', 
            'content': ' what is the probability of pulling 4 ace of spades from a deck of cards?'
        }
    ]
)

# Print the response
print(response['message']['content'])