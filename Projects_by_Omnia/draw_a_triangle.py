def draw_a_triangle (a : int):
  """
  function draw a triangle

  parameters:
  a: number of stars

  returns:
  draw
  """
  c = ''

  for i in range(a, 0, -1):

      c += ('*' * i)+'\n'

  return c