class SimpleCube:
  def __init__(self):
    self.points = [n for n in range(8)]
    self.points[0] = [[-1], [-1], [1]]
    self.points[1] = [[1], [-1], [1]]
    self.points[2] = [[1], [1], [1]]
    self.points[3] = [[-1], [1], [1]]
    self.points[4] = [[-1], [-1], [-1]]
    self.points[5] = [[1], [-1], [-1]]
    self.points[6] = [[1], [1], [-1]]
    self.points[7] = [[-1], [1], [-1]]

    self.faces = [
      [0, 1, 2, 3],
      [4, 5, 6, 7],
      [0, 1, 5, 4], 
      [2, 3, 7, 6], 
      [1, 2, 6, 5], 
      [0, 3, 7, 4]
    ]

  def get_vertices(self):
    return self.points
  
  def get_faces(self):
    return self.faces