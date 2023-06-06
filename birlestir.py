import cv2

def merge_images(background_path, overlay_path, output_path):
    # Arka plan görüntüsünü yükle
    background = cv2.imread(background_path)

    # Üzerine yapıştırılacak görüntüyü yükle
    overlay = cv2.imread(overlay_path)

    # Görüntüleri birleştir
    merged = cv2.addWeighted(background, 1.0, overlay, 1.0, 0)

    # Birleştirilmiş görüntüyü kaydet
    cv2.imwrite(output_path, merged)

# Çizgili görüntü ile deneme görüntüsünü birleştir
background_path = "cizgi.png"
overlay_path = "deneme.png"
output_path = "birlestirilmis.png"

merge_images(background_path, overlay_path, output_path)
