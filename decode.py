from PIL import Image,ImageDraw
import math

def decode(text):
	l=int(len(text)/6)
	decoded_text=''
	for pos in range(l):
	    char='1'+text[pos*6:(pos+1)*6]
	    decoded_text+=chr(int(char,2))
	return decoded_text

im=Image.open("file.png")
pixels=im.load()
length=''
for rght in range(16):
    if(pixels[rght,399]==(255,255,254)):
        length+='0'
    else:
        length+='1'
length=int(length,2)*6
print(length)
data=''
size=math.floor(math.sqrt(400*400/length)) #width x height	
base=int(size/2)
end_len=int(400/size)
for rght in range(end_len):
    for dwn in range(end_len):	
        px=pixels[base + rght*size, base +dwn*size ]
        if px==(255, 255, 255):
            data+='0'
        else:
            data+='1'
print(decode(data))
