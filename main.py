import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    parser = argparse.ArgumentParser(description="Personal Coding Agent")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    args = parser.parse_args()

    # Create new list of types.Content // types.Content contains the multi-part content of a message.
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    if api_key == None:
        raise RuntimeError("API key was not found")
    
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        )
    if response.usage_metadata == None:
        raise RuntimeError("API request failed")
    
    if args.verbose:
        print(
        f"User prompt: {args.user_prompt}",
        f"Prompt tokens: {response.usage_metadata.prompt_token_count}",
        f"Response tokens: {response.usage_metadata.candidates_token_count}",
        "Response:",
        response.text,
        sep=os.linesep)
    else:
        print(
        args.user_prompt,
        response.usage_metadata.prompt_token_count,
        response.usage_metadata.candidates_token_count,
        "Response:",
        response.text,
        sep=os.linesep)
    
if __name__ == "__main__":
    main()
