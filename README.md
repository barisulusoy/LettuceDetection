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

Artık veri setimiz için resimleri toplamaya başlayacağız. Veri setinde bulunacak resimlerin 416x416
boyutundan fazla olmasına dikkat ediniz.

Veri setiniz için yeterli sayıda resim bulamıyorsanız aşağıda göstermiş olduğum kod satırları ile veri
setinizde bulunan resimleri arttırabilirsiniz. Bu yüzden Google Colab’ı açalım ve ilk olarak aşağıdaki 
kod satırlarını kullanarak drive ile bağlantıyı gerçekleştirelim.

<img align="center" src="img/img17.png">

Veri setini arttırmak için keras kütüphanesinde bulunan sınıfları ve metotları kullanacağız.

<img align="center" src="img/img18.png">

Veri arttırma yönteminin ve hiperparametrelerin seçimi aşağıdaki kod satırında gösterilmiştir.

<img align="center" src="img/img19.png">

Veri arttırma işleminin yapılacağı görüntünün dosya okunması işlemi aşağıdaki kod satırlarında 
gösterimiştir.

<img align="center" src="img/img20.png">

Okuduğumuz resimden kaç adet darklı resim oluşturmak istiyorsak bunu for döngüsünde belirtmemiz gerekir.
Bu işlem aşağıdaki kod satırlarında gösterilmiştir. 

<img align="center" src="img/img21.png">

Veri setimiz içerisinde toplam 400 adet görüntü olacaktır. Aynı görüntülerin veri setinde bulunmamasına 
dikkat ediniz. Veri seti oluşturulduktan sonra Ctrl+A tuşu ile tüm resmiler seçilir ve resimlerden bir 
tanesine yeniden adlandır seçeneği seçilir. Böylece tüm resimlerin isimleri aynı şekilde olacaktır. 
Fakat rakamlar parantez içerisinde ve boşluklu olacaktır. Bu hata oluşturur, bu yüzden aşağıdaki kod 
satırları ile resimlerin isimleri düzenlenir. Bu kod satırları ile tek tek resimlerin elle düzeltmek 
yerine hızlıca istediğimiz isimle değiştirebiliriz.

<img align="center" src="img/img22.png">

<img align="center" src="img/img23.png">

<img align="center" src="img/img24.png">

### ADIM-4: Veri Setindeki Resimleri Etiketleme

Resimleri etiketlemek için Make Sense’i kullanacağız. Bu site açık kaynaktır ve tamamen ücretsizdir. 
Etiketlenen resimleri yolo formatında indirme imkanımız da bulunmaktadır. Bu siteye aşağıdaki linkten
ulaşabilirsiniz.

https://www.makesense.ai 

<img align="center" src="img/img25.png">

<img align="center" src="img/img26.png">

lettuce_images dosyası içerisindeki tüm resimler seçilir ve hepsi yüklenir.

<img align="center" src="img/img27.png">

<img align="center" src="img/img28.png">

<img align="center" src="img/img29.png">

Çıkan imleç ile tespit etmek istediğimiz nesnenin sınırları çizilir. Ardından "Select label" seçeneğine
tıklanır.

<img align="center" src="img/img30.png">

<img align="center" src="img/img31.png">

<img align="center" src="img/img32.png">

<img align="center" src="img/img33.png">

Veri setimizde bulunan tüm resimler yukarıdaki işlemlerden geçirilir. Tüm resimlerin doğru bir şekilde etiketlendiğinden emin olunuz.

<img align="center" src="img/img34.png">

<img align="center" src="img/img35.png">

Export seçeneğine tıklandıktan sonra .zip uzantılı klasör bilgisayarımıza indirilir. Daha sonra bu zip dosya
içerisinde bulunan txt dosyaları, veri setimizin bulunduğu lettuce_images dosyasına atılır.

<img align="center" src="img/img36.png">

Bu txt dosyalarının içerisinde tespit etmek istediğimiz marulların verilerini tutmaktadır.

### ADIM-5: Eğitim ve Test Verilerinin Oluşturulması

Öncelikle veri setimizin ve gerekli dosyaların atılacağı lettuce_data dosyasını LettuceDetection
klasörü içerisine oluşturalım. Ardından oluşturulan dosya içerisine veri setimizin bulunduğu
lettuce_images dosyasını atalım.

<img align="center" src="img/img37.png">

Not: Genel olarak sinir ağlarında verilerin %80’i eğitim, %20’si test için kullanılmaktadır.

lettuce_data dosyası içerisine lettuce_training.txt ve lettuce_testing.txt dosyalarını oluşturalım.

<img align="center" src="img/img38.png">

Oluşturulan bu txt dosyaları içerisine veri setinde bulunan resimlerin yolları girilecektir. lettuce_training.txt
dosyasına 320 adet resim yolu, lettuce_testing.txt dosyasına 80 adet resim yolu girilecektir. Bu işlemleri kolayca
yapmak için aşağıdaki kod satırlarını kullanabilirsiniz. 

    import os
    direction= os.getcwd()
    file_test=open("lettuce_testing.txt","a+",encoding="utf-8")
    file_train=open("lettuce_training.txt","a+",encoding="utf-8")
    count=1
    while (count<=320):
        file_train.write(r"lettuce_data\lettuce_image\lettuce{}.jpg".format(count)+"\n")
        count+=1
        if count==321:
            while (count<=400):
                 file_test.write(r"lettuce_data\lettuce_image\lettuce{}.jpg".format(count)+"\n")
                 count+=1

<img align="center" src="img/img39.png">

lettuce_data klasörü içerisine iki adet daha dosya oluşturulacaktır. İlk dosyanın ismi lettuce.names 
olacaktır ve bu dosya class ismini barındıracaktır. İkinci dosyanın ismi lettuce.data olacaktır ve bu 
dosya içerisinde modelimiz ile ilgili bilgiler tutulacaktır. Dosyaların isimlerini kaydetmeden önce 
txt dosyası açınız. Daha sonra dosya içeriğini düzenleyip dosya ismini kaydediniz.

<img align="center" src="img/img40.png"><img align="center" src="img/img41.png">

Son olarak lettuce_data klasörümüz aşağıdaki gibi olacaktır.

<img align="center" src="img/img42.png">

Ardından bu lettuce_data klasörünü darknet klasörümüz içerisine atalım.

<img align="center" src="img/img43.png">

Son olarak lettuce_data klasörümüzün içerisine lettuce_labels isminde bir dosya oluşturalım. 
Bu dosya içerisine de etiketleme sonucu oluşan txt dosyalarımızı yükleyelim.

<img align="center" src="img/img44.png">

### ADIM-6: Google Colab Üzerinde Eğitim İşleminin Gerçekleştirilmesi

Darknet dosyamızı sıkıştırarak .zip formatına dönüştürelim. Daha sonra da bu dosyamızı 
Drive'mıza ekleyelim.

<img align="center" src="img/img45.png">

Drive’mızda yeni bir colab projesi oluşturalım. Colab projesinin nasıl oluşturulacağını daha önceki
yazılarımda anlatmıştım. Colab dosyamızın ismi lettuce_model.ipynb olarak değiştirelim. Drive’mıza 
custom_lettuce_model isminde bir klasör oluşturalım ve zip dosyamızı bu klasör içerisine atalım. 
Ardından çalışma zamanından GPU’yu seçerek, bağlantı kurma işlemini tamamlayalım.

<img align="center" src="img/img46.png">

Aşağıdaki kod satırları yazılarak Drive ile bağlantı kurulur. 

    from google.colab import drive
    drive.mount('/content/drive')

<img align="center" src="img/img47.png">

Drive ile bağlantı kurulduğu sol taraftaki bölmeden kontrol edilebilir.

<img align="center" src="img/img48.png">

Sırasıyla aşağıdaki kod satırları yazılarak ubuntu güncellemeleri gerçekleştirilir.

    %cat /etc/lsb-release

<img align="center" src="img/img49.png">

    !apt-get update

<img align="center" src="img/img50.png">

Aşağıdaki kod satırları ile ziplenmiş dosyalarımız çıkartılır. 

    !unzip "/content/drive/MyDrive/custom_lettuce_model/darknet.zip"

<img align="center" src="img/img51.png">

Aşağıdaki kod satırı ile darknet dosya yoluna gidelim.

    % cd /content/darknet

<img align="center" src="img/img52.png">

Kodların linux'un anlayabileceği hale getirmek için aşağıdaki kod satırını yazmamız gerekmektedir.

    !sudo apt install dos2unix

<img align="center" src="img/img53.png">

    !find . -type f -print0 | xargs -0 dos2unix

<img align="center" src="img/img54.png">

Zipten çıkarmış olduğumuz dosyayı linuxda kullanabilmek için bazı işznlerin verilmesi gerekmektedir. 
Bu izinler aşağıdaki kod satırı ile sağlanır.

    !chmod +x /content/darknet

<img align="center" src="img/img55.png">

Ardından zipten çıkarmış olduğumuz darknet dosyasını aşağıdaki, kod satırı ile yapılandıralım.

    !make

<img align="center" src="img/img56.png">

Yapılandırma tamamlandıktan sonra, çıktının son satırında aşağıdaki gibi sonuç çıktıysa başarılı
bir yapılandırma gerçekleşmiş demektir.

<img align="center" src="img/img57.png">

Aşağıdaki kod satırları ile darknet test edilir.

    !./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights data/dog.jpg

<img align="center" src="img/img58.png">

<img align="center" src="img/img59.png">

Darknet dosyası içerisinde varsayılan olarak bir backup dosyası bulunmaktadır. Bu dosyayı kaldırarak 
kendi oluşturduğumuz backup dosyasını buraya ekleyeceğiz.

<img align="center" src="img/img60.png">

Backup dosyasını kaldırmadan önce Drive’mıza lettuce_weights isminde bir dosya oluşturalım. Bu dosya 
içerisine de backup isminde yeni bir dosya daha oluşturalım. Eğittiğimiz modelin ağırlıkları bu 
dosya içerisinde saklanacaktır. 

<img align="center" src="img/img61.png">

Aşağıdaki kod satırı ile mevcut backup dosyası kaldırılır.

    !rm /content/darknet/backup -r 

<img align="center" src="img/img62.png">

Ardından kendi oluşturmuş olduğumuz backup dosyası ile darknet dosyası birbirine bağlanır. Eğitim 
sonucunda oluşan ağırlıklar bu sayede oluşturmuş olduğumuz backup dosyasına atılır.

    !ln -s /content/drive/"My Drive"/lettuce_weights/backup /content/darknet

<img align="center" src="img/img63.png">

Tüm bu işlemler tamamlandıktan sonra artık eğitim işlemine başlayabiliriz. Eğitim işlemi 
için aşağıdaki kod satırı kullanılacaktır.

    !./darknet detector train lettuce_data/lettuce.data lettuce_yolov4.cfg yolov4.conv.137 -map -dont_show

<img align="center" src="img/img64.png">

Eğitim işlemi 5-6 saat sürebilir. Sabırla bekleyiniz.

Eğitim işlemi bittikten sonra backup dosyası içerisine ağırlık dosyalarımızı gelecektir. lettuce_weights 
dosyasını bilgisayarımıza indirelim. Önceden oluşturmuş olduğumuz LettuceDetection klasörü içerisine 
lettuce_model isminde bir dosya oluşturalım ve bu dosya içerisine indirmiş olduğumuz ağırlıkları atalım. 
Bu ağırlıklar arasında sadece lettuce_yolov4_last.weights dosyasını kullanacağız. O yüzden diğer dosyaları 
silebiliriz. Ayrıca bu dosya içerisine önceden düzenlemiş olduğumuz lettuce_yolov4.cfg dosyasını da 
yükleyeceğiz. Bu dosyaya darknet klasörü içerisinden erişilebilir.

<img align="center" src="img/img65.png">

Test için kullanacağımız resim ve videoları tutmak için input_frame isminde bir klasör oluşturalım. 
Test sonucunda oluşan tespit işlemlerini kaydetmek için de output_frame isminde bir klasör oluşturalım. 
Gerekli dosyalar oluşturulduktan sonra LettuceDetection klasörünün içerisi aşağıdaki gibi olacaktır.

<img align="center" src="img/img66.png">

### ADIM-6: Eğitilen Modelin Test Edilmesi

Eğitilen model üzerinde gerekli testleri yapmak için my_scripts klasörü içerisine goruntu_test_etme.py 
ismide bir python dosyası oluşturalım ve aşağıdaki kodları yazmaya başlayalım.
    
    # Gerekli kütüphanelerin eklenmesi:
    import cv2
    import numpy as np
    
    # Test edilecek görüntünün okunması:
    image = cv2.imread("D:/DeepLearningProjects/LettuceDetection/input_frame/input_lettuce1.jpg")
    
    # Test edilecek görüntünün yüksekliğinin ve genişliğinin bulunması:
    img_width = image.shape[1]
    img_height = image.shape[0]

<img align="center" src="img/img67.png">

2 numaralı satırda görüntü işleme ve bilgisayarlı görü kütüphanesi olan OpenCV; 3 numaralı satırda matris 
işlemlerinin kolay bir şekilde yapılabildiği Numpy kütüphanesi içe aktarılır.

6 numaralı satırda test edilecek görüntünün okunması işlemi gerçekleştirilir. Bu görüntü sayısal bir şekilde 
image değişkeni içerisine atılır.

9 ve 10 numaralı satırlarda test edeceğimiz görüntünün genişlik ve yükseklik değerleri gerekli değişkenlere atılır.

    # Sayısal görüntünün blob formatına dönüştürülmesi:
    img_blob = cv2.dnn.blobFromImage(image, 1/255, (416,416), swapRB=True, crop=False)
    
    # Eğitilen modelde kullanılan sınıfların diziye atılması:
    labels = ["Marul"]
    
    # Testpit edilen görüntüde farklı sınıflar bulunuyorsa; herbir farklı 
    # sınıfı farklı renkte sınırlayıcı dikdörtgen içerisine alma:
    colors = ["0,255,255","0,0,255","255,0,0","255,255,0","0,255,0"]
    colors = [np.array(color.split(",")).astype("int") for color in colors]
    colors = np.array(colors)
    colors = np.tile(colors,(18,1))

<img align="center" src="img/img68.png">

Sayısallaştırılmış görüntünün blob formata dönüştürülmesi gerekmektedir. 13 numaralı satırda sayısal 
görüntü blob formata dönüştürülmektedir. Blob, görünütünün 4 boyutlu tensörlere çevrilmiş halidir. 
Daha önceki yazılarımda tensör kavramına değinmiştim. Elimizde 8 bitlik bir görüntü bulunduğu için 
1/255 ile renk sayısı oranlanır. Eğitim setinde 416x416’lık görüntüleri kullandığımız için görüntünün 
boyutunu değiştiririz. swapRB, parametresi ile de görüntü RGB formattan BGR formata dönüştürülür. 

16 numaralı satırda, eğitim setinde kullandığımız sınıflar label dizisi içerisine atanır.

20 ve 23 numaralı satırlar arasında bulunan kodlar sayesinde testpit edilen görüntüde farklı sınıflar 
bulunuyorsa; her bir farklı sınıfı farklı renkte sınırlayıcı dikdörtgen içerisine alınır.

    # Eğitmiş olduğumuz modelin yüklenmesi:
    model = cv2.dnn.readNetFromDarknet("D:/DeepLearningProjects/LettuceDetection/lettuce_model/lettuce_yolov4.cfg",
                                "D:/DeepLearningProjects/LettuceDetection/lettuce_model/lettuce_yolov4_last.weights")
    
    # Bizi sadece çıktı katmanları ilgilendirdiği için çıktı katmanı seçilir. 
    # getUnconnectedOutLayers metodu çıktı katmanlarını bulur.
    layers = model.getLayerNames()
    output_layer = [layers[layer[0]-1] for layer in model.getUnconnectedOutLayers()]
    
    # Blob'a dönüştürmüş olduğumuz görüntü eğitilmiş modele input olarak verilir.
    model.setInput(img_blob)
    
    # Çıktı katmanı içerisindeki değerlere erişilir:
    detection_layers = model.forward(output_layer)
    
    # NON-MAXIMUM SUPPRESSION (OPERATION-1):
    ids_list = [] # predict id'leri tutar
    boxes_list = [] # bounding box özellikkerini tutar 
    confidences_list = [] # doğruluk (accuracy) değerlerini tutar
    # OPERATION-1'in bitişi

<img align="center" src="img/img69.png">

26 numaralı satırda Google Colab’da eğitmiş olduğumuz modelimiz yüklenir.

31 ve 32 numaralı satırlarda çıktı katmanı seçilir. Testimizi kontrol edebilmek için çıktı 
katmanında oluşan değerler bizim için önemlidir. 

35 numaralı satırda Blob’a dönüştürmüş olduğumuz görüntü eğitilmiş modele input olarak verilir.

38 numaralı satırda çıktı katmanındaki test için gerekli değerlere ulaşılır.

41, 42 ve 43 numaralı satırlardaki diziler ile NON-MAXIMUM SUPPRESSION yöntemi uygulanacaktır. 
NON-MAXIMUM SUPPRESSION yöntemi sayesinde en yüksek doğruluk oranına sahip nesne sınırlayıcı 
dikdörtgen ile sınırlandırılabilir. 

    # Çıktı katmanı değerlerinin tutulduğu dizi elemanları sırasıyla döndürülür:
    for detection_layer in detection_layers:
        
        for object_detection in detection_layer:
            
            # "object_detection" içerisindeki ilk 5 değer boundingBox ile ilgilidir.
            # 5'den sonraki değerler tahmin oranı ile ilgilidir.
            scores = object_detection[5:]
            
            # Tahmin oranları içerisindeki en büyük değer alınır. 
            predicted_id = np.argmax(scores)
            confidence = scores[predicted_id]
            
            # Belirlenen tahmin değerinden büyük değerlerin alınması:
            if confidence > 0.20:
                
                # Tespit edilen nesnelerin isimlerinin atandığı dizi:
                label = labels[predicted_id]
                
                # Tespit edilen nesnelerin sınır dikdörtgenlerinin bulunması:
                bounding_box = object_detection[0:4] * np.array([img_width,img_height,img_width,img_height])
                (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")
                start_x = int(box_center_x - (box_width/2))
                start_y = int(box_center_y - (box_height/2))
                
                # NON-MAXIMUM SUPPRESSION (OPERATION-2):
                ids_list.append(predicted_id)
                confidences_list.append(float(confidence))
                boxes_list.append([start_x, start_y, int(box_width), int(box_height)])
                # OPERATION-2'nin bitişi
                
                # Tespit işlemi burada bitti ve tespit edilen nesneler
                # NON-MAXIMUM SUPPRESSION dizileri içerisine kaydedildi. 

<img align="center" src="img/img70.png">

47 ve 49 numaralı satırlarda çıktı katmanı değerlerinin tutulduğu dizi elemanları sırasıyla döndürülür.

object_detection içerisindeki ilk 5 değer boundingBox (sınırlayıcı dikdörtgen) ile ilgilidir. Bu değerler 
53 numaralı satırda scores dizisi içerisine atanır. 5’den sonraki değerler tahmin oranı ile ilgilidir.

56 ve 57 numaralı satırlarda tahmin oranları içerisindeki en büyük değer alınır. 

63 numaralı satırda tespit edilen nesnelerin isimleri label dizisi içerisine atanır.

66 ve 69 numaralı satırlar arasında tespit edilen nesnelerin sınırlayıcı dikdörtgenleri bulunmaktadır.

72, 73 ve 74 numaralı satırlarda NON-MAXİMUM SUPPRESSION yönteminin ikinci adımı gerçekleştirilmiştir. 
Bu işlem de gerçekleştirildikten sonra tespit işlemi tamamlanır.

    # NON-MAXIMUM SUPPRESSION (OPERATION-3):
    # NMSBoxes methodu en yüksek güvenilirliğe sahip dikdörtgenlerin id'lerini döndürmektedir. 
    max_ids = cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5, 0.4)
         
    for max_id in max_ids:
        
        max_class_id = max_id[0]
        box = boxes_list[max_class_id]
    
        start_x = box[0] 
        start_y = box[1] 
        box_width = box[2] 
        box_height = box[3] 
         
        predicted_id = ids_list[max_class_id]
        label = labels[predicted_id]
        confidence = confidences_list[max_class_id]
        # OPERATION-3'nin bitişi
                
        end_x = start_x + box_width
        end_y = start_y + box_height
                
        box_color = colors[predicted_id]
        box_color = [int(each) for each in box_color]
                     
        label = "{}: {:.2f}%".format(label, confidence*100)
        print("predicted object {}".format(label))
         
        cv2.rectangle(image, (start_x,start_y),(end_x,end_y),box_color,4)
        cv2.putText(image,label,(start_x,start_y-10), cv2.FONT_HERSHEY_SIMPLEX, 4, box_color, 4)

    cv2.imwrite("D:/DeepLearningProjects/LettuceDetection/output_frame/output_lettuce1.jpg", image)
    cv2.imshow("Detection", image)     
    cv2.waitKey(0)

<img align="center" src="img/img71.png">

82 numaralı satırda kullanılan NMSBoxes methodu ile en yüksek güvenilirliğe sahip dikdörtgenlerin 
id’leri max_ids dizisi içerisine atanır.

84 numaralı satırda max_ids dizisi içerisindeki değerler döndürülür. 86 ve 92 numaralı satırlar 
arasında sınırlayıcı dikdörtgenin görüntü üzerindeki başlangıç, yükseklik ve genişlik değerleri 
start_x, start_y, box_width, box_height değişkenlerine atanır.

94, 95 ve 96 numaralı satırlar arasında tespit edilen nesnenin class ismi ve doğruluk oranı label 
ve confidence değişkenlerine atanır.

99 ve 100 numaralı satırlar arasında tespit edilen nesnenin sınırlayıcı dikdörtgeninin bitiş 
koordinatları bulunur.

102 ve 103 numaralı satırlar arasında tespit edilen nesneyi sınırlandıran dikdörtgenin rengi belirlenir.

<img align="center" src="img/img72.png">

NOT: Eğitmiş olduğumuz modeli bir video üzerinde test etmek istiyorsanız github hesabımdaki 
video_test_etme.py isimli python dosyasını indirebilirsiniz.
