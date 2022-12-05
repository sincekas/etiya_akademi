INVEST standartları, kaliteli bir iş listesinin olması gereken özelliklerinin bir hatırlatıcısıdır.
INVEST bize etkili bir kullanıcı hikayesinin sahip olması gereken 6 özelliği hatırlatır. "INVEST" adını bu özelliklerin baş harflerinden alır.

<img src ="images/invest.png" width="562,5" height="150">

**Independent — Gereksinim bağımsız olmalı:**

Hikayeler arasındaki bağımlılıklar önceliklendirme ve planlama problemlerine yol açar. Müşterinin yüksek öncelik verdiği hikaye, düşük öncelikli hikaye ile bağımlı olursa, hangisinin önce yapılacağına karar verilmesi problem oluşturur.

**Negotiable — Okuyan herkes aynı şeyi anlamalı:**

Kullanıcı hikayeleri, detayları ve kabul kriterleri müşteri ve geliştirme ekipleri arasındaki bir görüşmede tartışılacak ve karar verilecek olan kısa tanımlardır. Bu yüzden bir kullanıcı hikayesi üzerinde tartışılabilir olmalıdır. Hikayeler yazılı sözleşmeler gibi kati ve değişmez değildir.

Kullanıcı hikayeleri, tamamen ayrıntılı olmamalı ve üzerinden tartışılması için hatırlatıcı olduğundan tüm detayı içermemelidir. Ancak hikaye yazıldığında önemli detaylar biliniyorsa bu bilgiler hikayeye ek açıklama olarak yazılmalı.

Özetle, kullanıcı hikayeleri geliştirilecek ürün parçası için bize yol gösteren kısa bilgilerdir. Üzerinde tartıştıkça detaylandırılabilir. Değişmez olmamalı, aksine değişime adapte olmalıdır.

**Valuable — Müşteriyi doğru anlamak:**

“Kullanıcı hikayeleri değer üretmeli” demek tek başına yeterli olmuyor. Çünkü değer dediğimiz şey ürünü geliştiren ile ürünü kullanan kişi arasında farklılık gösterebiliyor. Teknik olarak değerli görünen bir şey, son kullanıcı için hiçbir değer üretmiyor olabilir. Bu yüzden kullanıcı hikayeleri bir değer üretmeli derken, o ürünü kullanacak son kullanıcılar için bir değer üretmeli olarak algılamak daha doğru olacaktır.

Bir kullanıcı hikayesinin müşteri ve kullanıcılar için değerli olmasını sağlamanın en iyi yolu ise hikayeyi onların yazmasını sağlamaktır.

**Estimable by Time — Zaman olarak tahmin edilebilir olmalı:**

Geliştirme ekibinin bir hikayenin büyüklüğünü veya geliştirmek için harcanacak süreyi tahmin edebilmeleri oldukça önemlidir. Bu bilgiye göre planlamalar yapılmaktadır. Bu yüzden de bir kullanıcı hikayesinin olması gereken özelliklerden biri tahmin edilebilir olmasıdır.

Bir hikayenin tahmin edilemez olmasının 3 genel nedeni vardır:

*Geliştiricilerin domain bilgisine sahip olmaması.
*Geliştiricilerin teknik olarak yetersiz olması.
*Hikayenin çok büyük olması

Eğer ki geliştirici ekip, hikayeyi anlamıyor veya yeterli domain bilgisine sahip değilse, hikayeyi yazan müşteri/kullanıcı ile detaylandırabilmek için üzerinde konuşmalı ve tartışmalıdır. Tahmin edilebilir olması için geliştirici ekibin hikayeyi genel olarak anlaması gerekir.

**Small enough — Küçük olmalı:**

Bir kullanıcı hikayesinin büyüklüğü, planlama ve tahminleme yapabilmek için önemli bir parametredir. Bu yüzden bir kullanıcı hikayesi, bir iterasyon içinde tamamlanabilecek kadar küçük olmalıdır.

Ürün iş listesinde büyük hikayelere “Epic” denir. Planlama ve tahminlemelerin Epic’ler üzerinden yapmak doğru sonuçlar vermeyebilir. Bu yüzden Epic’leri kullanıcı hikayelerine bölmek gerekir. Sonrasında bu küçük hikayeler üzerinden tahminleme ve planlama yapmak daha doğru olacaktır.

**Testable — Test edilebilir olmalı:**

Bir kullanıcı hikayesi test edilebilir şekilde yazılmalıdır. Bunu birçok sebebi var tabii ki. İlk akla gelen nedenlerden biri geliştiricinin neyi geliştireceğine ve hangi kurallara göre geliştirmesine yol göstermesidir. Ayrıca, testlerin başarılı geçmesi, hikayenin başarıyla geliştirildiğinin kanıtıdır aynı zamanda.

Bir hikayenin test edilebilir özelliğine en büyük katkıyı o hikayenin Kabul Kriterleri (Acceptance Criteria) sağlar. Kabul kriterleri, bir hikayenin geliştirilmesi sonucu olması istenenler ve beklenenler listesidir. Bir geliştirme eğer kabul kriterlerini sağlamıyorsa testlerden de geçmediğini ve dolayısı ile kullanıcı hikayesinin başarılı yazılmadığını gösterir. Kısaca kullanıcı hikayelerinde kabul kriterleri, test aktivitelerinde doğrudan etkilidir.

Herkes bir hikayenin tamamlanmasının nasıl doğrulanacağını anlamalı ve kabul etmelidir. Bunu yapmanın bir diğer yolu da Bitti Tanımı (Definition of DONE) oluşturmaktır. Bu tanım bir hikayenin hangi aşamalardan geçmesi gerektiğini belirtir. Test aktivitesi de bu tanım içinde olmazsa olmazdan tabii.

Önemli olan ir diğer konu ise testlerin mümkün olduğunca otomatikleştirilmesi. Projenin başlarında test aktiviteleri kolay olabilir. Proje adım adım geliştikçe kontrol edilmesi gerekenler de bir o kadar artacaktır. Dün çalışan kodun bugün çalışmaması durumuyla karşı karşıya kalabiliriz. Sorunu mümkün olan en kısa sürede bulabilecek otomatik testler, daha kaliteli ürünler çıkarmaya ve daha kısa sürede teslim etmeye katkı sağlayacaktır.
