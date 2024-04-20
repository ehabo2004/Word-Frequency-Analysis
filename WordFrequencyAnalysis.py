import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Read the contents of the "paragraphs.txt" file
with open("paragraphs.txt", "r") as file:
    text = file.read()

# Remove punctuation and split the text into words
words = re.findall(r'\b\w+\b', text.lower())

# Remove stop words using NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Count the frequency of each word
word_counts = Counter(filtered_words)

# Display word frequency count
for word, count in word_counts.items():
    print(f"{word}: {count}")
