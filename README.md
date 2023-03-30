# Bron-Kerbosch_algorithm
#Bron-Kerbosch algoritması

Bron-Kerbosch algoritmasının kullanım amacı:

  Bron-Kerbosch algoritması, bir grafikte maksimum bağımsız küme (klik) problemini çözmek için kullanılır. Bu algoritma, bir grafikte tüm maksimum tam kümeleri (klikleri) bulmaya çalışır. Klik, grafikteki her iki düğüm arasında bir kenar olan düğüm kümesidir. Bu algoritma, ağ analizi, biyoinformatik ve sosyal ağ analizi gibi alanlarda uygulanabilir. Örneğin, sosyal ağlarda, bir klik, bir grup insanın tamamen bağlantılı olduğu bir alt grup olarak düşünülebilir. Dolayısıyla, Bron-Kerbosch algoritması metin içinde bir dize veya kelime aramak için kullanılan bir arama algoritması değildir.

Bron-Kerbosch algoritmasının çalışma şekli şu şekildedir:

  Başlangıçta, tüm düğümler aday düğümler kümesine (P) ve tüm düğümler komşu düğümler kümesine (X) eklenir.
Eğer aday düğümler kümesi P ve komşu düğümler kümesi X boşsa, mevcut tıkları çıktıya yazar ve algoritmayı sonlandır.
Aday düğümler kümesi P'den bir düğüm seçilir ve bu düğümü v olarak adlandırılır.
v'nin komşularıyla aday düğümler kümesi P'nin kesişimini alarak yeni bir aday düğümler kümesi oluştur.
v'nin komşularıyla komşu düğümler kümesi X'in kesişimini alarak yeni bir komşu düğümler kümesi oluştur.
Özyinelemeli olarak Bron-Kerbosch algoritmasını bu yeni aday ve komşu düğümler kümeleriyle çağır.
v'yi aday düğümler kümesi P'den ve komşu düğümler kümesi X'e ekle.
Eğer aday düğümler kümesi P boşsa, işlemi durdur.

Algoritmanın çalışma zamanı analizi şu şekildedir:

Bron-Kerbosch algoritması, grafiğin tüm tıklarını bulmak için kullanıldığından, çalışma zamanı en kötü durumda O(3^(n/3)), n grafiğin düğüm sayısı olmak üzere, şeklinde ifade edilir. Bu durum, grafiğin tüm düğümlerinin herhangi bir düğümle bağlantılı olmadığı boş bir grafik için en kötü durum olarak kabul edilir.

En iyi durumda, grafiğin hiç tıkların olmadığı durumlar için algoritma O(n^2) zaman karmaşıklığına sahiptir. Bu, grafiğin düğümlerinin hiçbir alt kümesinin tam bağlantılı olmaması durumunda oluşur.

Ortalama durum analizi yapmak zordur, çünkü grafiklerin yapısı ve tıkların dağılımı büyük ölçüde değişkenlik gösterir. Bununla birlikte, ortalama durum analizine yaklaşmak için bazı yöntemler kullanılabilir. Öncelikle, gerçek dünya grafiklerinin bazı ortak özelliklerini göz önünde bulundurarak, algoritmanın performansı üzerindeki etkilerini değerlendirebiliriz. Gerçek dünya grafiklerinde, düğümlerin bağlantı dağılımları genellikle güç yasası dağılımı gösterir. Bu, bazı düğümlerin çok fazla bağlantıya sahip olduğu ve diğer düğümlerin daha az bağlantıya sahip olduğu anlamına gelir.

