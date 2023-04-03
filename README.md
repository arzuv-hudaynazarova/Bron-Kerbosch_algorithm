# Bron-Kerbosch_algorithm
#Bron-Kerbosch algoritması


Bron-Kerbosch algoritmasının kullanım amacı:

 Bron-Kerbosch algoritması, bir grafikte maksimum bağımsız küme (klik) problemini çözmek için kullanılır. Bu algoritma, bir grafikte tüm maksimum tam kümeleri (klikleri) bulmayı amaçlar. Klik, grafikteki her iki düğüm arasında bir kenar olan düğüm kümesidir. Bu algoritma, ağ analizi, biyoinformatik ve sosyal ağ analizi gibi alanlarda uygulanabilir. Örneğin, sosyal ağlarda, bir klik, bir grup insanın tamamen bağlantılı olduğu bir alt grup olarak düşünülebilir. Dolayısıyla, Bron-Kerbosch algoritması metin içinde bir dize veya kelimeyi aramak için kullanılan bir arama algoritması değildir.


Algoritmanın Çalışma Şekli:

Bron-Kerbosch algoritması, geri dönüşlü (recuversive) bir şekilde çalışır ve aşağıdaki üç küme kullanarak aramayı sürdürür:

1. R: Şu ana kadar seçilmiş tüm kliğe eklenen düğümler.
2. P: Henüz keşfedilmemiş veya incelenmesi gereken kliğe ait düğümler.
3. X: Geçersiz düğümler, yani daha önce ele alınmış ve kliğe eklenmeye uygun olmayan düğümler.

Algoritma, şu adımları izler:

1. Başlangıçta, R ve X boş kümelerdir ve P, grafiğin tüm düğümlerini içerir.
2. P ve X kümelerinin kesişimi boş olduğunda, algoritma sona erer. Bu durum, tüm düğümlerin incelendiğini ve daha fazla 
   kliğin oluşturulamayacağını gösterir.
3. Algoritma, P kümesinden bir düğüm seçer ve R'ye ekler. Ardından, P kümesini, seçilen düğümle bağlantılı olan düğümlere 
   göre güncellenir. Aynı şekilde, X kümesini de güncellenir.
4. Bu güncellemelerin ardından, algoritma tekrar çalıştırılır ve adım 2'ye geri döner. Bu süreç, P kümesi boş olana kadar devam eder.
5. Tüm düğümler incelendikten sonra, algoritma R kümesindeki düğümleri içeren maksimum kümeleri (klikleri) döndürür.


Algoritmanın çalışma prensibi, her bir adımda, en son bağımsız küçük küme kümesine dahil edilemeyen bir düğümü seçmek ve bu düğümle bağlantılı olan diğer düğümleri dahil etmek için bir geri dönüşlü arama yapmaktır. Algoritma, tüm düğümleri ziyaret ettikten sonra, elde edilen maksimum bağımsız küçük kümeleri döndürür.


Algoritmanın çalışma zamanı analizi şu şekildedir:

Bron-Kerbosch algoritması, grafiğin tüm kliklerini bulmak için kullanıldığından, çalışma zamanı en kötü durumda O(3^(n/3)), n grafiğin düğüm sayısı olmak üzere, şeklinde ifade edilir. Bu durum, grafiğin tüm düğümlerinin herhangi bir düğümle bağlantılı olmadığı boş bir grafik için en kötü durum olarak kabul edilir. 
Bron–Kerbosch algoritmasının en kötü durumda çalışma zamanı, O(3^(n/3)) olarak hesaplanır. Bu sınırlar, grafiğin bağlantılarına ve boyutuna bağlı olarak değişebilir. Algoritmanın sınırlarının hesaplanması, her bir düğümün mümkün olan tüm alt kümelerinin sayısının (2^n - 1) olduğu gerçeğine dayanır.

En iyi durumda, grafiğin hiç kliklerin olmadığı durumlar için algoritma O(n^2) zaman karmaşıklığına sahiptir. Bu, grafiğin düğümlerinin hiçbir alt kümesinin tam bağlantılı olmaması durumunda oluşur.

Ortalama durum analizi yapmak zordur, çünkü grafiklerin yapısı ve kliklerin dağılımı büyük ölçüde değişkenlik gösterir. Bununla birlikte, ortalama durum analizine yaklaşmak için bazı yöntemler kullanılabilir. Öncelikle, gerçek dünya grafiklerinin bazı ortak özelliklerini göz önünde bulundurarak, algoritmanın performansı üzerindeki etkilerini değerlendirebiliriz. Gerçek dünya grafiklerinde, düğümlerin bağlantı dağılımları genellikle güç yasası dağılımı gösterir. Bu, bazı düğümlerin çok fazla bağlantıya sahip olduğu ve diğer düğümlerin daha az bağlantıya sahip olduğu anlamına gelir.

Sonuç olarak, Bron-Kerbosch algoritması genellikle yoğun olmayan grafiklerde etkilidir ve maksimal kliği bulma probleminde en hızlı algoritmalardan biridir. Bununla birlikte, algoritmanın çalışma süresi grafiğin yoğunluğuna, maksimal kliği sayısına ve bağlantı dağılımına bağlı olarak kötüleşebilir. Bu nedenle, büyük ve yoğun grafiklerde kullanılması, performans açısından bazen uygun olmayabilir.





