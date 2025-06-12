NEGATIVE_WORDS = ['rusak', 'jelek', 'tidak sesuai', 'buruk', 'kecewa']
POSITIVE_WORDS = ['bagus', 'cepat', 'puas', 'baik', 'mantap']

def analyze_sentiment(text):
    for word in NEGATIVE_WORDS:
        if word in text:
            return 'Negatif', f'Mengandung kata negatif: "{word}"'
    for word in POSITIVE_WORDS:
        if word in text:
            return 'Positif', f'Mengandung kata positif: "{word}"'
    return 'Netral', 'Tidak ditemukan kata kunci kuat'
