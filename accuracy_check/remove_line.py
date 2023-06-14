with open('test_result.txt', 'r') as f:
    lines = f.read().split('\n')

new_lines = []
for line in lines:
    if line.startswith('Topic:'):
        new_lines.append('\n')  # add a new line before each new segment
    if line.strip() != '':  # only add line if it is not an empty line
        new_lines.append(line.strip())  # remove extra spaces around each line

# join lines back into a single string
# remove leading/trailing new lines
formatted_text = '\n'.join(new_lines).strip()

# print or write the formatted text to a file
with open('formattedfile0.txt', 'w') as f:
    f.write(formatted_text)
