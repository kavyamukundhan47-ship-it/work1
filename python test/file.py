# Step 1: Create file and write paragraph
file = open("info.txt", "w")
file.write("Python is a simple and powerful programming language. It is widely used for web development, data analysis, and automation.")
file.close()

# Step 2: Read file and count words
file = open("info.txt", "r")
content = file.read()
file.close()

# Step 3: Count words
words = content.split()
word_count = len(words)

# Output
print("Word Count:", word_count)