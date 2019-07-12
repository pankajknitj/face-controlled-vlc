import cv2 as cv
import vlc
import random as r

ps=list                       #previous state
psp=list
track=['D:\Downloads\Video\(643) Tu Cheez Badi 4k Video song - YouTube.MKV',
       'D:\Downloads\Video\(643) Official Video- Humnava Mere Song - Jubin Nautiyal - Manoj Muntashir - Rocky - Shiv - Bhushan Kumar - YouTube.MKV',
       'D:\Downloads\Video\(643) Full Video- Tera Yaar Hoon Main - Sonu Ke Titu Ki Sweety - Arijit Singh Rochak Kohli - Song 2018 - YouTube.MKV',
       'D:\Downloads\Video\(643) Yo Yo Honey Singh- DIL CHORI (Video) Simar Kaur, Ishers - Hans Raj Hans - Sonu Ke Titu Ki Sweety - YouTube.MKV,',
       'D:\Downloads\Video\(643) Saiyaara - Full Song - Ek Tha Tiger - Salman Khan - Katrina Kaif - Mohit Chauhan - Taraannum Mallik - YouTube.MKV',
       'D:\Downloads\Video\(643) Bom Diggy Diggy (VIDEO) - Zack Knight - Jasmin Walia - Sonu Ke Titu Ki Sweety - YouTube.MKV']


v=cv.VideoCapture(0)
fd=cv.CascadeClassifier(r'C:\Users\pankaj kumar\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
#fde=cv.CascadeClassifier(r'C:\Users\pankaj kumar\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_eye.xml')
fdp=cv.CascadeClassifier(r'C:\Users\pankaj kumar\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\open_palm.xml')
player=vlc.MediaPlayer('D:\Downloads\Video\(643) Tu Cheez Badi 4k Video song - YouTube.MKV')
while True:
    status,image=v.read()
    if status==True:
        gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        f=fd.detectMultiScale(gray_image)
        for [x,y,w,h]in f:
            cv.rectangle(image,(x,y),(x+w,y+h),(255,255,255),1)
            '''gray_face=gray_image[y:y+h,x:x+w]
            face=image[y:y+h,x:x+h]
            g=fde.detectMultiScale(gray_face)
            
            for [xe,ye,we,he] in g:
                cv.rectangle(face,(xe,ye),(xe+we,ye+he),(0,0,255),2)'''


        j=fdp.detectMultiScale(gray_image)       
        for [xp,yp,wp,hp] in j:
            cv.rectangle(image,(xp,yp),(xp+wp,yp+hp),(0,255,0),2)


        cs=type(j)
        if psp!=cs:
            psp=cs
            if type(j)==type(f):
                player.stop()
                player=vlc.MediaPlayer(track[r.randint(0,5)])           #5 also be included not excluded here in randint()
                player.play()
            
        k=cv.waitKey(3)
        if k==ord('q'):
            cv.destroyAllWindows()
            player.stop()
            break
        cs=type(f)
        if ps!=cs:
            ps=cs
            if type(f)==tuple:
                player.pause()
            else:
                player.play()


        
        
        cv.imshow('my image',image)    
                      
                        
