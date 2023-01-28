import openai

text = "People are sitting 9.3 hours a day, which is more than we're sleeping at 7.7 hours. Sitting is so incredibly prevalent, we don't even question how much we're doing it. Breast cancer and colon cancer are directly tied to our lack of physical inactivity, 10% in fact on both of those, 6% for heart disease, 7% for tied to diabetes, which my father died of. So instead of going to coffee meetings or a fluorescent lit conference room meetings, I asked people to go on a walking meeting to the tune of 20 to 30 miles a week. It's changed my life. You'll be surprised at how fresh air drives fresh thinking. And in the way that you do, you'll bring into your life an entirely new set of ideas. Thank you.  What you're doing right now at this very moment is killing you. More than cars or the internet or even that little mobile device we keep talking about, the technology you're using the most almost every day is this, your TUSH."


file = open("backend/apiKey.txt", "r")

# Set the API key
openai.api_key = file.read()

file.close()



# Define the prompt
prompt = "Group this paragraph into related content based on sentences in bullet points (using - ) with subheadings above each group: " + text

# Generate text
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=2048
)

# Print the generated text
print(response["choices"][0]["text"])