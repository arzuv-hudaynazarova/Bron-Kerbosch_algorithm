"""
Bron-Kerbosch algoritması, grafiklerdeki maksimum kümeleri (klikleri) bulmak için kullanılan geri dönüşlü bir arama algoritmasıdır.
Bu algoritma, metin içindeki kelime tekrarlarını saymak için kullanılacak bir arama algoritması değildir.
"""

# Burada 'alice_in_wonderland.txt' dosyasındaki belirli kelimelerin kaç kez geçtiğini gösteren basit python kodudur. 
# Her hangi bir arama algoritması kullanılmamıştır.

# "alice_in_wonderland.txt" dosyasını okuyarak içeriği bir dize değişkenine atarız
with open("alice_in_wonderland.txt", "r") as f:
    text = f.read()

# Sayısını hesaplamak istediğimiz kelimeleri bir liste olarak belirleriz
aranan_kelimeler = ["upon", "sigh", "Dormouse", "jury-box", "swim"]

# Her kelimenin sayısını saymak için bir döngü oluştururuz
for kelime in aranan_kelimeler:
    # "count()" yöntemiyle kelimenin sayısını hesaplarız
    sayi = text.count(kelime)
    # Hesaplanan sayıyı ekrana yazdırırız
    print(f"'{kelime}' kelimesi 'alice_in_wonderland.txt' dosyasında {sayi} kez tekrar ediyor.")

