def get_age():
 while True:
  try:
    n=int(input('how old are you?'))
    return n
  except ValueError:
    print('Please enter an integer value.')

get_age()
