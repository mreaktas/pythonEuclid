import math  

# 2 boyutlu uzaydaki noktaları temsil eden liste  
points = [(1, 2), (4, 6), (7, 1), (2, 3), (5, 5)]  

# Öklid Mesafesi için fonksiyon  
def euclideanDistance(point1, point2):  
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)  

# Mesafelerin saklanacağı liste  
distances = []  

# Her nokta çifti arasındaki mesafeyi hesaplama  
for i in range(len(points)):  
    for j in range(i + 1, len(points)):  
        distance = euclideanDistance(points[i], points[j])  
        distances.append(distance)  

# Minimum mesafeyi bulma  
min_distance = min(distances)  

# Sonuçları yazdırma  
print("Mesafeler:", distances)  
print("Minimum mesafe:", min_distance)