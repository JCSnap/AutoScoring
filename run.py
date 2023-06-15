import os
import openai
import constants

# export OPENAI_API_KEY="YOUR_API_KEY"


def format_answer_without_justification(question, model_answer, student_answer):
    template = """
        Question: {}
        Model answer: {}
        Student answer: <> {} <>

        Format:
        Score: [score]
    """.format(question, model_answer, student_answer)
    return template


openai.api_key = os.getenv("OPENAI_API_KEY")

instruction = constants.AUTOSCORING_INSTRUCTION

question = constants.QUESTION_SCIENTIFIC_METHOD

prompt = format_answer_without_justification(
    question["question"], question["model_answer"], question["student_answer"])

print("Sending request to OpenAI API...")
completion = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[
        {"role": "system", "content": instruction},
        {"role": "user", "content": prompt}
    ]
)
text = completion.choices[0].message.content

print(text)

# Find the index of "Score: "
start_index_s = text.find("Score: ")

# Extract the score value
score = text[start_index_s + len("Score: "):].strip()

print(f"Openai Score: {score}")
