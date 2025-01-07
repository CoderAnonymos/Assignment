import os

file_1_name = "Mr Diala Fell For It.txt"
file_2_name = "TestMonkey.txt"

# Step 2: Overwrite content
new_content_file_1 = "Mr. Diala couldn't believe what had happened next."
new_content_file_2 = "The TestMonkey discovered a treasure hidden in the jungle."

with open(file_1_name, "w") as file_1:
    file_1.write(new_content_file_1)

with open(file_2_name, "w") as file_2:
    file_2.write(new_content_file_2)

# Step 3: Append new content
append_content_file_1 = " He decided to investigate further, determined to uncover the truth."
append_content_file_2 = " It was guarded by a gang of mischievous monkeys."

with open(file_1_name, "a") as file_1:
    file_1.write(append_content_file_1)

with open(file_2_name, "a") as file_2:
    file_2.write(append_content_file_2)

# Step 4: Rename the files with checks for existence
new_file_1_name = "Mr Diala.txt"
new_file_2_name = "MonkeyTest.txt"

# Check if the new file already exists and delete it if necessary
if os.path.exists(new_file_1_name):
    os.remove(new_file_1_name)

if os.path.exists(new_file_2_name):
    os.remove(new_file_2_name)

os.rename(file_1_name, new_file_1_name)
os.rename(file_2_name, new_file_2_name)

# Step 5: Search for specific words
search_word_1 = "Diala"
search_word_2 = "Monkey"

with open(new_file_1_name, "r") as file_1:
    file_1_content = file_1.read()
    search_result_1 = search_word_1 in file_1_content

with open(new_file_2_name, "r") as file_2:
    file_2_content = file_2.read()
    search_result_2 = search_word_2 in file_2_content

# Step 6: Count lines, words, and characters
def count_stats(file_name):
    with open(file_name, "r") as file:
        content = file.read()
    lines = content.splitlines()
    words = content.split()
    chars = len(content)
    return len(lines), len(words), chars

line_count_1, word_count_1, char_count_1 = count_stats(new_file_1_name)
line_count_2, word_count_2, char_count_2 = count_stats(new_file_2_name)

# Step 7: Merge the files
merged_file_name = "MergedFile.txt"

with open(merged_file_name, "w") as merged_file:
    with open(new_file_1_name, "r") as file_1:
        merged_file.write(file_1.read() + "\n")
    with open(new_file_2_name, "r") as file_2:
        merged_file.write(file_2.read())

# Step 8: Do NOT delete the original files to allow reading them
# os.remove(new_file_1_name)   # Commented out to prevent deletion
# os.remove(new_file_2_name)   # Commented out to prevent deletion

# Output results
print(f"Search results for '{search_word_1}': {search_result_1}")
print(f"Search results for '{search_word_2}': {search_result_2}")
print(f"\nStatistics for {new_file_1_name}: Lines: {line_count_1}, Words: {word_count_1}, Characters: {char_count_1}")
print(f"Statistics for {new_file_2_name}: Lines: {line_count_2}, Words: {word_count_2}, Characters: {char_count_2}")
print(f"\nMerged file created: {merged_file_name}")

# Reading and displaying the new content
print(f"\nContent of {new_file_1_name}:")
with open(new_file_1_name, "r") as file_1:
    print(file_1.read())

print(f"\nContent of {new_file_2_name}:")
with open(new_file_2_name, "r") as file_2:
    print(file_2.read())

# Reading merged content
print(f"\nContent of {merged_file_name}:")
with open(merged_file_name, "r") as merged_file:
    print(merged_file.read())
