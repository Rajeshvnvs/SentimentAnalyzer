from textblob import TextBlob

# Step 1: Read the input file
input_file = input("Enter the source file name (e.g., File.txt): ").strip()

try:
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
except FileNotFoundError:
    print(f"File not found: {input_file}")
    exit(1)

# Step 2: Let user choose extracted words file path
extracted_file = input("Enter the output file path/name for extracted words (e.g., extracted_words.txt or D:\\somefolder\\output.txt): ").strip()

# Extract words and write them to the specified file
all_words = []
for line in lines:
    words = line.strip().split()
    all_words.extend(words)

with open(extracted_file, 'w', encoding='utf-8') as outfile:
    outfile.write(' '.join(all_words))

print(f"\nExtracted words saved to {extracted_file}")

# Step 3: Read the extracted file and perform sentiment analysis
try:
    with open(extracted_file, 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"File not found: {extracted_file}")
    exit(1)

blob = TextBlob(content)
polarity = blob.sentiment.polarity

if polarity > 0.1:
    tone = "Positive"
elif polarity < -0.1:
    tone = "Negative"
else:
    tone = "Neutral"

print("\n--- Sentiment Analysis ---")
print(f"Sentiment Score: {polarity:.2f}")
print(f"Tone Detected: {tone}")
