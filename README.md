# Bron-Kerbosch_algorithm
#Bron-Kerbosch algoritması


Bron-Kerbosch algoritmasının kullanım amacı:

  Bron-Kerbosch algoritması, bir grafikte maksimum bağımsız küme (klik) problemini çözmek için kullanılır. Bu algoritma, bir grafikte tüm maksimum tam kümeleri (klikleri) bulmaya çalışır. Klik, grafikteki her iki düğüm arasında bir kenar olan düğüm kümesidir. Bu algoritma, ağ analizi, biyoinformatik ve sosyal ağ analizi gibi alanlarda uygulanabilir. Örneğin, sosyal ağlarda, bir klik, bir grup insanın tamamen bağlantılı olduğu bir alt grup olarak düşünülebilir. Dolayısıyla, Bron-Kerbosch algoritması metin içinde bir dize veya kelime aramak için kullanılan bir arama algoritması değildir.






Algoritmanın çalışma zamanı analizi şu şekildedir:

Bron-Kerbosch algoritması, grafiğin tüm tıklarını bulmak için kullanıldığından, çalışma zamanı en kötü durumda O(3^(n/3)), n grafiğin düğüm sayısı olmak üzere, şeklinde ifade edilir. Bu durum, grafiğin tüm düğümlerinin herhangi bir düğümle bağlantılı olmadığı boş bir grafik için en kötü durum olarak kabul edilir.

En iyi durumda, grafiğin hiç tıkların olmadığı durumlar için algoritma O(n^2) zaman karmaşıklığına sahiptir. Bu, grafiğin düğümlerinin hiçbir alt kümesinin tam bağlantılı olmaması durumunda oluşur.

Ortalama durum analizi yapmak zordur, çünkü grafiklerin yapısı ve tıkların dağılımı büyük ölçüde değişkenlik gösterir. Bununla birlikte, ortalama durum analizine yaklaşmak için bazı yöntemler kullanılabilir. Öncelikle, gerçek dünya grafiklerinin bazı ortak özelliklerini göz önünde bulundurarak, algoritmanın performansı üzerindeki etkilerini değerlendirebiliriz. Gerçek dünya grafiklerinde, düğümlerin bağlantı dağılımları genellikle güç yasası dağılımı gösterir. Bu, bazı düğümlerin çok fazla bağlantıya sahip olduğu ve diğer düğümlerin daha az bağlantıya sahip olduğu anlamına gelir.



Çalışma Zamanı Analizi:

Bron–Kerbosch algoritmasının çalışma zamanı, grafın yapısına göre değişiklik gösterebilir. En kötü durumda, algoritmanın çalışma zamanı O(3^(n/3)) olarak hesaplanır.

Bu hesaplama, algoritmanın rekürsif bir şekilde çalışması ve her seferinde kümenin 1/3'ünü alması nedeniyle ortaya çıkmaktadır.
Bron–Kerbosch algoritması, bir grafın tüm maksimum bağımsız küçük kümelerini (MBC) bulmak için kullanılan bir geri dönüşlü arama algoritmasıdır. Bu algoritma, bir grafın tüm maksimum bağımsız küçük kümelerini bulmanın yanı sıra, grafın yapısını inceleyerek alt küme olmayan küçük kümeleri de belirleyebilir.

Algoritmanın çalışma prensibi, her bir adımda, en son bağımsız küçük küme kümesine dahil edilemeyen bir düğümü seçmek ve bu düğümle bağlantılı olan diğer düğümleri dahil etmek için bir geri dönüşlü arama yapmaktır. Algoritma, tüm düğümleri ziyaret ettikten sonra, elde edilen maksimum bağımsız küçük kümeleri döndürür.

Bron–Kerbosch algoritmasının en kötü durumda çalışma zamanı, O(3^(n/3)) olarak hesaplanır. Bu sınırlar, grafın bağlantılarına ve boyutuna bağlı olarak değişebilir. Algoritmanın sınırlarının hesaplanması, her bir düğümün mümkün olan tüm alt kümelerinin sayısının (2^n - 1) olduğu gerçeğine dayanır


