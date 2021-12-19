class Point:
    """Three-dimensional point."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        """Return dev-readable representation of Point."""
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other) -> bool:
        """Return True if our point is equal to other point"""
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, point) -> "Point":
        """Return a new point with coordinates from our and point added"""
        x1, y1, z1 = self.x, self.y, self.z
        x2, y2, z2 = point.x, point.y, point.z
        return Point(x1+x2, y1+y2, z1+z2)
    
    def __sub__(self, point) -> "Point":
        """Return a new point with coordinates from our and point subtracted"""
        x1, y1, z1 = self.x, self.y, self.z
        x2, y2, z2 = point.x, point.y, point.z
        return Point(x1-x2, y1-y2, z1-z2)

    def __mul__(self, scalar) -> "Point":
        """Return copy of our point, scaled by given scalar value."""
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        return Point(x, y, z)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

## Tests

# p1 = Point(x=1, y=2, z=3)
# p2 = Point(x=1, y=2, z=3)
# p3 = Point(x=2, y=3, z=4)

# print(p1)       # (1, 2, 3)
# print(p1 == p2) # True 
# print(p1 == p3) # False
# print(p1 + p2)  # (2, 4, 6)

# p2 = p1 * 10
# print(p1)
# print(p2)

# x, y, z = p1
# print(x, y, z)
# for coord in p1:
#     print(coord)