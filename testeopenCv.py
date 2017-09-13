# Joao Henrique DSS

import cv2

classificador = cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml')

imagem = cv2.imread("pessoas\pessoas\\pessoas1.jpg")
imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

faceDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor = 1.1 , minNeighbors = 9, minSize=(30,30))

print(len(faceDetectadas))

for (x, y , l, a) in faceDetectadas :

    cv2.rectangle(imagem, (x , y), (x + l, y + a), (1, 1, 255), 2)

cv2.imshow("faces encontradas" , imagem)
cv2.waitKey()
if( len(faceDetectadas) > 0):
    print ("Tem %i pessoas nesse local" %len(faceDetectadas))