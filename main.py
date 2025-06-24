import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions
from functions.call_function import call_function

def main():
    load_dotenv("apikey.env")
    api_key = os.environ.get("GEMINI_API_KEY")    
    client = genai.Client(api_key=api_key)
    max_iterations = 20

    if len(sys.argv) < 2:
        print("No prompt was provided.")
        sys.exit(1)
    
    user_prompt = sys.argv[1]
    i = 0
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    while i < max_iterations:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
        )

        for candidate in response.candidates:
            messages.append(candidate.content)
            
        verbose = False
        if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
            verbose = True

        if verbose:
            print("User prompt:", user_prompt)
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

        if response.function_calls:
            for function_call_part in response.function_calls:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
                result = call_function(function_call_part, verbose)
                messages.append(result)
        else:
            print("Response:")
            print(response.text)
            break

        i += 1

if __name__ == "__main__":
    main()

