import glob
import face_recognition


def face_compare_func(img1, img2):
    face = face_recognition.load_image_file(img1)
    face = face_recognition.face_encodings(face)[0]
    unknown_picture = face_recognition.load_image_file(img2)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    results = face_recognition.compare_faces([face], unknown_face_encoding)

    if results[0] == True:
        return img1
    else:
        return False


def open_files(img):
    for filename in glob.glob("registered_photo" + "*.jpg"):
        f = open(filename)
        print(face_compare_func(f, "photo/" + img))
