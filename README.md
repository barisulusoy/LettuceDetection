## YOLO-DARKNET İLE MARUL TESPİTİ

Yolo algoritması kullanılarak nesne tespit işlemi gerçekleştirilecek. Tüm işlemler 
sırasıyla aşağıda adımlar halinde gösterilmiştir.

### ADIM-1: "Git Bash" Kurulumu

Git Bash sayesinde Github üzerinde bulunan klasörleri bilgisayarımıza indirebilmekteyiz.
Git Bash’i indirebilmek için aşağıda verilen adrese gidilir.

https://git-scm.com/downloads 

Bu adresteki sistem sizin bilgisayarınızda hangi işletim sistemi bulunduğunu otomatik olarak
algılayacaktır. Bilgisayarınızda bulunan işletim sistemine tıklanır ve indirme işlemine başlanır.

<img align="center" src="img/img1.png">

Setup dosyası bilgisayara indikten sonra tüm adımlara Next diyerek kurulum tamamlanır.

### ADIM-2: Darknet Kurulumu

Öncelikle çalışmalarımızı yapacağımız bir klasör oluşturmamız gerekiyor. Ben D’nin altına DeepLearningProjects
isminde bir klasör oluşturdum bu klasör içerisine de LettuceDetection isminde bir klasör daha oluşturdum. 
Tüm çalışmalarımızı ve darknet’i bu klasör içerisine kuracağım. Çalışmamda marul resimlerinin bulunduğu veri
setini kullanarak marul tespiti yapacağım için LettuceDetection ismini koydum. 

Daha sonra oluşturulan LettuceDetection klasörü içerisine girilir ve mause ile sağ tıklanarak “Git Bash Here”
seçeneği seçilir ve git komut satırı açılır.

<img align="center" src="img/img2.png">

Ardından aşağıdaki şekilde gösterilen Git Bash açılır.

<img align="center" src="img/img3.png">

Git Bash açıldıktan sonra Darknet klasörlerinin bulunduğu github hesabına gitmek için aşağıdaki github adresine
gidilir. 

https://github.com/AlexeyAB/darknet 

<img align="center" src="img/img4.png">

Bu adreste yolov4 modelini eğitebilmemiz için gerekli dosyalar bulunmaktadır. Bu github adresi kopyalanır ve Git Bash’e
geri dönülür. Aşağıdaki kod satırı Git Bash üzerine yazılır:

=> git clone https://github.com/AlexeyAB/darknet 

Ardından Darknet, LettuceDetection klasörümüzün içerisine yüklenmiş olur. 

<img align="center" src="img/img5.png">

İndirilen darknet dosyasının içerisine girilir ve içerisinde bulunan Makefile dosyası Notepad ile açılır.
Daha sonra bu dosya içerisindeki bazı parametreler aşağıdaki şekilde gösterildiği gibi değiştirilir. 

<img align="center" src="img/img6.png">

Ardından darknet github hesabının olduğu siteye yeniden gidilir. İlk olarak yolov4.conv.137 dosyası bilgisayarımıza
indirilir. Ctrl+F kullanılarak bu dosya bulunabilir.

<img align="center" src="img/img7.png">

İkinci olarak yine bu adreste bulunan yolov4.weights dosyası bilgisayarımıza indirilir.

<img align="center" src="img/img8.png">

Daha sonra indirilen bu iki dosya darknet içerisine kaydedilir.

<img align="center" src="img/img9.png">

Darknet klasörü içerisinde bulunan cfg dosyası açılır. Bu dosya içerisindeki yolov4.cfg dosyası kopyalanır
ve darknet klasörü içerisine yapıştırılır. Bu klasörün ismi lettuce_yolov4.cfg olarak değiştirilir.

<img align="center" src="img/img10.png">

<img align="center" src="img/img11.png">

Daha sonra lettuce_yolov4.cfg dosyası not defteri ile açılır ve aşağıdaki değişiklikler yapılır:

<img align="center" src="img/img12.png">

Yukarıdaki değişiklikler yapıldıktan sonra Ctrl+F yaparak arama bölümü açılır. “class” kelimesi aratılır.
Cfg dosyası içerisindeki tüm class parametrelerinin değiştirilmesi gerekmektedir. Veri setinde kaç adet 
sınıf varsa bu değer class parametresine yazılır. Bizim modelimizde sadece marul resimleri olduğu için class 
parametremize 1 değeri atanacaktır. Ayrıca filters parametresi de class değerinin 5 fazlasının 3 katı olması 
gerekmektedir (filters = (class+5)*3).

<img align="center" src="img/img13.png">

<img align="center" src="img/img14.png">

<img align="center" src="img/img15.png">

### ADIM-3: Veri Setini Oluşturma

İlk olarak veri setinde bulunacak resimleri saklayacağımız dosyayı oluşturalım. Dosyayı LettuceDetection 
klasörü içerisinde lettuce_images isminde oluşturacağız.

<img align="center" src="img/img16.png">

