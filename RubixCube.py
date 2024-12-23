from enum import Enum


def default_data():
    # Cube layout
    #   W     |   4
    # O G R B | 0 1 2 3
    #   Y     |   5

    return [
        [
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ],
        [
            ['G', 'G', 'G'],
            ['G', 'G', 'G'],
            ['G', 'G', 'G']
        ],
        [
            ['R', 'R', 'R'],
            ['R', 'R', 'R'],
            ['R', 'R', 'R']
        ],
        [
            ['B', 'B', 'B'],
            ['B', 'B', 'B'],
            ['B', 'B', 'B']
        ],
        [
            ['W', 'W', 'W'],
            ['W', 'W', 'W'],
            ['W', 'W', 'W']
        ],
        [
            ['Y', 'Y', 'Y'],
            ['Y', 'Y', 'Y'],
            ['Y', 'Y', 'Y']
        ]
    ]


def print_2d_array(array):
    print('printing array')
    for row in array:
        print(row)


class RubixCube:
    class Face(Enum):
        # Cube layout
        #   W     |   4
        # O G R B | 0 1 2 3
        #   Y     |   5
        # Blue orientations assume horizontal rotations to reach face

        ORANGE = 0  # Left
        GREEN = 1   # Front
        RED = 2     # Right
        BLUE = 3    # Back
        WHITE = 4   # Up
        YELLOW = 5  # Down

        def to_char(self):
            return self.name[0]

        def up(self):
            if self == RubixCube.Face.ORANGE:
                return RubixCube.Face.WHITE
            elif self == RubixCube.Face.GREEN:
                return RubixCube.Face.WHITE
            elif self == RubixCube.Face.RED:
                return RubixCube.Face.WHITE
            elif self == RubixCube.Face.BLUE:
                return RubixCube.Face.WHITE
            elif self == RubixCube.Face.WHITE:
                return RubixCube.Face.BLUE
            elif self == RubixCube.Face.YELLOW:
                return RubixCube.Face.GREEN

        def down(self):
            if self == RubixCube.Face.ORANGE:
                return RubixCube.Face.YELLOW
            elif self == RubixCube.Face.GREEN:
                return RubixCube.Face.YELLOW
            elif self == RubixCube.Face.RED:
                return RubixCube.Face.YELLOW
            elif self == RubixCube.Face.BLUE:
                return RubixCube.Face.YELLOW
            elif self == RubixCube.Face.WHITE:
                return RubixCube.Face.GREEN
            elif self == RubixCube.Face.YELLOW:
                return RubixCube.Face.BLUE

        def right(self):
            if self == RubixCube.Face.ORANGE:
                return RubixCube.Face.GREEN
            elif self == RubixCube.Face.GREEN:
                return RubixCube.Face.RED
            elif self == RubixCube.Face.RED:
                return RubixCube.Face.BLUE
            elif self == RubixCube.Face.BLUE:
                return RubixCube.Face.ORANGE
            elif self == RubixCube.Face.WHITE:
                return RubixCube.Face.RED
            elif self == RubixCube.Face.YELLOW:
                return RubixCube.Face.RED

        def left(self):
            if self == RubixCube.Face.ORANGE:
                return RubixCube.Face.BLUE
            elif self == RubixCube.Face.GREEN:
                return RubixCube.Face.ORANGE
            elif self == RubixCube.Face.RED:
                return RubixCube.Face.GREEN
            elif self == RubixCube.Face.BLUE:
                return RubixCube.Face.RED
            elif self == RubixCube.Face.WHITE:
                return RubixCube.Face.ORANGE
            elif self == RubixCube.Face.YELLOW:
                return RubixCube.Face.ORANGE

        def back(self):
            if self == RubixCube.Face.ORANGE:
                return RubixCube.Face.RED
            elif self == RubixCube.Face.GREEN:
                return RubixCube.Face.BLUE
            elif self == RubixCube.Face.RED:
                return RubixCube.Face.ORANGE
            elif self == RubixCube.Face.BLUE:
                return RubixCube.Face.GREEN
            elif self == RubixCube.Face.WHITE:
                return RubixCube.Face.YELLOW
            elif self == RubixCube.Face.YELLOW:
                return RubixCube.Face.WHITE

        def front(self):
            # Adding method for clarity
            return self

        def orientation(self):
            return (f'Front: {self.front().name}\n'
                    f'Back: {self.back().name}\n'
                    f'Left: {self.left().name}\n'
                    f'Right: {self.right().name}\n'
                    f'Up: {self.up().name}\n'
                    f'Down: {self.down().name}')

    def __init__(self):
        self.data = default_data()

    def to_string(self):
        # Cube layout
        #   W     |   4
        # O G R B | 0 1 2 3
        #   Y     |   5

        output_str = ''
        for row in range(3):
            output_str += f'    {"".join(map(str, self.data[RubixCube.Face.WHITE.value][row]))}\n'

        for row in range(3):
            output_str += (f'{"".join(map(str, self.data[RubixCube.Face.ORANGE.value][row]))} '
                           f'{"".join(map(str, self.data[RubixCube.Face.GREEN.value][row]))} '
                           f'{"".join(map(str, self.data[RubixCube.Face.RED.value][row]))} '
                           f'{"".join(map(str, self.data[RubixCube.Face.BLUE.value][row]))}\n')

        for row in range(3):
            output_str += f'    {"".join(map(str, self.data[RubixCube.Face.YELLOW.value][row]))}\n'

        return output_str

    def get_edges(self, face):

        top = None
        right = None
        bottom = None
        left = None

        if face == RubixCube.Face.ORANGE:
            top = [row[0] for row in self.data[RubixCube.Face.WHITE.value]]
            bottom = [row[0] for row in self.data[RubixCube.Face.YELLOW.value]]
            left = [row[2] for row in self.data[RubixCube.Face.BLUE.value]]
            right = [row[0] for row in self.data[RubixCube.Face.GREEN.value]]
        elif face == RubixCube.Face.GREEN:
            top = self.data[RubixCube.Face.WHITE.value][2]
            bottom = self.data[RubixCube.Face.YELLOW.value][0]
            left = [row[2] for row in self.data[RubixCube.Face.ORANGE.value]]
            right = [row[0] for row in self.data[RubixCube.Face.RED.value]]
        elif face == RubixCube.Face.RED:
            top = [row[2] for row in self.data[RubixCube.Face.WHITE.value]]
            bottom = [row[2] for row in self.data[RubixCube.Face.YELLOW.value]]
            left = [row[0] for row in self.data[RubixCube.Face.GREEN.value]]
            right = [row[2] for row in self.data[RubixCube.Face.BLUE.value]]
        elif face == RubixCube.Face.BLUE:
            top = self.data[RubixCube.Face.WHITE.value][0]
            bottom = self.data[RubixCube.Face.YELLOW.value][2]
            left = [row[2] for row in self.data[RubixCube.Face.RED.value]]
            right = [row[0] for row in self.data[RubixCube.Face.ORANGE.value]]
        elif face == RubixCube.Face.WHITE:
            top = self.data[RubixCube.Face.BLUE.value][0]
            bottom = self.data[RubixCube.Face.GREEN.value][0]
            left = self.data[RubixCube.Face.ORANGE.value][0]
            right = self.data[RubixCube.Face.RED.value][0]
        elif face == RubixCube.Face.YELLOW:
            top = self.data[RubixCube.Face.GREEN.value][2]
            bottom = self.data[RubixCube.Face.BLUE.value][2]
            left = self.data[RubixCube.Face.ORANGE.value][2]
            right = self.data[RubixCube.Face.RED.value][2]

        return top, bottom, left, right
    
    def set_edges(self, face, top, bottom, left, right):
        # TODO implement
        return None

    def rotate(self, face, clockwise):
        if not isinstance(face, RubixCube.Face):
            raise ValueError(f"Expected a Face enum, but got {type(face).__name__}")

        # Rotate Face #
        # Dummy starting array. outer ring is for the edges. Corners will remain X
        temp_face = [['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X']]
        # Set center
        for row in range(3):
            for col in range(3):
                temp_face[row + 1][col + 1] = self.data[face.value][row][col]

        # Set edges
        # TODO: use get_edges
        for val in range(3):
            temp_face[0][val + 1] = self.data[face.up().value][2][val]
            temp_face[4][val + 1] = self.data[face.down().value][0][val]
            temp_face[val + 1][0] = self.data[face.left().value][val][2]
            temp_face[val + 1][4] = self.data[face.right().value][val][0]

        print_2d_array(temp_face)

        n = len(temp_face)
        # Transpose array
        for row in range(n):
            for col in range(row + 1, n):
                # Transpose by flipping along diagonal
                temp_face[row][col], temp_face[col][row] = temp_face[col][row], temp_face[row][col]

        # reverse row/col depending on clockwise or counterclockwise
        if clockwise:
            for row in range(n):
                for col in range(n // 2):
                    temp = temp_face[row][col]
                    temp_face[row][col] = temp_face[row][n - col - 1]
                    temp_face[row][n - col - 1] = temp
        else:
            for col in range(n):
                for row in range(n // 2):
                    temp = temp_face[row][col]
                    temp_face[row][col] = temp_face[n - row - 1][col]
                    temp_face[n - row - 1][col] = temp

        print_2d_array(temp_face)

        # Write new data to cube
        # Set center
        for row in range(3):
            for col in range(3):
                self.data[face.value][row][col] = temp_face[row + 1][col + 1]

        # Set edges
        # TODO: use set_edges
        for val in range(3):
            self.data[face.up().value][2][val] = temp_face[0][val + 1]
            self.data[face.down().value][0][val] = temp_face[4][val + 1]
            self.data[face.left().value][val][2] = temp_face[val + 1][0]
            self.data[face.right().value][val][0] = temp_face[val + 1][4]


cube = RubixCube()
print(RubixCube.Face.GREEN.orientation())
# print(RubixCube.Face.BLUE.to_char())
print(cube.to_string())
cube.rotate(RubixCube.Face.GREEN, True)
print(cube.to_string())
cube.rotate(RubixCube.Face.RED, True)
print(cube.to_string())
