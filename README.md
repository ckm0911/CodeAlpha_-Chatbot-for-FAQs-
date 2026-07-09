<<<<<<< HEAD
# FAQ Chatbot - College Life & Study Tips

A simple FAQ chatbot that answers common college-life and study-related questions using NLTK preprocessing and TF-IDF similarity matching.

## Features

- Stores a predefined list of FAQ question-answer pairs.
- Preprocesses text using NLTK.
- Matches user input with the most similar FAQ using TF-IDF and cosine similarity.
- Returns the best matching answer in a command-line chat loop.

## Requirements

- Python 3.x
- NLTK
- scikit-learn

## Installation

Install the required packages:

```bash
pip install nltk scikit-learn
```

Download the required NLTK data:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab')"
```

## How It Works

1. The chatbot loads a set of FAQ question-answer pairs.
2. It cleans and preprocesses both the FAQ questions and the user input.
3. It converts the text into TF-IDF vectors.
4. It uses cosine similarity to find the closest matching FAQ.
5. It displays the most relevant answer in the chat loop.

## Run the Project

Run the chatbot with:

```bash
python faq_chatbot.py
```

## Example Usage

```bash
You: How do I stay focused while studying?
Bot: Honestly? Put your phone in another room. Try 25 min focused, 5 min break (Pomodoro) - it's a game changer.
```

## Project Structure

```bash
faq_chatbot.py
README.md
```

## Notes

- If the chatbot cannot find a close enough match, it shows a fallback message.
- The threshold can be adjusted in the code if you want stricter or looser matching.
=======
# CodeAlpha_-Chatbot-for-FAQs-
>>>>>>> d2c1c1bb84f14ec417522b8e70af2be88bc29183
