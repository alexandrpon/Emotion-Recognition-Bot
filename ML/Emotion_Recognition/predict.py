from ML.Emotion_Recognition.load_model import model
from tensorflow.keras.preprocessing.image import img_to_array
from mtcnn import MTCNN
from PIL import Image
import cv2


async def predict(img_path):
    detector = MTCNN()
    src = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
    result = detector.detect_faces(src)

    bounding_box = result[0]["box"]
    x, y, w, h = bounding_box

    img = src[y : y + h, x : x + w]
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
    return grey_face, emotion


async def emo_rec_pred(img_path):
    image_rescale, out = await predict(img_path)
    image_rescale.save(img_path)
    return out
