import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download('punkt')
nltk.download('stopwords')

with open('random_paragraphs.txt', 'r') as file:
    paragraphs = file.read()

words = nltk.word_tokenize(paragraphs)

words = [word for word in words if word not in string.punctuation]

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

word_counts = Counter(filtered_words)

for word, count in word_counts.items():
    print(f"{word}: {count}")
