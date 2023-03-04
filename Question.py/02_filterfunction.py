#filter function
#It return a iterator where the items are filtered through a function to test if the item is acceptd or not
name = ["sarthak","dev","piyush","udit"]

def Cloudburst(name):
  if name=="udit":
    return False
  else:
    return True

List = filter(Cloudburst, name)

for x in List:
  print(x)
