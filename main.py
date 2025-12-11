import os
from dotenv import load_dotenv
from google import genai




def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    print("Hello from personalcodingagent!")
    if api_key == None:
        raise RuntimeError("API key was not found")
    
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        )
    if response.usage_metadata == None:
        raise RuntimeError("API request failed")
    
    print(
    "Why is Boot.dev such a great place to learn backend development?",
    f"Prompt tokens: {response.usage_metadata.prompt_token_count}",
    f"Response tokens: {response.usage_metadata.candidates_token_count}",
    "Response:",
    response.text,
    sep=os.linesep)
    
if __name__ == "__main__":
    main()
