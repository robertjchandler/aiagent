import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv("apikey.env")
    api_key = os.environ.get("GEMINI_API_KEY")    
    client = genai.Client(api_key=api_key)    

    if len(sys.argv) < 2:
        print("No prompt was provided.")
        sys.exit(1)
    
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        print("User prompt:", user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()

