FROM python
WORKDIR /app
COPY script.py /app
RUN pip install nltk
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
COPY random_paragraphs.txt /app
CMD ["python", "script.py"]
