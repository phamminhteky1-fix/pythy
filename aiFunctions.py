import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model_pool = [
    "gemini-2.5-pro",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "learnlm-2.0-flash-experimental"
]

def get_working_model(prompt):
    for model_name in model_pool:
        try:
            model = genai.GenerativeModel(model_name=model_name)
            response = model.generate_content(prompt)
            print(f"✅ Using model: {model_name}")
            return response.text
        except Exception as e:
            print(f"⚠️ Model {model_name} failed: {e}")
    return "❌ All models returned an error. My limit for using AI can be reached."

def gemini_chat():
    print("🤖 AI Chat Mode Activated!")
    print("Type your message below. Say 'bye' to exit.\n")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["bye", "goodbye", "exit", "quit", "see you", "later"]:
            print("👋 Gemini says goodbye!")
            break
        print(f"\n🤖 Gemini says:\n{get_working_model(prompt)}\n")