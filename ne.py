import numpy as np

a = np.array([[10,0,20,11,15],[12,7,9,20,25],[0,14,16,18,5],[5,15,15,10,45]])

#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      #for row in a]))
#Northwest
def Nortwest(a):
  print(a)
  aux=a[-1][-1]
  aux2= np.array([[aux]])
  while a[-1][-1]==aux:
    comparar=np.array_equal(a,aux2)
    if comparar==True:
      break
    
    if a[0][-1]>a[-1][0]:
      a[0][-1]=a[0][-1]-a[-1][0]
    else:
      a[-1][0]=a[-1][0]-a[0][-1]
      a[0][-1]=0
    if a[0][-1]!=0:
      print("se cumplio con la demanda, elimina columna")
      a=np.delete(a, 0, axis=1)
      print(a)
    else:
      print("se acabo la oferta, elimina fila")
      a=np.delete(a, 0, axis=0)
      print(a)
  return

norte= Nortwest(a)
