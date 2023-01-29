import openai

# Take in summary text and GPT3 will return notated version with subgroups
def classifySummary(summaryText):
        


    file = open("backend/apiKey.txt", "r")

    # Set the API key
    openai.api_key = file.read()

    file.close()



    # Define the prompt
    prompt = "Group this paragraph into related content based on sentences in bullet points (using - ) with subheadings above each group: " + summaryText

    # Generate text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048
    )

    # Print the generated text
    return response["choices"][0]["text"]