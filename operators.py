class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, input):
        if isinstance(input, Vector):
            return Vector(self.x + input.x, self.y + input.y)

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'

def print_vector(vector: Vector):
    print(vector)

vector_one = Vector(1, 1)
vector_two = Vector(2, 3)

# print(vector_one)
# print(vector_two)

print_vector(vector_two + vector_one)