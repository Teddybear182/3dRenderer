import sys
import pygame as pg
import utils.model_loader as model_loader
import utils.simple_cube as cube
from utils.matrix_functions import rotate_x, rotate_y, rotate_z

filepath = input("\n >> enter model path or type 'cube' to render 3d cube: ")
if filepath == "cube":
  cube_obj = cube.SimpleCube()
  points, faces = cube_obj.get_vertices(), cube_obj.get_faces()
else:
  points, faces = model_loader.get_faces(str(filepath))

pg.init()
HEIGHT, WIDTH = 600, 500
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()
scale = 100
angle_x, angle_y, angle_z = 0,0,0

def project_point(point):
  x = int(point[0] * scale + WIDTH//2)
  y = int(point[1] * scale + HEIGHT//2)
  return (x,y)

def connect_points(a,b):
  pg.draw.line(screen, 'goldenrod', a, b)

while True:
  pg.display.set_caption(f"3d renderer, fps = {clock.get_fps()}")
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
    
  key = pg.key.get_pressed()
  if key[pg.K_UP] or key[pg.K_w]:
    angle_x-=1 / clock.get_fps()
  if key[pg.K_DOWN] or key[pg.K_s]:
    angle_x+=1 / clock.get_fps()
  if key[pg.K_LEFT] or key[pg.K_a]:
    angle_y+=1 / clock.get_fps()
  if key[pg.K_RIGHT] or key[pg.K_d]:
    angle_y-=1 / clock.get_fps()
  if key[pg.K_e]:
    scale-=10 / clock.get_fps()
  if key[pg.K_q]:
    scale+=10 / clock.get_fps()

  screen.fill('black')

  rotated_points = []

  for p in points:
    rp = rotate_x(p, angle_x)
    rp = rotate_y(rp, angle_y)
    rp = rotate_z(rp, angle_z)
    rotated_points.append(rp)

  projected_points = [project_point(p) for p in rotated_points]

  # for x,y in projected_points:
  #   pg.draw.ellipse(screen, 'white', (x,y,5,5))

  for face in faces:
    for i in range(len(face)):
      x = projected_points[face[i]]
      y = projected_points[face[(i+1) % len(face)]]
      connect_points(x, y)

  pg.display.update()
  clock.tick(120)
