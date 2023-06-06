import cv2
import numpy as np
import math

def calculate_vase_volume(image_path):
    # Görüntüyü yükle
    image = cv2.imread(image_path)

    # Görüntüyü ters çevir (beyaz üzerine siyah şekil)
    inverted_image = cv2.bitwise_not(image)

    # Kenarları tespit et
    edges = cv2.Canny(inverted_image, 50, 150)

    # Kenar noktalarını bul
    points = np.column_stack(np.where(edges > 0))

    # Çizilecek çizgi rengini belirle (mavi)
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (255, 0, 255), (255, 255, 0), (0, 255, 255)]

    # Yarıçap ve yükseklik değerlerini hesapla
    radii_squares = []  # Yarıçapların karelerini saklayacak bir liste
    height = 0

    for i in range(len(points)-1):
        point1 = points[i][::-1]
        point2 = points[i+1][::-1]
        distance = np.linalg.norm(point2 - point1) * 0.01  # İki nokta arası mesafe (cm)
        radius = distance / 2  # Yarıçap
        radius_square = radius**2  # Yarıçapın karesi
        radii_squares.append(radius_square)
        height += distance

        # İki nokta arasında çizgi çiz
        # Çizgi rengini belirle
        color = colors[i % len(colors)]

        # Çizgi çiz
        cv2.line(image, tuple(point1), tuple(point2), color, thickness=2)

    # Görüntüyü göster
    cv2.imshow("Çizgili Görüntü", image)
    cv2.imwrite("C:\\Users\\ASUS\\Desktop\\mat porje\\cizgi.png", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    volume = (sum(radii_squares) / len(radii_squares)) * height
    print("nokta 1: ", tuple(point1))
    print("nokta 2: ", tuple(point2))
    print("h: ", height)
    print("len: ", len(radii_squares))
    volumse = sum(radii_squares) / len(radii_squares)

    print("ort yaruçap değeri: ", volumse)

    return volume

# Örnek görüntüyü kullanarak hesaplama yapma
image_path = "denememe.png"  # Görüntü dosyasının yolunu belirtin
vase_volume = calculate_vase_volume(image_path)
print("Vazonun Hacmi: ", vase_volume, " pi birimi")
