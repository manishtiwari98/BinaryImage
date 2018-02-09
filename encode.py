from PIL import Image,ImageDraw
import math

def convertToBinary(text):
	encoded_string=''
	for char in text:
		bin_text=bin(ord(char))[-7:]
		if bin_text[0]=='b':
		    bin_text='0'+bin_text[1:]
		encoded_string+=bin_text
		
	return encoded_string

    
print("Enter Text To Encode:")
txt=input().strip()
data=convertToBinary(txt)
length=len(data)

nearest_sq=math.ceil(math.sqrt(length))

#print("nearest:",nearest_sq)
#size=math.floor(math.sqrt(400*400/length))  #width x height	

size=int(400/nearest_sq)
#print("length is:",len(txt))

#converting lenghth of data to 16 digit binary, which will be used in decoding.......
lengthInBin=bin(len(txt))[2:]
lengthInBin='0'*(16-len(lengthInBin))+lengthInBin

im=Image.new('RGB',(500,500),'white')
draw=ImageDraw.Draw(im)
	
end_len=int(400/size)

pos=0
for rght in range(end_len):
    for dwn in range(end_len):	
        if pos>=length:
            	break
        cord=[(rght*size,size*dwn),((rght+1)*size,size*(dwn+1))]
        if(data[pos]=='1'):
            draw.rectangle(cord,fill='black')
        pos+=1

#Hiding data length....
pixels=im.load()
for rght in range(16):
    if(lengthInBin[rght]=='0'):
        pixels[rght,399]=(255,255,254)
    else:
        pixels[rght,399]=(255,254,255)
    

im.show()
im.save("file.png")
im.close()	
