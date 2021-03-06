import cv2
import numpy as np
import glob
import random
import os
import base64

print(base64.b64decode(b'Cl9fICAgICAgICBfX19fX18gICAgICBfX19fICAKXCBcICAgICAgLyAvIF9fX3xfXyBffCAgXyBcIAogXCBcIC9cIC8gLyB8ICAgLyBfYCB8IHxfKSB8CiAgXCBWICBWIC98IHxfX3wgKF98IHwgIF8gPCAKICAgXF8vXF8vICBcX19fX1xfXyxffF98IFxfXAo=').decode("UTF-8"))
print("\n\nGIVE ABSOLUTE PATH FOR THE FILES REQUIRED\nEXAMPLE OF WEIGHT FILE PATH : E:\\data\\yolov3_trained.weights\n\n")

# Paths
weight_path = str(input("\n\nEnter the absolute path of the Weight file : "))
config_path = str(input("Enter the absolute path of the Test Config file : "))
image_path = str(input("Enter the absolute path of the image(s) to test [*.jpg for all] : "))


# Load Yolo
net = cv2.dnn.readNet(weight_path, config_path)

# Name custom object
classes = ["Gun"]


# Images path
images_path = glob.glob(image_path)
#                       Path for the image to test                        


layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Insert here the path of your images
random.shuffle(images_path)
# loop through all the images
for img_path in images_path:
    # Loading image
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                # Object detected
                print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 2)


    cv2.imshow("Image", img)
    key = cv2.waitKey(0)

cv2.destroyAllWindows()
