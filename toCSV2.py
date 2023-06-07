import pandas as pd

# Open the text file and read it
with open('results2.txt', 'r') as file:
    data = file.read()

# Split the text file into separate blocks
blocks = data.split('Question: ')

# Define the columns names
columns = ["Question", "Model Answer", "Student Answer",
           "OpenAI Score", "Original Score", "Time taken for OpenAI API", "Time taken for Original API"]

# Initialize an empty list to store the data
rows = []

# Loop over each block
for block in blocks[1:]:  # We start from the second block because the first block is empty
    block = 'Question: ' + block  # Add back the 'Question: ' prefix we removed earlier

    # Split the block into lines
    lines = block.split('\n')

    # Initialize an empty dictionary to store the data for this block
    row = {}

    # Loop over each line in the block
    for line in lines:
        # Find the first colon in the line
        index = line.find(':')

        # Get the field and value
        field = line[:index].strip()
        value = line[index+1:].strip()

        # Remove any trailing 'seconds' in the 'Time taken' fields
        if 'Time taken' in field:
            value = value.replace(' seconds', '')

        # Convert the numeric fields to float
        if field in ['OpenAI Score', 'Original Score', 'Time taken for OpenAI API', 'Time taken for Original API']:
            value = float(value)

        # Add the field and value to the row dictionary
        row[field] = value

    # Add the row dictionary to the rows list
    rows.append(row)

# Create a DataFrame from the rows list
df = pd.DataFrame(rows, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('visualize2.csv', index=False)
