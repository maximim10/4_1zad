from PIL import Image, ImageDraw
inp=input().split()
try:
    image_inp=inp[0]
except:
    image_inp="8d39c54cae428ce3b7531326f5721614.png"
try:
    image_out=inp[1]
except:
    image_out="out.jpg"
try:
    image=Image.open(image_inp)
except:
    print ("Net Faila")
else:
    draw=ImageDraw.Draw(image)
    pix=image.load()
    br=0;
    for i in range (image.size[0]):
        for j in range (image.size[1]):
            if br<pix[i,j][0]+pix[i,j][1]+pix[i,j][2]:
                br=pix[i,j][0]+pix[i,j][1]+pix[i,j][2];
    for i in range (image.size[0]):
        for j in range (image.size[1]):
            a=pix[i,j][0]
            b=pix[i,j][1]
            c=pix[i,j][2]
            k=br/(a+b+c) if a+b+c>0 else 0;
            a=int(a*k) if a*k<255 or k==0 else 255;
            b=int(b*k) if b*k<255 or k==0 else 255;
            c=int(c*k) if c*k<255 or k==0 else 255;
            draw.point((i,j),(a,b,c))
    image.save(image_out,"jpeg")

    image.show()
