# nhandienkhuonmat
python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model 	--embedding-model openface_nn4.small2.v1.t7

python train_model.py --embeddings output/embeddings.pickle  --recognizer output/recognizer.pickle 	--le output/le.pickle


python recognize_video.py --detector face_detection_model \
	--embedding-model openface_nn4.small2.v1.t7 \
	--recognizer output/recognizer.pickle \
	--le output/le.pickle


Chạy theo thư tự các file 01_ ,, 02, 03, 04

01_face_detection_capture.py để lấy được khuôn mặt chính xác hơn


# hướng dẫn nhanh:

1. tạo thư mục tên mình (không dấu) trong file dataset ví dụ : huy , lan ... Copy hình khuôn mặt của mình vào ( lưu ý hình chỉ có 1 mặt mình) 
    , copy nhiều hình người lạ vào thư mục unknown
    
2. Chạy file 02_extract_embeddings.py 
3. Chạy file 03_train_model.py -> kết quả sẽ tạo được 3 file embeddings.pickle , recognizer.pickle , le.pickle trong thư mục output
4. chạy file 04_recognize_video.py ( lưu ý nhớ cài thự viện  imutils )
