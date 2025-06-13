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
    'susah', 'sulit', 'repot', 'ribet', 'berisik', 'bising', 'sumpek',

    # Elektronik
    'panas', 'hangus', 'korslet', 'meledak', 'batrei', 'boros', 'tahan', 
    'garansi', 'hang', 'lemot', 'error', 'bluetooth', 'wifi', 'sinyal',
    'patah', 'retak', 'layar', 'mati', 'blank', 'flek', 'berat',
    
    # Fashion
    'kecilan', 'kebesaran', 'gatal', 'gerah', 'ketat', 'longgar', 'luntur',
    'sobek', 'kusut', 'kumal', 'bau', 'warna', 'fade', 'jahitan',
    'kancing', 'resleting', 'selip', 'tipis', 'transparan',
    
    # Makanan & Minuman
    'basi', 'kadaluarsa', 'jamuran', 'berulat', 'berjamur', 'tengik',
    'hambar', 'anyir', 'asam', 'pahit', 'kelebihan', 'gula', 'goreng',
    'berminyak', 'berpasir', 'berbulu', 'berkutu', 'berlendir',
    
    # Kecantikan & Kesehatan
    'iritasi', 'alergi', 'gatal', 'perih', 'panas', 'merah', 'bengkak',
    'komedo', 'jerawat', 'kemerahan', 'kering', 'mengelupas', 'ketombe',
    'rontok', 'botak', 'pecah', 'kuku', 'kaki', 'bau', 'keringat',
    
    # Rumah Tangga
    'berkarat', 'berkerak', 'penyok', 'peyot', 'berlubang', 'tumpul',
    'berjamur', 'berdebu', 'berkutu', 'rayap', 'kutu', 'berantakan',
    'berminyak', 'lengket', 'berkerak', 'tersumbat', 'mampet',
    
    # Olahraga & Outdoor
    'palsu', 'kw', 'sobek', 'robek', 'pudar', 'kempes', 'bocor',
    'berkarat', 'berbau', 'berjamur', 'licin', 'berbahaya', 'tergelincir',
    'kram', 'keseleo', 'kaku', 'pegal', 'nyeri', 'otot',
    
    # Buku & Media
    'robek', 'sobek', 'lecek', 'basah', 'berjamur', 'kuning', 'buram',
    'blur', 'error', 'hang', 'lag', 'buffering', 'putus', 'nyambung',
    'patah', 'cd', 'dvd', 'gores', 'skip', 'macet',
    
    # Lainnya
    'hilang', 'tertinggal', 'tercuri', 'terbakar', 'terkena', 'banjir',
    'tersesat', 'terlambat', 'kabur', 'tipu', 'scam', 'bodong', 'kw',
    'palsu', 'aspal', 'terkontaminasi', 'terinfeksi', 'terkena', 'virus'
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
    'sukses', 'hebat', 'keren', 'wow', 'fantastis', 'epik', 'legendaris',
    
    # Elektronik
    'canggih', 'mutakhir', 'kekinian', 'responsive', 'awet', 'tahan',
    'batrei', 'hemat', 'full', 'hd', '4k', '8k', 'hdr', 'dolby',
    'stereo', 'surround', 'nirkabel', 'bluetooth', 'fast', 'charging',
    'garansi', 'resmi', 'original', 'premium', 'sleek', 'ramping',
    
    # Fashion
    'nyaman', 'adem', 'breathable', 'anti', 'keringat', 'stretch',
    'elastis', 'size', 'standar', 'premium', 'branded', 'eksklusif',
    'limited', 'edition', 'waterproof', 'anti', 'air', 'wrinkle',
    'free', 'anti', 'luntur', 'lembut', 'halus', 'mewah',
    
    # Makanan & Minuman
    'segar', 'organik', 'natural', 'homemade', 'homegrown', 'fresh',
    'rendah', 'kalori', 'sugar', 'free', 'gluten', 'free', 'lactose',
    'free', 'halal', 'thoyyib', 'higienis', 'steril', 'pasteurisasi',
    'kaya', 'nutrisi', 'vitamin', 'mineral', 'probiotik', 'prebiotik',
    
    # Kecantikan & Kesehatan
    'hypoallergenic', 'non-comedogenic', 'dermatologist', 'tested',
    'clinical', 'proven', 'organic', 'natural', 'herbal', 'botanical',
    'fragrance', 'free', 'paraben', 'free', 'sulfate', 'free',
    'anti-aging', 'anti-wrinkle', 'brightening', 'moisturizing',
    'nourishing', 'rejuvenating', 'revitalizing',
    
    # Rumah Tangga
    'antikarat', 'tahan', 'lama', 'stainless', 'food', 'grade',
    'bpa', 'free', 'microwave', 'safe', 'dishwasher', 'safe',
    'non-stick', 'scratch', 'resistant', 'heat', 'resistant',
    'space', 'saving', 'foldable', 'adjustable', 'multifungsi',
    
    # Olahraga & Outdoor
    'waterproof', 'windproof', 'shockproof', 'dustproof', 'anti-slip',
    'breathable', 'lightweight', 'portable', 'compact', 'adjustable',
    'shock', 'absorption', 'high', 'performance', 'professional',
    'grade', 'competition', 'level', 'training', 'fitness',
    
    # Buku & Media
    'hardcover', 'limited', 'edition', 'collector', 'item', 'rare',
    'out', 'print', 'first', 'edition', 'signed', 'autographed',
    'high', 'resolution', 'bluray', 'remastered', 'uncut', 'director',
    'cut', 'special', 'features', 'bonus', 'content', 'interactive',
    
    # Lainnya
    'unik', 'langka', 'antik', 'vintage', 'retro', 'collectible',
    'handmade', 'custom', 'personalized', 'tailor', 'made', 'bespoke',
    'one', 'kind', 'exclusive', 'import', 'original', 'genuine',
    'certified', 'authentic', 'warranty', 'guarantee', 'insurance'
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

