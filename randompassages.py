import random
import re

# Define the path to the text file
file_path = r"C:\Users\safee\Desktop\Dissertation\combined_text.txt"

# Read the entire text file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Split text into sentences using regular expressions
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

# Function to get random passages
def get_random_passages(sentences, num_passages=6, min_words=105, max_words=115):
    passages = []
    while len(passages) < num_passages:
        start_idx = random.randint(0, len(sentences) - 1)
        passage = []
        word_count = 0
        for i in range(start_idx, len(sentences)):
            sentence = sentences[i]
            word_count += len(sentence.split())
            passage.append(sentence)
            if min_words <= word_count <= max_words:
                passages.append(' '.join(passage))
                break
            elif word_count > max_words:
                break
    return passages

# Get random passages
random_passages = get_random_passages(sentences)

# Define the path to the output file
output_file_path = r"C:\Users\safee\Desktop\Dissertation\Random_Passages.txt"

# Write the random passages to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for i, passage in enumerate(random_passages):
        output_file.write(f"Passage {i + 1}:\n{passage}\n\n")

print("Random passages have been written to", output_file_path)
