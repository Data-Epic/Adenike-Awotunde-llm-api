#  🏦 NKBank Customer Support Assistant

An intelligent virtual assistant built with Python that delivers courteous and informative banking customer support, powered by the [Groq](https://groq.com/) API and the `deepseek-r1-distill-llama-70b` LLM model. It handles diverse types of customer inquiries such as complaints, inquiries, feedback and even provide insights to customers on the available product offers by the bank.


---

## 🚀 Features

- Responds to banking-related customer inquiries and complaints in a friendly, clear, and helpful manner.
- Logs conversations and errors to a log file (`assistant.log`).
- Command line interface that allows real-time interaction with the assistant.
- Uses environment variables to protect sensitive credentials.

---

## 🛠️ Setup Instructions

1. **Clone the repository:**

```
git clone https://github.com/yourusername/bank-customer-support-assistant.git
cd bank-customer-support-assistannt
```
2. Create a virtual environment and activate it.
```
python -m venv .venv
.venv\Scripts\activate
```
4. Install Dependencies
   
```pip install -r requirements.txt```

6. Create a .env file in the project root directory and add your Groq API key
   
   ```GROQ_API_KEY=your_groq_api_key_here```
   
7. Run the assistant from your terminal or command prompt
   
   ``` main.py ```

## Example Usage
- Customer: I want to get a debit card
- Assistant: Of course! To apply for a debit card, you can visit our website or mobile app, fill out the application form, and follow the prompts. Alternatively, you can visit your nearest branch or contact our customer service team for assistance. Please ensure you have your identification and account details ready. Once approved, your debit card will be mailed to you within [X] business days. If you have any questions, feel free to ask!

## Limitations
- Responses are generated using a large language model and may not reflect actual bank policies.
- Does not interact with real banking systems or databases.
- Limited to terminal-based interaction (no web or mobile interface yet).
- Requires internet access and a valid Groq API key to work.

## Future Improvements
- Integrate FAQs from a structured banking database 
- Add voice input/output capabilities.
- Create a web-based interface using Flask or Streamlit.
- Enable memory and context tracking for more natural conversations.
- Link the assistant to real backend systems for ticket logging or CRM updates.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute with attribution.

## Author

**Adenike Awotunde**  
[GitHub]()  
[LinkedIn](https://www.linkedin.com/in/adenike-awotunde-b9740b80)
Email: adenikeisblessed@gmail.com
