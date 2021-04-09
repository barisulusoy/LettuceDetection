# Gerekli kütüphanelerin eklenmesi:
import cv2
import numpy as np


# Test edilecek videonun tanımlanması:
frame_capture = cv2.VideoCapture("videos\lettuce_video.mp4")

# Test edilen videoyu kaydetmek için oluşturulan değişken:
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_register = cv2.VideoWriter('videos\lettuce_output.avi', fourcc, 20.0, (1080,610))

# Videolar arka arkaya sıralanmış görüntülerden oluştuğu için sonsuz döngü içerisinde 
# her bir görüntü (frame) okunur.
while True:
    
    # Framelerin okunması işlemi, frame başarılı bir şekilde okunmuş ise
    # ret değişkenine True, okunamamış ise False değişkenim atanır. 
    ret, frame = frame_capture.read()
    
    # Frame'in okunamadığının bilgisi kullanıcaya gösterilir:
    if not ret:
        print("Kamera okunamadı...")
        break
    
    # Frame boyutunun değiştirilmesi işlemi:
    frame = cv2.resize(frame,(1080,610))
    
    # Herbir frame'in genişlik ve yükseklik değerlerinin alınması işlemi:
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]
    
    # Frame'in blob formata dönüştürülmesi:
    frame_blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416), swapRB=True, crop=False)
    
    # Eğitilen modelde kullanılan sınıfların diziye atılması:
    labels =["Marul"]

    # Testpit edilen görüntüde farklı sınıflar bulunuyorsa; herbir farklı 
    # sınıfı farklı renkte sınırlayıcı dikdörtgen içerisine alma:
    colors = ["0,0,255","0,0,255","255,0,0","255,255,0","0,255,0"]
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
    model.setInput(frame_blob)
    
    # Çıktı katmanı içerisindeki değerlere erişilir:
    detection_layers = model.forward(output_layer)

    # NON-MAXIMUM SUPPRESSION (OPERATION-1):
    ids_list = []
    boxes_list = []
    confidences_list = []
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
                bounding_box = object_detection[0:4] * np.array([frame_width,frame_height,frame_width,frame_height])
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
         
        cv2.rectangle(frame, (start_x,start_y),(end_x,end_y),box_color,2)
        cv2.rectangle(frame, (start_x-1,start_y),(end_x+1,start_y-30),box_color,-1)
        cv2.putText(frame,label,(start_x,start_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    
    video_register.write(frame)
    cv2.imshow("Detector",frame)
    
    if cv2.waitKey(1) & ord("q") ==27:
        break

frame_capture.release()
video_register.release()
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    