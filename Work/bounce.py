# bounce.py
#
# Exercise 1.5
"""
A rubber ball is dropped from a height of 100 meters and each time it hits the ground,
it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints
a table showing the height of the first 10 bounces.
"""
height = 100
bounce = 0
while bounce < 10:
  height = height * .6
  bounce += 1
  print(bounce, round(height, 4))
  
  
