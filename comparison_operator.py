class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, input):
        if isinstance(input, Vector):
            return Vector(self.x + input.x, self.y + input.y)

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'
    
    def __eq__(self, input: object) -> bool:
        if isinstance(input, Vector):
            return self.x == input.x and self.y == input.y
        return False
    
v1 = Vector(1, 1)
v2 = Vector(1, 1)
v3 = Vector(2, 3)

print(id(v1), id(v2), id(v3))
print(f'v1 == v2: {v1 == v2}')
print(f'v2 == v3: {v2 == v3}')