import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
  xmin = domain[0]
  xmax = domain[1]

  xs = []
  ys = []

  step = (xmax - xmin) / (ns - 1)

  for i in range(ns):
    x = xmin + i * step
    xs.append(x)

    y = eval(fun_str)
    ys.append(y)

  print()
  print("{:<15} {:<15}".format("x", "y"))
  print("-" * 30)

  for i in range(ns):
    print("{:<15.4f} {:<15.4f}".format(xs[i], ys[i]))

  plt.plot(xs, ys)
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Function: " + fun_str)
  plt.grid(True)
  plt.show()

fun_str = input("Enter function with variable x: ")

xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

ns = int(input("Enter number of samples: "))

domain = (xmin, xmax)

plot_function(fun_str, domain, ns)
