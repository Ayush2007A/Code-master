
from PIL import Image
#img = Image.open(path)	 
# On successful execution of this statement, 
# an object of Image type is returned and stored in img variable) 

try: 
	img = Image.open('A:\python\spanso_\icon.png') 
except IOError: 
	pass
