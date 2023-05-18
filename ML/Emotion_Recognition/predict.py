from ML.Emotion_Recognition.load_model import model
from tensorflow.keras.preprocessing.image import img_to_array
from mtcnn import MTCNN
from PIL import Image
import numpy as np
import cv2


async def predict(img_path):
    detector = MTCNN()
    original_image = cv2.imread(img_path)
    image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    faces_detection = detector.detect_faces(image)

    async def getFaceEmo(x, y, w, h):
        img = np.copy(image[y : y + h, x : x + w])
        RGB_face = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        grey_face = RGB_face.convert("L")
        grey_face = grey_face.resize((48, 48))
        face_array = img_to_array(grey_face)
        face_array = face_array.reshape(1, 48, 48, 1)

        # predict with pretrained model
        expression_predict = model.predict(face_array)[0]

        # emotion in string
        mapper = {
            0: "happy",
            1: "sad",
            2: "neutral",
        }
        emotion = mapper[expression_predict.argmax()]
        return emotion

    if len(faces_detection) == 0:
        raise

    faces = []
    for face in faces_detection:
        bounding_box = face["box"]

        x, y, w, h = bounding_box
        emotion = await getFaceEmo(x, y, w, h)
        faces.append([[x, y, w, h], emotion])

    for [x, y, w, h], emotion in faces:
        cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(
            original_image,
            emotion,
            (x, y + h),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            3,
        )
    return original_image


async def emo_rec_pred(img_path):
    new_image = await predict(img_path)
    cv2.imwrite(img_path, new_image)
    return
