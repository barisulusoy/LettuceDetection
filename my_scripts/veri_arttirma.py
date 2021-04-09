"""
    NOT: Bu kısım Google Colab dosyasını açamayanlar içindir. Buradaki kodları
    Google Colab'a kopyalayabilirsiniz.
"""

# Drive'a bağlanma:
from google.colab import drive
drive.mount('/content/drive')

# Gerekli paketlerin yüklenmesi:
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# Veri arttırma yönteminin ve hiperparametrelerin seçilmesi:
datagen = ImageDataGenerator(rotation_range=40,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             vertical_flip=True,
                             fill_mode='nearest')
                             
# Arttırma işlemi yapılacak olan görüntünün dosyadan okunması işlemi:
img = load_img('/content/drive/MyDrive/lettuce_images/lettuce (17).jpg')
x = img_to_array(img)
x = x.reshape((1,) + x.shape)

# Giriş görüntüsünden kaç tane üretilmesini istediğimizle ilgili oluşturduğumuz for döngüsü
# ve sonuçların ilgili formatla kaydedilip, dosyaya yazdırılması işlemleri:                      
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='/content/drive/MyDrive/arttirilmis_veri', 
                          save_format='jpg'):
    i += 1
    if i > 20:
        break