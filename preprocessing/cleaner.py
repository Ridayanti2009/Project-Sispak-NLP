# cleaner.py
import re
import string
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

factory = StopWordRemoverFactory()
stopword_remover = factory.create_stop_word_remover()

def clean_text(text):
    # Lowercase
    text = text.lower()

    # Hapus angka dan tanda baca
    text = re.sub(r'[\d]', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Hapus spasi berlebih
    text = re.sub(r'\s+', ' ', text).strip()

    # Hapus stopwords
    text = stopword_remover.remove(text)

    return text
