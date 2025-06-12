NEGATIVE_WORDS = [
    # Kualitas buruk
    'rusak', 'jelek', 'buruk', 'gagal', 'salah', 'keliru', 'cacat', 
    'pecah', 'patah', 'sobek', 'lecet', 'blur', 'buram', 'kabur',
    
    # Emosi negatif
    'kecewa', 'sedih', 'marah', 'kesal', 'jengkel', 'sebal', 'benci',
    'takut', 'khawatir', 'cemas', 'stress', 'frustasi', 'malu', 'hina',
    
    # Masalah teknis
    'error', 'hang', 'bug', 'lag', 'lemot', 'crash', 'blank',
    'mati', 'mogok', 'macet', 'tersangkut', 'kendala', 'glitch',
    
    # Penipuan/Kejahatan
    'tipu', 'scam', 'korup', 'curang', 'bohong', 'dusta', 'palak',
    'palsu', 'aspal', 'kw', 'abal', 'bodong', 'ilegal', 'haram',
    
    # Harga
    'mahal', 'rugi', 'terlalu', 'overpriced', 'menggigit', 'bangkrut',
    
    # Pelayanan
    'lambat', 'lelet', 'telat', 'lalai', 'acuh', 'cuek', 'kasar',
    'jegal', 'hambat', 'birokrasi', 'ribet', 'belit', 'diskriminasi',
    
    # Kebersihan
    'kotor', 'jorok', 'dekil', 'bau', 'amis', 'apek', 'busuk', 'lapuk',
    
    # Keamanan
    'bahaya', 'risiko', 'ancam', 'ganggu', 'bully', 'siksa', 'eksploitasi',
    
    # Kesehatan
    'sakit', 'racun', 'alergi', 'gatal', 'pusing', 'mual', 'keracunan',
    
    # Umum
    'susah', 'sulit', 'repot', 'ribet', 'berisik', 'bising', 'sumpek'
]

POSITIVE_WORDS = [
    # Kualitas baik
    'bagus', 'baik', 'mantap', 'ok', 'oke', 'solid', 'sip', 'nice',
    'sempurna', 'paripurna', 'flawless', 'impeccable', 'premium',
    
    # Emosi positif
    'puas', 'senang', 'bahagia', 'gembira', 'suka', 'cinta', 'bangga',
    'haru', 'terharu', 'tenteram', 'tenang', 'nyaman', 'aman', 'legah',
    
    # Kecepatan
    'cepat', 'instan', 'realtime', 'responsif', 'gesit', 'cekatan',
    
    # Pelayanan
    'ramah', 'sopan', 'santun', 'helpful', 'supportif', 'proaktif',
    'profesional', 'ahli', 'berpengalaman', 'solutif', 'responsif',
    
    # Harga
    'murah', 'hemat', 'worth', 'terjangkau', 'promo', 'diskon', 'bonus',
    
    # Kebersihan
    'bersih', 'steril', 'higienis', 'wangi', 'harum', 'segar', 'mewah',
    
    # Keamanan
    'aman', 'protektif', 'terjamin', 'terlindungi', 'secure', 'safety',
    
    # Kesehatan
    'sehat', 'nutrisi', 'vitamin', 'organik', 'natural', 'herbal',
    
    # Fitur
    'lengkap', 'komplit', 'unggul', 'eksklusif', 'unik', 'langka',
    'inovatif', 'kreatif', 'revolusioner', 'gamechanger', 'terobosan',
    
    # Rekomendasi
    'rekomendasi', 'referensi', 'acuan', 'standar', 'role model',
    
    # Umum
    'sukses', 'hebat', 'keren', 'wow', 'fantastis', 'epik', 'legendaris'
]

def analyze_sentiment(text):
    neg_matches = [word for word in NEGATIVE_WORDS if word in text]
    pos_matches = [word for word in POSITIVE_WORDS if word in text]

    total = len(neg_matches) + len(pos_matches)

    if len(neg_matches) > len(pos_matches):
        sentiment = 'Negatif'
        reason = f'Mengandung kata negatif: {", ".join(neg_matches)}'
        confidence = len(neg_matches) / total if total > 0 else 0.5
    elif len(pos_matches) > len(neg_matches):
        sentiment = 'Positif'
        reason = f'Mengandung kata positif: {", ".join(pos_matches)}'
        confidence = len(pos_matches) / total if total > 0 else 0.5
    else:
        sentiment = 'Netral'
        reason = 'Tidak ditemukan kata kunci kuat' if total == 0 else f'Mengandung positif ({", ".join(pos_matches)}) dan negatif ({", ".join(neg_matches)}) dalam jumlah seimbang'
        confidence = 0.5

    return sentiment, reason, round(confidence, 2)

