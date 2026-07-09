import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FAQS = [
    ("How do I stay focused while studying?",
     "Honestly? Put your phone in another room. Try 25 min focused, 5 min break (Pomodoro) - it's a game changer."),
    ("What's the best way to prepare for exams?",
     "Start early, don't cram. Make a summary sheet per topic and quiz yourself instead of just re-reading notes."),
    ("How can I manage my time better?",
     "Write down your top 3 tasks every morning. If it's not on the list, it's not happening today - keeps you sane."),
    ("I'm feeling stressed about assignments, what do I do?",
     "Break it into tiny steps, do the smallest one right now. Momentum kills stress way better than a to-do list does."),
    ("How do I take good notes?",
     "Don't write everything - write in your own words and leave gaps for questions. Review them within 24 hours, it sticks way better."),
    ("What should I do if I fall behind in class?",
     "Talk to your professor sooner rather than later, seriously. Also find one classmate to catch you up - don't try to fix it alone."),
    ("How can I improve my memory for studying?",
     "Spaced repetition is the secret. Review stuff after a day, then a week, then a month. Cramming just doesn't stick."),
    ("Is it okay to study at night?",
     "If you're a night owl, sure! Just protect your sleep - 6 hours before an exam beats one extra hour of studying, promise."),
    ("How do I deal with procrastination?",
     "Trick yourself: commit to just 5 minutes on the task. You'll almost always keep going once you start."),
    ("What's a good study routine?",
     "Same time, same place, every day if you can. Your brain loves routine - it makes starting way easier."),
    ("How can I stay motivated?",
     "Connect the boring task to your actual goal. Also, reward yourself after - coffee, a show, whatever works."),
    ("Should I study alone or in groups?",
     "Depends on the subject honestly. Use groups to test each other, but do the first read-through solo so you're not lost."),
    ("How do I handle exam anxiety?",
     "Deep breaths, seriously - 4 seconds in, 4 hold, 4 out. Also remind yourself: you've survived every exam so far."),
    ("What's the best way to revise before an exam?",
     "Practice past papers under timed conditions. It's way more useful than passively reading your notes again."),
    ("How many hours should I study daily?",
     "Quality beats quantity - 2-3 focused hours usually beats 6 distracted ones. Protect your focus, not just your time."),
]

def ensure_nltk_data():
    resources = ["punkt", "punkt_tab", "stopwords", "wordnet"]
    for res in resources:
        try:
            nltk.data.find(f"tokenizers/{res}" if "punkt" in res else f"corpora/{res}")
        except LookupError:
            nltk.download(res, quiet=True)

class Preprocessor:
    def __init__(self):
        ensure_nltk_data()
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean(self, text: str) -> str:
        tokens = word_tokenize(text.lower())
        tokens = [t for t in tokens if t.isalpha()]
        tokens = [t for t in tokens if t not in self.stop_words]
        tokens = [self.lemmatizer.lemmatize(t) for t in tokens]
        return " ".join(tokens)

class FAQChatbot:
    def __init__(self, faqs, similarity_threshold: float = 0.25):
        self.faqs = faqs
        self.threshold = similarity_threshold
        self.preprocessor = Preprocessor()
        questions = [q for q, _ in faqs]
        self.cleaned_questions = [self.preprocessor.clean(q) for q in questions]
        self.vectorizer = TfidfVectorizer()
        self.faq_matrix = self.vectorizer.fit_transform(self.cleaned_questions)

    def get_response(self, user_input: str) -> str:
        cleaned = self.preprocessor.clean(user_input)
        if not cleaned.strip():
            return "I didn't quite catch that - could you rephrase?"
        user_vec = self.vectorizer.transform([cleaned])
        similarities = cosine_similarity(user_vec, self.faq_matrix).flatten()
        best_idx = similarities.argmax()
        best_score = similarities[best_idx]
        if best_score < self.threshold:
            return "Hmm, I'm not sure about that one. Try asking me about studying, exams, focus, or motivation!"
        return self.faqs[best_idx][1]

def main():
    bot = FAQChatbot(FAQS)
    print("=" * 60)
    print("Hey! I'm your study buddy bot.")
    print("Ask me anything about college life, exams, or staying sane.")
    print("(type 'quit' or 'exit' to stop)")
    print("=" * 60)
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Bot: Good luck out there - you've got this!")
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()