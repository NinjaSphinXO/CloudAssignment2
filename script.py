import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Read the contents of the file
with open('random_paragraphs.txt', 'r') as file:
    paragraphs = file.read()

# Tokenize the text into words
words = nltk.word_tokenize(paragraphs)

# Remove punctuation marks
words = [word for word in words if word not in string.punctuation]

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Count word frequencies
word_counts = Counter(filtered_words)

# Print word frequencies to console
for word, count in word_counts.items():
    print(f"{word}: {count}")
