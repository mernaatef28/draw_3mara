import numpy as np
from PIL import Image
w , h = 800 , 800 
img = np.zeros((w,h,3) ,dtype=np.uint8 )
img[:] =(135, 206 ,235) # the RGB colors assigned to img 
#img[top:bottom , left:right ]
img [int (h* .80 ) :h , 0:w] =(178 , 190 ,181) # the road 
img [int (h* .1) :int (h*.9), int(w*.2):int(w*.65)] =(95, 100 ,101)# el3mara
#windows 
for row in range(6):
    for col in range (5):
        if np.random.randint(0,8)==5 :
            win_color = (240 , 230 , 140)
        else :
            win_color=(30 , 22, 40)
        img[int(h*.1 +100 * row +20 ): int (h*.1 +100 * row +60+20)
            , int (w*.2 +75*col +15 ): int (w*.2 +75*col +30+15)] = win_color
Image.fromarray(img).save('3mara.png') 