def get_faces(filename):
  vertices = []
  faces = []
  try:
    with open(filename) as file:
      for line in file:
        if line.startswith('v '):
          vertices.append([float(i) for i in line.split()[1:]])
        elif line.startswith('f '):
          faces.append([int(i.split('/')[0]) - 1 for i in line.split()[1:]])
  except Exception as e:
    print(f"Something went wrong! Error: {e}")
  return vertices, faces
    