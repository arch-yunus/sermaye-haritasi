import random
import time
import sys

quotes = [
    ("Kapitalizm bir uygarlık meselesidir; yüzyılların birikimini, toplumların ruhunu ve coğrafyanın kaderini tek bir bilançoda eritir.", "Fernand Braudel"),
    ("Sermaye, ölü emektir; ancak vampir gibi, yalnızca canlı emeği emerek yaşar ve ne kadar çok emerse o kadar canlı kalır.", "Karl Marx"),
    ("Yabancı, bugün gelip yarın kalan kişidir. O, gruba dışarıdan gelir ama mekânsal olarak içine yerleşir.", "Georg Simmel"),
    ("Geçmiş, geleceği yutuyor. Mirasla devralınan servetler, üretilen servetlerden daha hızlı büyüdüğünde, kapitalizm kendi liyakat efsanesini yok eder.", "Thomas Piketty"),
    ("Kapitalizm doğası gereği yaratıcı yıkımdır. Eski yapıları durmadan yıkar, yenilerini yaratır.", "Joseph Schumpeter"),
    ("Büyük servet, kendisini göstermediğinde saygı uyandırır; gösterişe kaçtığında ise sadece kıskançlık ve öfke doğurur.", "Thorstein Veblen"),
    ("Kapitalizm ölmedi, daha kötü bir şeye dönüştü: Tekno-Feodalizm.", "Yanis Varoufakis"),
    ("Zaman paradır. İtibar paradır. Para, kendi doğası gereği üretken ve çoğalgandır.", "Benjamin Franklin / Max Weber"),
    ("Kazanmayı bilenler, koşullar henüz şekillenmeden zaferi tasarlayanlardır.", "Sun Tzu"),
    ("Servet, güçtür.", "Thomas Hobbes"),
    ("Tarih, sadece savaşların değil, mülkiyetin el değiştirmesinin kaydıdır.", "İbn Haldun")
]

def print_quote():
    quote, author = random.choice(quotes)
    
    print("\n" + "="*70)
    print("🔮 SERMAYE HARİTASI - GÜNÜN AFORİZMASI 🔮".center(70))
    print("="*70 + "\n")
    
    # Daktilo efekti
    sys.stdout.write("  \"")
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\"\n")
    
    time.sleep(0.5)
    print(f"\n      — {author}\n")
    print("="*70 + "\n")

if __name__ == "__main__":
    print_quote()
