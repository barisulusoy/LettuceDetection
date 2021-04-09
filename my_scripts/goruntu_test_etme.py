# Gerekli kütüphanelerin eklenmesi:
import cv2
import numpy as np

# Test edilecek görüntünün okunması:
image = cv2.imread("D:/DeepLearningProjects/LettuceDetection/input_frame/input_lettuce1.jpg")

# Test edilecek görüntünün yüksekliğinin ve genişliğinin bulunması:
img_width = image.shape[1]
img_height = image.shape[0]
                                          
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

