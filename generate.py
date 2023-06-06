import os
from flask import Flask, request, jsonify
import openai
import constants
import requests
import json
import time

# export OPENAI_API_KEY="YOUR_API_KEY"


def format_answer(question, model_answer, student_answer):
    template = """
        Question: {}
        Model answer: {}
        Student answer: <> {} <>

        Format:
        Justification: [your justification]
        Score: [score]
    """.format(question, model_answer, student_answer)

    return template


openai.api_key = os.getenv("OPENAI_API_KEY")

instruction = "You are a teacher. You will be given a question, a model answer, and a student's answer. You are tasked to grade your student's answer out of 100 based on its accuracy when compared to the model answer. There can be some leeway and the answer need not follow the model answer word for word."

questions = constants.QUESTIONS_COMPLEX_STRCUTURES

with open("results2.txt", "a") as file:
    for question in questions:
        prompt = format_answer(
            question["question"], question["model_answer"], question["student_answer"])

        print("Sending request to OpenAI API...")
        start_time_openai = time.time()
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": prompt}
            ]
        )
        text = completion.choices[0].message.content
        end_time_openai = time.time()

        print(text)
        print(f"Time taken: {end_time_openai - start_time_openai}")

        # Find the index of "Justification: "
        start_index_j = text.find("Justification: ")
        # Find the index of "Score: "
        start_index_s = text.find("Score: ")

        # Extract the justification string
        justification = text[start_index_j +
                             len("Justification: "): start_index_s].strip()

        print(f"Justification: {justification}")

        # Extract the score value
        score = text[start_index_s + len("Score: "):].strip()

        print(f"Openai Score: {score}")

        url = "https://gtfpdj13l7.execute-api.us-east-1.amazonaws.com/dev/qa"

        payload = {
            "data": [
                question["model_answer"],
                question["student_answer"],
            ]
        }

        json_payload = json.dumps(payload)

        headers = {
            "Content-Type": "application/json"
        }

        print("Sending request to Original API...")
        start_time_original = time.time()
        response = requests.post(url, data=json_payload, headers=headers)
        end_time_original = time.time()

        if response.status_code == 200:
            print("POST request successful!")
            scores = response.text
            # Parse the JSON data
            data = json.loads(scores)

            # Access the overall_score value
            overall_score = data['overall_score'][0]

            # Print the overall score
            print(f"Original Score: {overall_score}")
            print(
                f"Time taken for Original API: {end_time_original - start_time_original} seconds")
        else:
            print(
                f"POST request failed with status code: {response.status_code}")

        # Write the results to the file
        file.write("Question: " + question["question"] + "\n")
        file.write("Model Answer: " + question["model_answer"] + "\n")
        file.write("Student Answer: " + question["student_answer"] + "\n")
        file.write("OpenAI Justification: " + justification + "\n")
        file.write("OpenAI Score: " + score + "\n")
        file.write("Original Score: " + str(overall_score * 100) + "\n")
        file.write("Time taken for OpenAI API: " +
                   str(end_time_openai - start_time_openai) + " seconds\n")
        file.write("Time taken for Original API: " +
                   str(end_time_original - start_time_original) + " seconds\n\n")
