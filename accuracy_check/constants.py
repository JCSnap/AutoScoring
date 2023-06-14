import re

QUESTION_GENERATION_INSTRUCTION = """
You are a versatile teaching assistant who teaches concepts to different levels of students. 
You are tasked to create a question for your student. You need to:
1. Follow strictly with the format of the question and do not include any explanations.
2. Scale the question difficulty accordingly to the educational level of the student.
3. Make sure the question and options are short and succinct (if any)
"""


def get_user_setting(grade, topic):
    user_setting = f"""
Language: English
Student educational level: Grade {grade}
Number of questions: 1
Question type(s): MCQ

Subtopic: {topic}
    """
    return user_setting


def get_user_setting_unscramble(grade, topic):
    user_setting = f"""
Language: English
Student educational level: Grade {grade}
Number of questions: 1
Question type(s): Unscramble

Subtopic: {topic}
"""
    return user_setting


MCQ_FORMAT = """
Format:
Subtopic: [subtopic]
Question: [your question]
Options:
A. [option 1]
B. [option 2]
C. [option 3]
D. [option 4]
Answer: [Letter of answer]
"""

UNSCRAMBLE_FORMAT = """
Format:
Subtopic: [subtopic]
Question: [your question]
Answers:
Scrambled: [scrambled set]
Answers (formatted):
1. [answer 1]
2. [answer 2]
3. so on and so forth...
"""
ACCURACY_CHECK_INSTRUCTION = """
You are a highly educated teacher in all fields of knowledge.
You are meticulous and detail-oriented. You will be given a question and an answer.
The answer is correct most of the times but it might be wrong, so you would need to look at the question and think through step by step to give the correct answer.
If the question type is MCQ, there could only be one correct answer:
1. If the answer is wrong and the correct answer is contained within the options, update the answer.
2. If the answer is wrong and none of the options contains the correct answer, update the options to include the correct answer and update the answer.
3. If the options contain multiple correct answers, remove the additional correct options and replace them with wrong options such that there is only 1 correct option and update the answer accordingly.
Follow the format of the output strictly:
My thought process: [your step-by-step process to reach the answer]
Updated: [If the answer is correct, respond with 'false', else edit the answer and options (if any) and rewrite everything, following the format given strictly.
"""

ACCURACY_CHECK_INSTRUCTION_UNSCRAMBLE = """
You are a highly educated teacher in all fields of knowledge.
You are meticulous and detail-oriented. You will be given a question, a scrambled set, and the answer(s).
The answer is correct most of the times but it might be wrong, so you would need to look at the question and think through step by step to give the correct answer.
There could be multiple scenarios you would need to update:
1. If the answer(s) is wrong, update the answer and the set if necessary.
2. If there are more correct answers that can be formed from the set, update the answers but do not update the set.
Follow the format of the output strictly:
My thought process: [your step-by-step process to reach the answer]
Updated: [If the answer is correct, respond with 'false' and do not elaborate, else edit the answer and rewrite everything, following the format given strictly.
"""

text = """
Subtopic: High Level Addition
Question: What is the sum of 2,356 + 1,875?

Options:
A. 4,131
B. 1,431
C. 3,231
D. 3,132

Answer: B
"""

TEST = """
Topic: High Level Addition
Grade: 7
Original Question: Question: What is the sum of 2,845 + 1,390?
Options:
A. 3,235
B. 4,235
C. 4,245
D. 4,145
Answer: B
Is Updated: False
Updated: Question: What is the sum of 2,845 + 1,390?
Options:
A. 3,235
B. 4,235
C. 4,245
D. 4,145
Answer: B
Time taken for accuracy check: 19.32567596435547
"""

UNSCRAMBLE_INSTRUCTION = """
You are a teacher. You will be given a topic and your student's education level. 
Your task is to create a question that requires the students to unscramble a set of words and punctuations to form a coherent answer. 
The catch is that you will provide the scrambled answer first, and your students will have to unscramble it. You need to:
1. Follow strictly with the format of the question and do not include any explanations.
2. Scale the question difficulty accordingly to the educational level of the student.
3. Make sure the answer is short and succinct.
4. Include irrelevant words/punctuations. 
5. Encapsulate each word, punctuation, or symbol in brackets []
6. Each word can only be used once when forming the answer. 
7. Encapsulate the same word in two different brackets [] if the word is used twice.
8. Note that the scrambled set may allow for 1 to 2 valid answers.
9. Scramble by words, not by letters.
10. Note that the options are case sensitive.
"""

UNSCRAMBLE_USER_ONE = """
Topic: Economics
Student educational level: 12
Number of questions: 1
Question type(s): Unscrambled
"""

UNSCRAMBLE_ASSISTANT_ONE = """
Subtopic: Supply and Demand
Question: Unscramble the words to form a valid sentence about the law of demand and supply.
Answers:
1. The price increases when demand increases.
2. The price decreases when supply increases.
Scrambled: [increases] [supply] [.] [demand] [what] [decreases] [?] [when] [happens] [The] [price]
Answers (formatted):
1. [The] [price] [increases] [when] [demand] [increases] [.]
2. [The] [price] [decreases] [when] [supply] [increases] [.]
"""

UNSCRAMBLE_USER_TWO = """
Topic: Math
Student educational level: 1
Number of questions: 1
Question type(s): Unscramble
"""

UNSCRAMBLE_ASSISTANT_TWO = """
Subtopic: Addition
Question: Unscramble the scrambled words to find a valid expression.
Answers:
1. 5 = 2 + 3
2. 3 + 2 = 5
Scrambled: [2] [=] [3] [+] [8] [5]
Answers (formatted):
1. [5] [=] [2] [+] [3]
2. [3] [+] [2] [=] [5]
"""


def parse(section):
    lines = section.split('\n')
    for index, line in enumerate(lines):
        if line.startswith('Updated:'):
            if 'Question:' in line:
                updated_lines = []
                for subsequent_line in lines[index:]:
                    if subsequent_line.startswith('Time taken for accuracy check:'):
                        break
                    updated_lines.append(subsequent_line)
                updated = '\n'.join(updated_lines).replace(
                    'Updated: ', '').strip()
            else:
                updated = line.split(': ')[1]
            break
    print(updated)


parse(TEST)
