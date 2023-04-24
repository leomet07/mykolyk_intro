def makeSentence(words):
  s = ""
  if len(words) == 0:
    return s
  for i in range(len(words) - 1):
    s+=words[i] + " "
  s+= words[len(words) - 1]
  return s

def breakSentence(s):
  words = [""]
  if s == "":
    return []
  for c in s:
    if c != " ":
      words[-1] = words[-1] + c
    else:
      words.append("")
  return words


def zipLists( a, b ):
  c= []
  for i in range(max(len(a), len(b))):
    if i< len(a):
      c.append(a[i])
    if i < len(b):
      c.append(b[i])
  return c

def cleanList( data, thingsToRemove ):
  for t in thingsToRemove:
    while t in data:
      data.remove(t)
  return data

def MergeWords(a,b):
  return [a[i] + b[i] for i in range(len(a))]

def foundFirst(data,x,y):
  
  notFound = False
  
  try:
    xi = data.index(x)
  except:
    xi = -1
    notFound = True
  try:
    yi = data.index(y)
  except:
    yi = -1
    notFound = True
  
  return max(xi, yi) if notFound else min(xi, yi)

def stripList( data, thingsToRemove ):
  indexes = []
  # Remove from start
  for i in range(len(data)):
    e = data[i]
    if e in thingsToRemove:
      indexes.append(i)
    else:
      break
    
  # Remove from end
  for i in range(len(data)):
    e = data[len(data) - 1 - i]
    if e in thingsToRemove:
      indexes.append(len(data) - 1 - i)
    else:
      
      break
  
  # Removal of indexes marked for deletion without mutating original list
  newdata = []
  for d in range(len(data)):
    if d not in indexes:
      newdata.append(data[d])
  return newdata
      
