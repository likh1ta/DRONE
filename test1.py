
import cv2

from ultralytics import YOLO







MODEL_WEIGHTS_PATH = 'C:/Users/Likhita/Downloads/best.pt' 





WEBCAM_SOURCE = 0 

CONFIDENCE_THRESHOLD = 0.25









try:

    model = YOLO(MODEL_WEIGHTS_PATH)

except Exception as e:

    print(f"Error loading model: {e}")

    exit()





cap = cv2.VideoCapture(WEBCAM_SOURCE)



if not cap.isOpened():

    print("Error: Could not open webcam. Check drivers or try a different source index (1, 2, etc.)")

    exit()



print("Starting YOLOv8 Live Detection (Press 'q' to quit)...")



while True:

    ret, frame = cap.read()

    if not ret:

        print("Failed to grab frame.")

        break



    

    results = model.predict(

        source=frame, 

        conf=CONFIDENCE_THRESHOLD, 

        verbose=False 

    )



    

    annotated_frame = results[0].plot()

    

    

    cv2.imshow("Live Thermal Detection (Model Test)", annotated_frame)

    

    

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break





cap.release()

cv2.destroyAllWindows()
