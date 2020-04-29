import pysystems
solve = pysystems.solve
def test2():
  assert solve("2x+y=14", "2x+17y=21") == (6.78125, 0.4375)
def test3():
  assert solve("2x+7y+3z=5", "3x+12y+z=91", "2x+9y+z=11") == (189.5, -36.5, -39.5)
