# open first file in read mode
with open('formattedfile.txt', 'r') as f1:
    contents = f1.read()

# open second file in append mode
with open('formattedfile0.txt', 'a') as f2:
    f2.write(contents)   # append the content
