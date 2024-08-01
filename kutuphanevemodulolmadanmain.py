# 2D uzaydaki noktaları temsil eden liste  
points = [(1, 2), (4, 6), (7, 1), (2, 3), (5, 5)]  

# Öklid mesafesi için fonksiyon  
def euclideanDistance(point1, point2):  
    # Noktaların x ve y koordinatlarını ayırma  
    x1, y1 = point1  
    x2, y2 = point2  
    # Öklid mesafe formülünü kullanarak mesafeyi hesaplama  
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  
    return distance  

# Mesafelerin saklanacağı liste  
distances = []  

# Her nokta çifti arasındaki mesafeyi hesaplama  
for i in range(len(points)):  
    for j in range(i + 1, len(points)):  
        distance = euclideanDistance(points[i], points[j])  
        distances.append(distance)  

# Minimum mesafeyi bulma  
min_distance = distances[0] if distances else None  
for distance in distances:  
    if distance < min_distance:  
        min_distance = distance  

# Sonuçları yazdırma  
print("Hesaplanan mesafeler:", distances)  
print("Minimum mesafe:", min_distance)