# mode 1 is 3 varible equation, mode 0 is 2 varible equation
def solve(*args):
  
  if len(args) == 2:
    equation1 = args[0]
    equation2 = args[1]
    x = equation1.split("=")
    y = x[0].split("+")
    try:
      c1 = float(x[1].replace(" ", ""))
    except:
      c1 = 1
    try:
      a1 = float(y[0].split("x")[0].replace(" ", ""))
    except:
      a1 = 1
    try:
      b1 = float(y[1].split("y")[0].replace(" ", ""))
    except:
      b1 =1
    x = equation2.split("=")
    y = x[0].split("+")
    try:
      c2 = float(x[1].replace(" ", ""))
    except:
      c2 = 1
    try:
      a2 = float(y[0].split("x")[0].replace(" ", ""))
    except:
      a2 = 1
    try:
      b2 = float(y[1].split("y")[0].replace(" ", ""))
    except:
      b2 =1
    d = (a1*b2)-(b1*a2)
    d1 = (c1*b2)-(b1*c2)
    d2 = (a1*c2)-(c1*a2)
    if d != 0:
      solved_x = d1/d
      solved_y = d2/d
      return solved_x, solved_y
    else:
      return "No Unique Value", "No Unique Value"
  elif len(args) == 3:
    equation1 = args[0]
    equation2 = args[1]
    equation3 = args[2]
    x = equation1.split("=")
    y = x[0].split("+")

    d1 = float(x[1].replace(" ", ""))
    try:
      a1 = float(y[0].split("x")[0].replace(" ", ""))
    except:
      a1 = 1
    try:
      b1 = float(y[1].split("y")[0].replace(" ", ""))
    except:
      b1 = 1
    try:
      c1 = float(y[2].split("z")[0].replace(" ", ""))
    except:
      c1 = 1
    x = equation2.split("=")
    y = x[0].split("+")

    d2 = float(x[1].replace(" ", ""))
    try:
      a2 = float(y[0].split("x")[0].replace(" ", ""))
    except:
      a2 = 1
    try:
      b2 = float(y[1].split("y")[0].replace(" ", ""))
    except:
      b2 = 1
    try:
      c2 = float(y[2].split("z")[0].replace(" ", ""))
    except:
      c2 = 1
    x = equation3.split("=")
    y = x[0].split("+")

    d3 = float(x[1].replace(" ", ""))
    try:
      a3 = float(y[0].split("x")[0].replace(" ", ""))
    except:
      a3 = 1
    try:
      b3 = float(y[1].split("y")[0].replace(" ", ""))
    except:
      b3 = 1
    try:
      c3 = float(y[2].split("z")[0].replace(" ", ""))
    except:
      c3 = 1
    d = (a1*b2*c3) + (b1*c2*a3) + (c1*a2*b3) - (a3*b2*c1) - (b3*c2*a1) - (c3*a2*b1)
    if d != 0:
       dx = float((d1*b2*c3) + (b1*c2*d3) + (c1*d2*b3) - (d3*b2*c1) - (b3*c2*d1) - (c3*d2*b1))
       dy = float((a1*d2*c3) + (d1*c2*a3) + (c1*a2*d3) - (a3*d2*c1) - (d3*c2*a1) - (c3*a2*d1))
       dz = float((a1*b2*d3) + (b1*d2*a3) + (d1*a2*b3) - (a3*b2*d1) - (b3*d2*a1) - (d3*a2*b1))
       solved_x = dx/d
       solved_y = dy/d
       solved_z = dz/d
       return solved_x, solved_y, solved_z
    else:
      return "No Unique Value", "No Unique Value", "No Unique Value"
  else:
    return "Only supports systems with 2 or 3 equations"
