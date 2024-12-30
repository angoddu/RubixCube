from enum import Enum
import random
import tkinter as tk


def default_data(debug):
    # Cube layout
    #   W     |   4
    # O G R B | 0 1 2 3
    #   Y     |   5

    return [make_dummy_array(3, RubixCube.Face.ORANGE.to_char(), debug),
            make_dummy_array(3, RubixCube.Face.GREEN.to_char(), debug),
            make_dummy_array(3, RubixCube.Face.RED.to_char(), debug),
            make_dummy_array(3, RubixCube.Face.BLUE.to_char(), debug),
            make_dummy_array(3, RubixCube.Face.WHITE.to_char(), debug),
            make_dummy_array(3, RubixCube.Face.YELLOW.to_char(), debug)]


def make_dummy_array(size, val, debug=False):
    if debug:
        return [[f'{val}{r * size + c + 1}' for c in range(size)] for r in range(size)]
    else:
        return [[val for _ in range(size)] for _ in range(size)]


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

        @staticmethod
        def from_char(char_val):
            char_val = char_val.upper()
            for face in RubixCube.Face:
                if char_val == face.to_char():
                    return face
            return None

        def get_position(self):
            positions_map = {
                "white": (0, 1), "green": (1, 1), "yellow": (2, 1),
                "orange": (1, 0), "red": (1, 2), "blue": (1, 3)
            }
            return positions_map.get(self.name.lower())

        # def up(self):
        #     if self == RubixCube.Face.ORANGE:
        #         return RubixCube.Face.WHITE
        #     elif self == RubixCube.Face.GREEN:
        #         return RubixCube.Face.WHITE
        #     elif self == RubixCube.Face.RED:
        #         return RubixCube.Face.WHITE
        #     elif self == RubixCube.Face.BLUE:
        #         return RubixCube.Face.WHITE
        #     elif self == RubixCube.Face.WHITE:
        #         return RubixCube.Face.BLUE
        #     elif self == RubixCube.Face.YELLOW:
        #         return RubixCube.Face.GREEN
        #
        # def down(self):
        #     if self == RubixCube.Face.ORANGE:
        #         return RubixCube.Face.YELLOW
        #     elif self == RubixCube.Face.GREEN:
        #         return RubixCube.Face.YELLOW
        #     elif self == RubixCube.Face.RED:
        #         return RubixCube.Face.YELLOW
        #     elif self == RubixCube.Face.BLUE:
        #         return RubixCube.Face.YELLOW
        #     elif self == RubixCube.Face.WHITE:
        #         return RubixCube.Face.GREEN
        #     elif self == RubixCube.Face.YELLOW:
        #         return RubixCube.Face.BLUE
        #
        # def right(self):
        #     if self == RubixCube.Face.ORANGE:
        #         return RubixCube.Face.GREEN
        #     elif self == RubixCube.Face.GREEN:
        #         return RubixCube.Face.RED
        #     elif self == RubixCube.Face.RED:
        #         return RubixCube.Face.BLUE
        #     elif self == RubixCube.Face.BLUE:
        #         return RubixCube.Face.ORANGE
        #     elif self == RubixCube.Face.WHITE:
        #         return RubixCube.Face.RED
        #     elif self == RubixCube.Face.YELLOW:
        #         return RubixCube.Face.RED
        #
        # def left(self):
        #     if self == RubixCube.Face.ORANGE:
        #         return RubixCube.Face.BLUE
        #     elif self == RubixCube.Face.GREEN:
        #         return RubixCube.Face.ORANGE
        #     elif self == RubixCube.Face.RED:
        #         return RubixCube.Face.GREEN
        #     elif self == RubixCube.Face.BLUE:
        #         return RubixCube.Face.RED
        #     elif self == RubixCube.Face.WHITE:
        #         return RubixCube.Face.ORANGE
        #     elif self == RubixCube.Face.YELLOW:
        #         return RubixCube.Face.ORANGE
        #
        # def back(self):
        #     if self == RubixCube.Face.ORANGE:
        #         return RubixCube.Face.RED
        #     elif self == RubixCube.Face.GREEN:
        #         return RubixCube.Face.BLUE
        #     elif self == RubixCube.Face.RED:
        #         return RubixCube.Face.ORANGE
        #     elif self == RubixCube.Face.BLUE:
        #         return RubixCube.Face.GREEN
        #     elif self == RubixCube.Face.WHITE:
        #         return RubixCube.Face.YELLOW
        #     elif self == RubixCube.Face.YELLOW:
        #         return RubixCube.Face.WHITE
        #
        # def front(self):
        #     # Adding method for clarity
        #     return self
        #
        # def orientation(self):
        #     return (f'Front: {self.front().name}\n'
        #             f'Back: {self.back().name}\n'
        #             f'Left: {self.left().name}\n'
        #             f'Right: {self.right().name}\n'
        #             f'Up: {self.up().name}\n'
        #             f'Down: {self.down().name}')

    def __init__(self, root, data, debug=False):
        self.root = root
        self.root.title("Rubix Cube")

        self.debug = debug
        self.grid_frames = {}  # Store the grid frames for easier access later
        self.data = data  # Store the cube data (3D array)
        self.create_cube_layout()
        self.create_buttons()

    def create_cube_layout(self):
        for face in RubixCube.Face:
            position = face.get_position()
            frame = tk.Frame(self.root, bg="black", padx=2, pady=2)
            frame.grid(row=position[0], column=position[1])
            self.grid_frames[face.name] = frame
            self.create_face_grid(frame, face)

    def create_face_grid(self, parent, face):
        canvas = tk.Canvas(parent, width=150, height=150, bg="black")
        canvas.pack()

        cell_size = 50
        for row in range(len(self.data[face.value])):
            for col in range(len(self.data[face.value][row])):
                # Extract color and display from cell
                cell_data = self.data[face.value][row][col]
                cell_color = RubixCube.Face.from_char(cell_data[0]).name.lower()
                if self.debug:
                    cell_number = cell_data[1]
                else:
                    cell_number = None

                # Draw a rectangle for the cell
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                canvas.create_rectangle(x1, y1, x2, y2, fill=cell_color, outline="black")
                # Add text to the center of the cell
                canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=cell_number, fill="black")

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=4, column=0, columnspan=4)

        # Create rotation buttons
        for face in RubixCube.Face:
            # Make buttons
            clockwise = tk.Button(
                button_frame,
                text=face.to_char(),
                command=lambda arg_face=face: (self.rotate(arg_face, True), self.update_display())
            )
            counterclockwise = tk.Button(
                button_frame,
                text=face.to_char() + '\'',
                command=lambda arg_face=face: (self.rotate(arg_face, False), self.update_display())
            )

            # Set position
            clockwise.grid(row=0, column=face.value, padx=2, pady=2)
            counterclockwise.grid(row=1, column=face.value, padx=2, pady=2)

            # Add tooltips
            # self.add_tooltip(clockwise, f"{face.name.capitalize()} clockwise")
            # self.add_tooltip(counterclockwise, f"{face.name.capitalize()} counterclockwise")

        # Create reset button
        reset = tk.Button(
            button_frame,
            text="Reset",
            command=lambda: (self.reset(), self.update_display())
        )
        reset.grid(row=0, column=6, rowspan=2, padx=2, pady=2)
        # self.add_tooltip(reset_button, "Reset cube data")

        shuffle = tk.Button(
            button_frame,
            text="Shuffle",
            command=lambda moves=100: (self.shuffle(moves), self.update_display())
        )
        shuffle.grid(row=0, column=7, rowspan=2, padx=2, pady=2)

    # Tooltips not displaying correctly. Shelving for now
    # def add_tooltip(self, widget, tooltip_text):
    #     # Create a label for the tooltip, initially hidden
    #     tooltip = tk.Label(self.root, text=tooltip_text, background="yellow", relief="solid", padx=5, pady=2, bd=1)
    #     tooltip.place_forget()  # Make sure it is not displayed initially
    #
    #     def show_tooltip(event):
    #         # Calculate position of the button relative to the root window
    #         x = event.x_root + 10
    #         y = event.y_root + 10
    #         print(f"Showing tooltip at ({x}, {y})")  # Debugging message for tooltip position
    #         tooltip.place(x=x, y=y)
    #
    #     def hide_tooltip(event):
    #         print("Hiding tooltip")
    #         tooltip.place_forget()  # Hide the tooltip when mouse leaves the button
    #
    #     # Bind the events to the widget
    #     widget.bind("<Enter>", show_tooltip)
    #     widget.bind("<Leave>", hide_tooltip)

    def update_display(self):
        for face_name, frame in self.grid_frames.items():
            # Clear the existing widgets in the frame
            for widget in frame.winfo_children():
                widget.destroy()

            # Redraw the cube layout with the updated data
            self.create_face_grid(frame, RubixCube.Face[face_name])

    def to_string(self):
        # Cube layout
        #   W     |   4
        # O G R B | 0 1 2 3
        #   Y     |   5

        output_str = ''
        elem_len = len(self.data[0][0][0])
        for row in range(3):
            output_str += f'{" " * ((elem_len + 1) * 3)}  {" ".join(map(str, self.data[RubixCube.Face.WHITE.value][row]))}\n'

        for row in range(3):
            output_str += (f'{" ".join(map(str, self.data[RubixCube.Face.ORANGE.value][row]))}   '
                           f'{" ".join(map(str, self.data[RubixCube.Face.GREEN.value][row]))}   '
                           f'{" ".join(map(str, self.data[RubixCube.Face.RED.value][row]))}   '
                           f'{" ".join(map(str, self.data[RubixCube.Face.BLUE.value][row]))}\n')

        for row in range(3):
            output_str += f'{" " * ((elem_len + 1) * 3)}  {" ".join(map(str, self.data[RubixCube.Face.YELLOW.value][row]))}\n'

        return output_str

    def get_edges(self, face):

        top = None
        right = None
        bottom = None
        left = None

        if face == RubixCube.Face.ORANGE:
            top = [row[0] for row in self.data[RubixCube.Face.WHITE.value]]
            bottom = [row[0] for row in self.data[RubixCube.Face.YELLOW.value]][::-1]
            left = [row[2] for row in self.data[RubixCube.Face.BLUE.value]]
            right = [row[0] for row in self.data[RubixCube.Face.GREEN.value]]
        elif face == RubixCube.Face.GREEN:
            top = self.data[RubixCube.Face.WHITE.value][2]
            bottom = self.data[RubixCube.Face.YELLOW.value][0]
            left = [row[2] for row in self.data[RubixCube.Face.ORANGE.value]]
            right = [row[0] for row in self.data[RubixCube.Face.RED.value]]
        elif face == RubixCube.Face.RED:
            top = [row[2] for row in self.data[RubixCube.Face.WHITE.value]][::-1]
            bottom = [row[2] for row in self.data[RubixCube.Face.YELLOW.value]]
            left = [row[2] for row in self.data[RubixCube.Face.GREEN.value]]
            right = [row[0] for row in self.data[RubixCube.Face.BLUE.value]]
        elif face == RubixCube.Face.BLUE:
            top = self.data[RubixCube.Face.WHITE.value][0][::-1]
            bottom = self.data[RubixCube.Face.YELLOW.value][2][::-1]
            left = [row[2] for row in self.data[RubixCube.Face.RED.value]]
            right = [row[0] for row in self.data[RubixCube.Face.ORANGE.value]]
        elif face == RubixCube.Face.WHITE:
            top = self.data[RubixCube.Face.BLUE.value][0][::-1]
            bottom = self.data[RubixCube.Face.GREEN.value][0]
            left = self.data[RubixCube.Face.ORANGE.value][0]
            right = self.data[RubixCube.Face.RED.value][0][::-1]
        elif face == RubixCube.Face.YELLOW:
            top = self.data[RubixCube.Face.GREEN.value][2]
            bottom = self.data[RubixCube.Face.BLUE.value][2][::-1]
            left = self.data[RubixCube.Face.ORANGE.value][2][::-1]
            right = self.data[RubixCube.Face.RED.value][2]

        return top, bottom, left, right

    def print_edges(self):
        old_data = self.data
        self.data = default_data(True)
        temp_face = make_dummy_array(5, 'X')
        # Set center
        for face in RubixCube.Face:
            for row in range(3):
                for col in range(3):
                    temp_face[row + 1][col + 1] = self.data[face.value][row][col]

            # Set edges
            top, bottom, left, right = self.get_edges(face)
            for i in range(3):
                temp_face[0][i + 1] = top[i]
                temp_face[4][i + 1] = bottom[i]
                temp_face[i + 1][0] = left[i]
                temp_face[i + 1][4] = right[i]

            print_2d_array(temp_face)

        self.data = old_data

    def set_edges(self, face, top, bottom, left, right):
        print(f"Setting edges: {face.name}")
        print(f"Top: {top}")
        print(f"Bottom: {bottom}")
        print(f"Left: {left}")
        print(f"Right: {right}")
        if face == RubixCube.Face.ORANGE:
            for i in range(3):
                self.data[RubixCube.Face.WHITE.value][i][0] = top[i]
                self.data[RubixCube.Face.YELLOW.value][i][0] = bottom[2 - i]
                self.data[RubixCube.Face.BLUE.value][i][2] = left[i]
                self.data[RubixCube.Face.GREEN.value][i][0] = right[i]
        elif face == RubixCube.Face.GREEN:
            self.data[RubixCube.Face.WHITE.value][2] = top
            self.data[RubixCube.Face.YELLOW.value][0] = bottom
            for i in range(3):
                self.data[RubixCube.Face.ORANGE.value][i][2] = left[i]
                self.data[RubixCube.Face.RED.value][i][0] = right[i]
        elif face == RubixCube.Face.RED:
            for i in range(3):
                self.data[RubixCube.Face.WHITE.value][i][2] = top[2 - i]
                self.data[RubixCube.Face.YELLOW.value][i][2] = bottom[i]
                self.data[RubixCube.Face.GREEN.value][i][2] = left[i]
                self.data[RubixCube.Face.BLUE.value][i][0] = right[i]
        elif face == RubixCube.Face.BLUE:
            self.data[RubixCube.Face.WHITE.value][0] = top[::-1]
            self.data[RubixCube.Face.YELLOW.value][2] = bottom[::-1]
            for i in range(3):
                self.data[RubixCube.Face.RED.value][i][2] = left[i]
                self.data[RubixCube.Face.ORANGE.value][i][0] = right[i]
        elif face == RubixCube.Face.WHITE:
            self.data[RubixCube.Face.BLUE.value][0] = top[::-1]
            self.data[RubixCube.Face.GREEN.value][0] = bottom
            self.data[RubixCube.Face.ORANGE.value][0] = left
            self.data[RubixCube.Face.RED.value][0] = right[::-1]
        elif face == RubixCube.Face.YELLOW:
            self.data[RubixCube.Face.GREEN.value][2] = top
            self.data[RubixCube.Face.BLUE.value][2] = bottom[::-1]
            self.data[RubixCube.Face.ORANGE.value][2] = left[::-1]
            self.data[RubixCube.Face.RED.value][2] = right

    def rotate(self, face, clockwise):
        if not isinstance(face, RubixCube.Face):
            raise ValueError(f"Expected a Face enum, but got {type(face).__name__}")

        # Rotate Face #
        # Dummy starting array. outer ring is for the edges. Corners will remain X
        temp_face = make_dummy_array(5, 'X')
        # Set center
        for row in range(3):
            for col in range(3):
                temp_face[row + 1][col + 1] = self.data[face.value][row][col]

        # Set edges
        top, bottom, left, right = self.get_edges(face)
        for i in range(3):
            temp_face[0][i + 1] = top[i]
            temp_face[4][i + 1] = bottom[i]
            temp_face[i + 1][0] = left[i]
            temp_face[i + 1][4] = right[i]

        if self.debug:
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

        if self.debug:
            print_2d_array(temp_face)

        # Write new data to cube
        # Set center
        for row in range(3):
            for col in range(3):
                self.data[face.value][row][col] = temp_face[row + 1][col + 1]

        # Set edges
        for i in range(3):
            top[i] = temp_face[0][i + 1]
            bottom[i] = temp_face[4][i + 1]
            left[i] = temp_face[i + 1][0]
            right[i] = temp_face[i + 1][4]

        self.set_edges(face, top, bottom, left, right)

    def reset(self):
        self.data = default_data(self.debug)

    def shuffle(self, moves):
        last_move = None
        for i in range(moves):
            while True:
                face = RubixCube.Face(random.randint(0, 5))
                direction = random.choice([True, False])

                if last_move != (face, direction):
                    self.rotate(face, direction)
                    last_move = (face, direction)
                    break


if __name__ == "__main__":
    root = tk.Tk()

    debug = True
    cube_data = default_data(debug)
    cube = RubixCube(root, cube_data, debug)
    root.mainloop()

    # cube.print_edges()

    # print(RubixCube.Face.GREEN.orientation())
    # print(RubixCube.Face.BLUE.to_char())
    # print(cube.to_string())
    # cube.rotate(RubixCube.Face.GREEN, True)
    # print(cube.to_string())
    # cube.rotate(RubixCube.Face.WHITE, True)
    # print(cube.to_string())
