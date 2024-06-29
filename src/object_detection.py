import cv2
import numpy as np
from PIL import Image
import streamlit as st
import tempfile

MODEL = "model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "model/MobileNetSSD_deploy.prototxt.txt"


def process_image(image):
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections


def annotate_image(image, detections, confidence_threshold=0.5):
    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(image, (startX, startY), (endX, endY), 70, 2)
    return image


def main():
    st.title('👁️👁️Object Detection for Images and Videos')
    st.divider()

    option = st.selectbox("Choose an option", ("Image", "Video"))

    if option == "Image":
        file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
        if file is not None:
            st.image(file, caption="Uploaded Image")
            image = Image.open(file)
            image = np.array(image)
            detections = process_image(image)
            processed_image = annotate_image(image, detections)
            st.image(processed_image, caption="Processed Image")

    elif option == "Video":
        video_file = st.file_uploader(
            'Upload Video', type=['mp4', 'avi', 'mov'])
        if video_file is not None:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(video_file.read())
            cap = cv2.VideoCapture(tfile.name)

            stframe = st.empty()
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                detections = process_image(frame)
                processed_frame = annotate_image(frame, detections)
                stframe.image(processed_frame, channels="BGR")
            cap.release()


if __name__ == "__main__":
    main()
