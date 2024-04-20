# Use an official Python runtime as a base image
FROM python:alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and the text file into the container
COPY WordFrequencyAnalysis.py .
COPY paragraphs.txt /app/paragraphs.txt

# Install any necessary dependencies (e.g., NLTK)
RUN pip install nltk
RUN python -m nltk.downloader stopwords

# Run the Python script when the container starts
CMD ["python", "WordFrequencyAnalysis.py"]