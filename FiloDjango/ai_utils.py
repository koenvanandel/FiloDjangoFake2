import openai
from api_code import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_philosopher(question, philosopher):
    # Mapping the philosopher's name to a specific style or known works
    style_prompts = {
        "Socrates": "I am Socrates. Answer every question how Socrates would have done, using no more than 100 words per response. ",
        "Plato": "I am Plato. Answer every question how Plato would have done, using no more than 100 words per response. ",
        "Aristotle": "I am Aristotle. Answer every question how Aristotle would have done, using no more than 100 words per response. ",
    }

    prompt = style_prompts.get(philosopher, "Philosopher not found. ") + question
    response = openai.Completion.create(
      engine="gpt-3.5-turbo-instruct",
      prompt=prompt,
      max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
question = "What do you think of meditation?"
philosopher = "Socrates"
answer = ask_philosopher(question, philosopher)
print(philosopher + ":")
print(answer)