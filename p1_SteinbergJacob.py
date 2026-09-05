import the math module
import matplotlib.pyplot

while True:
  a_input = input("Enter coefficient a: ")

  if a_input == "":
    print("Program ended")
    break

  a = float(a_input)
  b = float(input("Enter coefficient b: "))
  c = float(input("Enter coefficient c: "))

  D = b**2 - 4*a*c

  if D < 0:
    print("no real solutions")
    vertex_x = -b / (2*a)
    x_min = vertex_x - 10
    x_max = vertex_x + 10

  elif D == 0:
    x1 = -b / (2*a)
    print("one solution", x1)

    x_min = x1 - 10
    x_max = x1 + 10

  else:
    x1 = (-b + math.sqrt((D)) / (2*a)
    x2 = (-b - math.sqrt((D)) / (2*a)

    print("two solutions:", x1, x2)

    x_min = min(x1, x2) - 5
    x_max = max(x1, x2) + 5

  x_values = []
  y_values = []

  number_of_points = 200
  step = (x_max - x_min) / number_of_points

  x = x_min

  while x <= x_max:
     y = a*x**2 + b*x + c

     x_values.append(x)
     y_values.append(y)

     x += step

  plt.plot(x_values, y_values)

  plt.axhline(0)
  plt.axvline(0)

  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Quadratic Function")

  plt.grid(True)
  plt.show()
   
   
   

 
          
    
