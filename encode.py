from PIL import Image,ImageDraw
import math

def convertToBinary(text):
	encoded_string=''
	for char in text:
		encoded_string+=bin(ord(char))[-6:]
	return encoded_string

    
print("Enter Text To Encode:")
txt=input().strip()
data=convertToBinary(txt)
length=len(data)
nearest_sq=math.ceil(math.sqrt(length))
print("nearest:",nearest_sq)
size=math.floor(math.sqrt(400*400/length)) #	width x height	
print("length is:",len(txt))

sizeInBin=bin(len(txt))[2:]
sizeInBin='0'*(16-len(sizeInBin))+sizeInBin

im=Image.new('RGB',(500,500	),'white')
draw=ImageDraw.Draw(im)
print("size is:",size)	
end_len=int(400/size)
print("end_len:",end_len)
pos=0
for rght in range(end_len):
    for dwn in range(end_len):	
        if pos>=length:
            	break
        cord=[(rght*size,size*dwn),((rght+1)*size,size*(dwn+1))]
        if(data[pos]=='1'):
            draw.rectangle(cord,fill='black')
        pos+=1
pixels=im.load()
for rght in range(16):
    if(sizeInBin[rght]=='0'):
        pixels[rght,399]=(255,255,254)
    else:
        pixels[rght,399]=(255,254,255)
    

im.show()
print("Do you want to save? Y/N")
inp=input().strip()
if(inp=="Y"):
    im.save("file.png")
    im.close()
else:
    im.close()
