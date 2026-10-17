points = [
    (2, 3),
    (-1, 4),
    (5, -6),
    (0, 7),
    (-3, -2)
]

def both_positive(point):
    a, b = point

    return a > 0 and b > 0

positive_points = list(filter(both_positive, points))

print("Points where both values are positive:")
print(positive_points)
