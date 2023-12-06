
import openai

def chatgpt_api(transcript):
    try:
        # Read the API key from a file
        with open("API_KEY", "r") as file:
            api_key = file.read().strip()
        openai.api_key = api_key

        # Prepare the prompt from the transcript
        prompt = str(transcript)

        # Send the prompt to ChatGPT and get the response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the generated response
        generated_response = response['choices'][0]['message']['content']
        return generated_response
    except Exception as e:
        return f"An error occurred: {str(e)}"
