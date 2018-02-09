from PIL import Image,ImageDraw
import math

def decode(text):
	l=int(len(text)/7)
	decoded_text=''
	for pos in range(l):
	    char=text[pos*7:(pos+1)*7]
	    decoded_text+=chr(int(char,2))
	return decoded_text

im=Image.open("file.png")
pixels=im.load()
lengthInBin=''
for rght in range(16):
    if(pixels[rght,399]==(255,255,254)):
        lengthInBin+='0'
    else:
        lengthInBin+='1'
length=int(lengthInBin,2)*7
#print(length)
data=''
#size=math.floor(math.sqrt(400*400/length)) #width x height	

nearest_sq=math.ceil(math.sqrt(length))
size=int(400/nearest_sq)
base=int(size/2)
end_len=int(400/size)
#Extracing data from Image
pos=0
for rght in range(end_len):
    for dwn in range(end_len):
        if pos>=length:
           break	
        px=pixels[base + rght*size, base +dwn*size ]
        if px==(255, 255, 255):
            data+='0'
        else:
            data+='1'
        pos+=1
print(decode(data))
