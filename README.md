# RubixCube
Rubix cube simulator

# Development Plan
## Cube class

- `data`
  - 3D array of chars 3x3x3
  - `data[face][row][col]`
- `rotate(face, clockwise)`
  - `face`: the below face enum to identify the face
  - `clockwise`: a boolean saying if we are rotating clockwise (true) or counter clockwise (false)
  - Rotates the corresponding face the correct way
- `get_edges(face)` return tuple(top, bottom, left, right)
  - tuple return is 4 arrays of the edge data
  - Mapping:

| Face          | Top Edge        | Bottom Edge     | Left Edge       | Right Edge        |
|---------------|-----------------|-----------------|-----------------| ----------------- |
| Front (Green) | Up (W) bottom   | Down (Y) top    | Left (O) right  | Right (R) left    |
| Back (Blue)   | Up (W) top      | Down (Y) bottom | Right (R) right | Left (O) left     |
| Left (Orange) | Up (W) left     | Down (Y) left   | Back (B) right  | Front (G) left    |
| Right (Red)   | Up (W) right    | Down (Y) right  | Front (G) right | Back (B) left     |
| Up (White)    | Back (B) top    | Front (G) top   | Left (O) top    | Right (R) top     |
| Down (Yellow) | Front (G) bottom| Back (B) bottom | Left (O) bottom | Right (R) bottom  |

- `shuffle(moves)` 
  - `moves`: the number of rotations to use to shuffle the cube
  - Randomly decides which face to rotate in which direction
    - Not allowed to do the reverse of the last move
    - IE Last move was White counter-clockwise, next move can't be White clockwise
- `validate()` return boolean
  - Validates that the cube is in a valid state
  - Need to look into how to do this
- `complete()` return boolean
  - Returns true if the cobe is complete

## Face enum

- Values
    - Green, Red, Blue, Orange, White, Yellow
- `toChar()` return char
  - Returns first char of value name
- `up()` return Face
  - returns the face that would be above
- `down()` return Face
  - returns the face that would be below
- `left()` return Face
  - returns the face that would be to the left
- `right()` return Face
  - returns the face that would be to the right
- `back()` return Face
  - returns the face that would be behind
  - Unsure if it will be useful

