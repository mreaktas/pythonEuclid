import math

# 2 boyutlu uzaydaki noktaları temsil eden liste
points = [(1, 2), (4, 6), (7, 8), (2, 1), (8, 3)]

# Öklid Mesafesi için fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Her nokta çifti arasındaki mesafelerin hesaplanıp saklanacağı liste 
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma ve sonucu yazdırma
min_distance = min(distances)
print("Minimum mesafe:", min_distance)