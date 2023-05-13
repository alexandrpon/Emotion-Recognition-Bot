from ML.Emotion_Recognition.load_model import model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import cv2


async def predict(src):
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    #  improves the contrast of the image
    dst = cv2.equalizeHist(src)

    # -- Detect faces
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_alt.xml"
    )
    faces = face_cascade.detectMultiScale(dst, minSize=(80, 80))

    if list(faces):
        x, y, w, h = faces[0]
    else:
        x, y, w, h = (0, 0, 80, 80)

    img = dst[y : y + h, x : x + w]
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
    image = cv2.imread(img_path)
    image_rescale, out = await predict(image)
    image_rescale.save(img_path)
    return out
