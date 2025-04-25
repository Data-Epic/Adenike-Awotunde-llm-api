import os
from dotenv import load_dotenv
from groq import Groq
import logging
import re

# Load the API key from .env file
load_dotenv()

# Set the API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if the API key is loaded correctly
if not groq_api_key:
    print("Error: GROQ_API_KEY not found. Please check your .env file.")
    exit()

# Set up logging
logging.basicConfig(filename="assistant.log", level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Create the class for Bank Customer Support Assistant
class BankCustomerSupportAssistant:
    def __init__(self, model="deepseek-r1-distill-llama-70b"):
        self.client = Groq(api_key=groq_api_key)
        self.model = model

    # Define a function to get response from the assistant
    def get_response(self, user_query):
        prompt = (
            "You are a courteous and knowledgeable virtual assistant for a bank. "
            "Provide clear, helpful, and friendly responses to customers' inquiries, feedback or complaints."
            f"Customer query: {user_query}"
        )

        try:
            # Pass the model into the method 
            response = self.client.chat.completions.create(
                model=self.model,  
                messages=[
                    {"role": "system", 
                     "content": ("You are a helpful, knowledgeable, and professional banking customer service assistant. "
                    "You must respond clearly, concisely, and politely to the user's question. "
                     "IMPORTANT: Do NOT include internal thoughts, reasoning steps, or <think> tags in your answer. "
                    "Only provide the final message the customer should see.")},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            # Log the full response for debugging
            logging.info(f"Full API Response: {response}")

            # Extract the assistant's reply
            assistant_reply = response.choices[0].message.content.strip()

            # Logging the interaction
            logging.info(f"Customer: {user_query}")
            logging.info(f"Assistant: {assistant_reply}")
            
            assistant_reply = re.sub(r"<think>.*?</think>", "", assistant_reply, flags=re.DOTALL).strip()

            return assistant_reply

        except Exception as e:
            # Log any exceptions that occur
            logging.error(f"Error: {e}")
            return f"Error: {e}. Please try again later."

def main():
    assistant = BankCustomerSupportAssistant()

    print("Welcome to NkBank Virtual Assistant")
    print("How can I assist you today? Type 'exit' to quit.\n")

    while True:
        user_input = input("Customer: ").strip()

        if user_input.lower() == 'exit':
            print("Assistant: Thank you for using NKBank Assistant. Have a great day!")
            break

        if not user_input:
            print("Assistant: Please enter a valid question or complaint.")
            continue

        # Get the response from the assistant
        reply = assistant.get_response(user_input)
        print(f"Assistant: {reply}\n")

if __name__ == "__main__":
    main()
