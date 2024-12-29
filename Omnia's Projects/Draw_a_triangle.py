def draw (a : int):
  """
  function draw a triangle

  parameters:
  a: number of stars

  returns:
  draw
  """
  
  
#  a = int (input ("Enter a number"))
  c = ''
#  r = ''
  for i in range(a, 0, -1):
#    for j in range (i):
      c += ('*' * i)+'\n'
#    r+= c +'\n'
  return c
triangle = draw (8)
print (triangle) 
