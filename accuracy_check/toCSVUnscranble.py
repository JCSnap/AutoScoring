import csv

txt_file = 'formattedfile0.txt'
csv_file = 'autoscoring_unscramble.csv'

# Define the fieldnames for the CSV file
fieldnames = ['Topic', 'Grade', 'Original Question',
              'Is Updated', 'Updated', 'Time Taken']

# Open the text file for reading
with open(txt_file, 'r') as file:
    content = file.readlines()

content = ''.join(content)

# Split the content into sections based on 'Topic:'
# [1:] to ignore the first section before the first 'Topic:'
sections = content.split('Topic:')[1:]

with open(csv_file, 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for section in sections:
        # prepend 'Topic:' to each section
        lines = ('Topic:' + section).split('\n')
        lines = [line.strip() for line in lines]  # strip whitespace

        # Initialize variables to store the field values
        topic = ""
        grade = ""
        original_question = ""
        is_updated = ""
        updated = ""
        time_taken = ""

        # Indicators to help collect multi-line fields
        is_collecting_original_question = False
        is_collecting_updated_question = False

        # Iterate through the lines of the text file
        for index, line in enumerate(lines):
            line = line.strip()
            if line.startswith('Topic:'):
                topic = line.split(': ')[1]
            elif line.startswith('Grade:'):
                grade = line.split(': ')[1]
            elif line.startswith('Original Question:'):
                is_collecting_original_question = True
                split_line = line.split(': ')
                original_question += ': '.join(split_line[1:]) + '\n'
            elif line.startswith('Is Updated:'):
                is_updated = line.split(': ')[1]
                is_collecting_original_question = False  # Stop collecting original question
            elif line.startswith('Updated:'):
                if 'Subtopic' in line:
                    is_collecting_updated_question = True
                # updated += line.split(': ')[1] + '\n'
            elif line.startswith('Time taken for accuracy check:'):
                time_taken = line.split(': ')[1]
                is_collecting_updated_question = False  # Stop collecting updated question
            elif is_collecting_original_question:
                original_question += line + '\n'  # Collect lines of the original question
            elif is_collecting_updated_question:
                updated += line + '\n'  # Collect lines of the updated question

        # Write the data for the current question into the CSV file
        writer.writerow({
            'Topic': topic,
            'Grade': grade,
            'Original Question': original_question.strip(),
            'Is Updated': is_updated,
            'Updated': updated.strip(),
            'Time Taken': time_taken
        })
