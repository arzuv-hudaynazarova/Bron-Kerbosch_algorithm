"""
Bron-Kerbosch algoritması, grafiklerdeki maksimum kümeleri (klikleri) bulmak için kullanılan geri dönüşlü bir arama algoritmasıdır.
Bu algoritma, metin içindeki kelime tekrarlarını saymak için kullanılacak bir arama algoritması değildir.

Burada 'alice_in_wonderland.txt' dosyasındaki belirli kelimelerin kaç kez geçtiğini gösteren basit python kodu verilmiştir.
Her hangi bir arama algoritması kullanılmamıştır. Pythonda olan hazır fonksyon count() kullanılmıştır.
"""

# "alice_in_wonderland.txt" dosyasını okuyarak içeriğini 'text' değişkenine atadım
with open("alice_in_wonderland.txt", "r") as f:
    text = f.read()

# Sayısını hesaplamak istediğim kelimeleri bir liste olarak belirledim
aranan_kelimeler = ["upon", "sigh", "Dormouse", "jury-box", "swim"]

# Her kelimenin sayısını saymak için bir döngü oluşturdum
for kelime in aranan_kelimeler:
    # "count()" yöntemiyle kelimenin sayısını hesapladım
    sayi = text.count(kelime)
    # Hesaplanan sayıyı ekrana yazdırdım
    print(f"'{kelime}' kelimesi 'alice_in_wonderland.txt' dosyasında {sayi} kez tekrar ediyor.")

    
    
