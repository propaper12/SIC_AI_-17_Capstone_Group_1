# Literatür Taraması — Bölüm 1, 2, 4, 5
### AI Personal Coach · Pazarlamada Yapay Zeka Bitirme Projesi

---

## 1. Giriş: Pazar Bağlamı, Tüketici Dinamikleri ve Stratejik Konumlandırma

### 1.1 Yüksek Riskli Sınav Ortamı, Veli Rehberliği Eksikliği ve İkili Kullanıcı İkilemi

Türkiye’deki Liselere Geçiş Sistemi (LGS) ve Yükseköğretim Kurumları Sınavı (YKS) gibi yüksek riskli merkezi sınavlarda, hanehalkı eğitim harcamaları 
ailelerin temel mali yatırımlarından birini oluşturur. Bu yüksek baskılı sosyo-akademik ortamda, eğitim teknolojisi (EdTech) hizmetleri genellikle yoğun bir veli 
kaygısıyla satın alınır. Ancak bu abonelik tabanlı platformlar, sisteme girişin ilk 30 ila 90 günü içinde çok ciddi bir müşteri kaybı (churn) yaşar.

Bu kaybı teşhis etmek ve çözmek için ürünün asimetrik ikili kullanıcı yapısı üzerinden incelenmesi zorunludur:

1. **Ödeyen Müşteri (Veli):** Mali yükü üstlenen, yüksek başarı kaygısı yaşayan ve çoğunlukla ailedeki eğitim yatırımlarını yöneten anneler.
Daha da önemlisi, bu veliler derin bir rehberlik eksikliği ile karşı karşıyadır: Sınava hazırlanan ergenlik çağındaki bir gence duygusal ve
akademik olarak nasıl yaklaşacaklarına dair profesyonel pedagojik bilgiye sahip değillerdir. Özel eğitim koçları ve psikologlar çok pahalıdır;
okullardaki rehberlik servisleri ise aşırı yoğunluk nedeniyle her öğrenciyle birebir ilgilenemez.
2. **Kullanan (Öğrenci):** Ders materyalleriyle doğrudan etkileşime giren, dijital dikkat dağıtıcılarla ve sınav stresiyle boğuşan,
velinin bilgisiz ve baskıcı denetimine aktif olarak direnç gösteren 13–18 yaş arası gençler.

Geleneksel EdTech modellerinde bu iki taraf birbirinden kopuk çalışır.
Öğrenci dersi erteleme veya odaklanma kaybı yaşadığında veli, pedagojik rehberlikten yoksun olduğu için içgüdüsel olarak baskıcı ve otoriter sorgulamalara başvurur. Bu rehbersiz veli tepkisi öğrenciyi dersten daha da uzaklaştırır. Deneme sınavı sonuçları durağanlaştığında ise veli uygulamanın işe yaramadığını düşünüp aboneliği iptal eder. Pazarlama diliyle söylersek: Anlık veli iletişim rehberliğinin eksikliği; ev içi çatışmayı, öğrencinin sistemden kaçışını ve veli abonelik iptalini (churn) doğrudan tetikleyen ana unsurdur.

### 1.2 Pazarlamayı Yeniden Çerçeveleme: Salt Bir Araçtan Veli Rehberliği ve Elde Tutma Motoruna

Bu proje, AI Personal Coach sistemini salt bir çalışma takibi aracı veya soru bankası olmaktan çıkarır; yapay zeka destekli bir abonelik elde tutma (retention) ve 
sürekli veli rehberliği motoru olarak konumlandırır. Sistem, ders çalışma bloklarını ve rutinleri takip ederek dersten kopma risklerini önceden tahmin eder
ve veli rehberliği boşluğunu dolduran pedagojik bildirimler üreterek ham davranış verisini yapıcı bir iletişim döngüsüne dönüştürür.

| Huni Aşaması | Ana Aktör | Sistem Hedefi | Elde Tutma Mekanizması |
| :--- | :--- | :--- | :--- |
| **Edinim & Deneme (Trial)** | Veli (Ekonomik) | Güven İnşası | Pedagojik oryantasyon ve şeffaf veri gizliliği |
| **Aktivasyon (1–14 Gün)** | Öğrenci & Veli | Alışkanlık & İş Birliği | 10 dakikalık aktivasyon kuralları + veli ipuçları |
| **Bağlılık (15–60 Gün)** | Öğrenci & Veli | Çatışmasız Rutin | Davranışsal risk puanlama modeli (LightGBM) |
| **Elde Tutma (60–90+ Gün)** | Veli (Ekonomik) | Sürdürülebilir Değer / ROI | Haftalık raporlar & LLM ile üslup dönüştürme |

### 1.3 Temel Başarı Metrikleri (KPI'lar)

Platformun optimizasyon hedefleri doğrudan ölçülebilir ticari ve davranışsal pazarlama metriklerine bağlanmıştır:

* **Birincil Ticari Metrik:** 90 Günlük Veli Elde Tutma (Retention) Oranı — Alışkanlığın ve algılanan değerin pekiştiği kritik ilk 3 aylık dönem boyunca aboneliğini aktif olarak sürdüren velilerin yüzdesi.
* **Denemeden Ücretliye Geçiş Oranı:** Ücretsiz deneme kullanıcılarının ücretli aylık abonelik paketlerine geçiş oranı.
* **Haftalık Rapor ve Rehberlik Açılma Oranı:** Velilerin otomatik ilerleme raporları ve pedagojik eylem önerileriyle etkileşim oranı.
* **Bildirim Aksiyonu Tamamlama Oranı:** Öğrenciye veya veliye iletilen dürtüklemelerin doğrulanmış bir davranışsal düzeltmeyle sonuçlanma oranı (ör. duraksayan bir dersi 10 dakika içinde başlatmak).
* **Veli-Öğrenci Diyalog Benimseme Oranı:** Velilerin sistem tarafından önerilen özerklik destekleyici iletişim kalıplarını kullanma sıklığı.
* **LTV/CAC Oranı:** Düşük dağıtım maliyetlerine karşılık ölçeklenebilir yapay zeka rehberliğinin birim ekonomisini doğrulayan finansal metrik.

---

## 2. Literatür Taramasının Organizasyonu

Sistemimizin teorik ve ampirik temeli Bölüm 3'te birbiriyle bağlantılı dört ana başlık altında toplanmıştır:

1. **Tema 1 — Bir Pazarlama Yeteneği Olarak Davranışsal Segmentasyon:** Öğrencinin neden koptuğunu teşhis etmek için demografik verilerden dinamik durum bazlı gruplamaya (başlayamayan, yarıda bırakan, telefonla dağılan, kaygıyla erteleyen, geceye kayan) geçişi inceler.
2. **Tema 2 — Churn Tahmini ve Risk Tespiti:** Zaman serisi etkileşim verilerinin, erken uyarı sinyali vermede statik demografik verilerden neden çok daha başarılı olduğunu ortaya koyar.
3. **Tema 3 — Kişiselleştirme ve Öneri Sistemleri:** Yapay zekanın müşteri bağlılığı sağlarken tüketici gözetlenme hassasiyetine (kişiselleştirme paradoksu) nasıl dikkat etmesi gerektiğini ele alır.
4. **Tema 4 — Dürtüklemeler, Bildirim Zamanlaması ve Mesaj Çerçeveleme:** Bildirimlerin baskıcı değil, özerkliği destekleyen bir üslupla yazılmasının abonelik kalıcılığı için neden kritik olduğunu açıklar.

---

## 4. Pazarlama İlişkisi, Eleştirel Sentez ve Literatürdeki Boşluklar

Literatür taraması sonucunda projemizin doldurduğu üç temel araştırma ve pazar boşluğu belirlenmiştir:

| Boşluk Boyutu | Literatürün Mevcut Durumu | AI Personal Coach Çözümü |
| :--- | :--- | :--- |
| **1. Metrik Kopukluğu** | AUC/F1 skorlarını tek başına optimize eder; ticari retention çıktısını görmezden gelir. | Risk puanlarını doğrudan veli elde tutma iş akışlarına ve ticari KPI'lara bağlar. |
| **2. Rehberlik Boşluğu** | Ham eksiklik bildirimi yapar; velilerin koçluk becerisine sahip olduğunu varsayar. | LLM destekli pedagojik koç; gerçek zamanlı üslup dönüştürme katmanı sunar. |
| **3. Gözetlenme Paradoksu** | Sınırsız arka plan takibi öğrenci tepkisine, sistemden kaçışa ve churn'e yol açar. | Yalnızca çalışma oturumlarında aktif olan şeffaf ve sınırlı odak takibi uygular. |

### Boşluk 1: Tahmin Doğruluğu (AUC) ile Pazarlama Müdahalesi Çıktıları Arasındaki Kopukluk

Churn tahmin literatürü modellerin teknik doğruluk skorlarını (AUC, F1) tek başına bir amaç gibi ele almaktadır. 
Ancak 0.91 AUC değerine sahip bir model, eğer sahadaki müdahale insan davranışını değiştiremiyorsa ticari olarak sıfır değer üretir. 
Ticari SaaS ortamlarında kopuş uyarıları genellikle müşteri zihinsel olarak sistemi terk ettikten sonra ulaşır. 
Mevcut araştırmalar, yapay zeka destekli bir bildirimin pazarlama KPI'larını (özellikle veli aksiyon tamamlama ve 90 günlük retention oranını)
doğrudan artırıp artıramadığını ölçmekte yetersiz kalmaktadır.

### Boşluk 2: Veli Rehberliği Boşluğu ve Aktif İletişim Dönüşümünün Olmaması

Okul tabanlı bildirim literatürü velilere gönderilen düşük maliyetli otomatik mesajların akademik başarısızlığı azalttığını kanıtlamıştır. 
Ancak bu çalışmalar velilerin olumsuz akademik veriyi nasıl yapıcı bir şekilde yorumlayıp aksiyona dönüştüreceğini bildiğini varsayar. 
Gerçekte ise sınav kaygısı yüksek kültürlerde veliler derin bir pedagojik koçluk desteği eksikliği yaşar. 
Özel eğitim danışmanları çok pahalıdır, okul rehberlik servisleri ise yoğunluktan her öğrenciye yetişemez.

Sonuç olarak sistemden ham bir uyarı alan kaygılı veli, pedagojik araçlara sahip olmadığı için baskıcı ve suçlayıcı bir dile başvurur. 
Gelişim psikolojisinin ortaya koyduğu gibi, kontrolcü veli tepkileri ergenin savunmaya geçmesine, sınav kaygısının artmasına ve dersi tamamen terk etmesine yol açar; 
bu da doğrudan abonelik iptaliyle sonuçlanır. Projemiz bu boşluğu LLM tabanlı bir pedagojik arabuluculuk katmanıyla kapatır: Öğrencinin neden zorlandığını davranışsal 
profillere göre veliye açıklar, veliye uygulanabilir konuşma taslakları sunar ve velinin yüksek kaygıyla yazdığı kontrolcü mesajları özerklik destekleyici diyalog önerilerine dönüştürür.

### Boşluk 3: Çocuk Takibindeki Kişiselleştirme-Gözetlenme Paradoksu

Velileri hedefleyen ticari uygulamalar genellikle cihazı arka planda sürekli izleyen istilacı yöntemlere başvurur. 
Literatürde ortaya konduğu üzere, gizli ve aşırı veri toplama tüketicide savunma tepkisi yaratarak bağlılığı ve güveni zedeler. 
Ergen yaştaki kullanıcılar için bu gözetleme, platformu tamamen reddetmeyle sonuçlanır. 
Sistemimiz bu paradoksu yalnızca öğrencinin başlattığı odaklanma bloklarında aktif olan şeffaf izleme ile çözer; böylece veri güvenliğini bir marka güveni ve müşteri elde tutma unsuru haline getirir.

---

## 5. Sonuç ve Sentez

Yüksek riskli sınav pazarlarında 90 günlük veli abonelik kalıcılığı sadece matematiksel tahmin modelleriyle ya da ham gözetleme uyarılarıyla sağlanamaz.
Bu süreç, veli rehberliği açığını kapatan bütünleşik bir sistem gerektirir.Risk tahminlerini erişilebilir ve özerkliği destekleyen bir veli koçluğuna dönüştürerek
projemiz; metrik kopukluğunu,rehberlik boşluğunu ve gözetlenmeparadoksunu çözer. Böylece kaygılı velileri çatışma kaynağından çıkarıp bilinçli birer abonelik partnerine dönüştürür.
