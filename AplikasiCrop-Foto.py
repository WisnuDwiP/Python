import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import messagebox as mBox
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
from tkinter.filedialog import askopenfilename, askdirectory
import cv2
import glob
import os
  

class Main:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
        lebar = 900
        tinggi = 690
        setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
        setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        self.parent.config(bg="#a1dbcd")
        self.komponen()

    #----------------------------Aksi Image Processing--------------------------------#
    
    def ambil(self):
        
        try:
            self.img = self.Im
        except:
            try:
                self.img = Image.open(self.filename)
            except:
                return
          

    def proses(self):
        
        #size digunakan untuk meresize image menjadi 350x350
        self.imgtk = self.Im.resize((350,350))

        #gambar didefinisikan ke function imagetk supaya support tkinter
        images = ImageTk.PhotoImage(self.imgtk)

        #memasukan gambar ke objek tkinter 
        self.lbimage.config(image=images)
        self.lbimage.image = images
        

    def OnColor(self,event):
        
        try:
            img = Image.open(self.filename) 
        except:
            return
            
        #mendapatkan nilai
        num = self.trackColor.get()

        #menempatkan gambar dengan function ImageEnhance (color)
        enh = ImageEnhance.Color(img)
        #membuat gambar di enhance dengan nilai yg di dpt dri vairable num
        self.Im = enh.enhance(num)

        self.proses()

        self.trackContrast.set(0)
        self.trackBrightness.set(0)
        self.trackSharpness.set(0)
    

    def OnContrast(self,event):
        
        try:
            img = Image.open(self.filename)
        except:
            return

        #mendapatkan nilai
        num = self.trackContrast.get()

        #menempatkan gambar dengan function ImageEnhance (contrast)
        enh = ImageEnhance.Contrast(img)
        #membuat gambar di enhance dengan nilai yg di dpt dri vairable num
        self.Im = enh.enhance(num)

        self.proses()
        
        self.trackBrightness.set(0)
        self.trackColor.set(0)
        self.trackSharpness.set(0)
    

    def OnBrightness(self,event):
        
        try:
            img = Image.open(self.filename) 
        except:
            return

        #mendapatkan nilai
        num = self.trackBrightness.get()

        #menempatkan gambar dengan function ImageEnhance (Brightness)
        enh = ImageEnhance.Brightness(img)
        #membuat gambar di enhance dengan nilai yg di dpt dri vairable num
        self.Im = enh.enhance(num)

        self.proses()

        self.trackContrast.set(0)
        self.trackColor.set(0)
        self.trackSharpness.set(0)
       

    def OnSharpness(self,event):
        
        try:
            img = Image.open(self.filename) 
        except:
            return

        #mendapatkan nilai
        num = self.trackSharpness.get()

        #menempatkan gambar dengan function ImageEnhance (Sharpness)
        enh = ImageEnhance.Sharpness(img)
        #membuat gambar di enhance dengan nilai yg di dpt dri vairable num
        self.Im = enh.enhance(num)

        self.proses()

        self.trackBrightness.set(0)
        self.trackColor.set(0)
        self.trackContrast.set(0)
    

    def gray(self):
        
        try:
            self.ambil()
            self.Im = self.img.convert('L')
            self.proses()
        except:
            return


    def emboss(self):
        
        try:
            self.ambil()
            self.Im = self.img.filter(ImageFilter.EMBOSS)
            self.proses()
        except:
            return


    def contour(self):
        
        try:
            self.ambil()
            self.Im = self.img.filter(ImageFilter.CONTOUR)
            self.proses()
        except:
            return    
    

    def blur(self):
        
        try:
            self.ambil()
            num = float(self.enBlur.get())
            self.Im = self.img.filter(ImageFilter.GaussianBlur(radius=num))
            self.proses()
        except:
            return
        

    def flip_x(self):
        
        try:
            self.ambil()
            self.Im = self.img.transpose(Image.FLIP_LEFT_RIGHT)
            self.proses()
        except:
            return


    def flip_y(self):
        
        try:
            self.ambil()
            self.Im = self.img.transpose(Image.FLIP_TOP_BOTTOM)

            self.proses()
        except:
            return

        
    def rotate_90(self):
        
        try:
            self.ambil()
            self.Im = self.img.transpose(Image.ROTATE_90)
            self.proses()
        except:
            return

        
    def rotate_180(self):
        
        try:
            self.ambil()
            self.Im = self.img.transpose(Image.ROTATE_180)
            self.proses()
        except:
            return
     
        
    def rotate_270(self):
        
        try:
            self.ambil()
            self.Im = self.img.transpose(Image.ROTATE_270)
            self.proses()
        except:
            return

    #-------------------------- Aksi Form ----------------------------------#

    def keluar(self,event=None):
        self.parent.destroy()

    def opfile(self,event=None):

        self.filename = tkinter.filedialog.askopenfilename()
        
        if len(self.filename) > 0:
            self.Im = Image.open(self.filename)
        else:
            return

        self.proses()

        self.trackColor.config(state='normal')
        self.trackContrast.config(state='normal')
        self.trackBrightness.config(state='normal')
        self.trackSharpness.config(state='normal')


    def reset(self):

        try:
            self.trackContrast.set(0)
            self.trackColor.set(0)
            self.trackSharpness.set(0)
            self.trackBrightness.set(0)
            self.trackX.set(0)
            self.trackY.set(0)
            self.Im = Image.open(self.filename)
            self.enBlur.delete(0, END)
            self.proses()
            
        except:
            return

            
    def save(self):
        
        try:
            self.Im.save('output.png','png')
            mBox.showwarning('Informasi Penting','File gambar anda telah tersimpan sebagai output.png')
        except:
            return

    def _quit(self, event=None):
        self.parent.destroy()

    def _paspoto(self):
        
        
        mBox.showwarning('Informasi Penting','Hanya Mendukung Gambar Dengan Format *.jpg')
        self.folderpath = tkinter.filedialog.askdirectory()
        cascpath = "asset/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascpath)

        files = glob.glob(self.folderpath + "/*.*")

        for file in files:



            image = cv2.imread(file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			
			
			
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )

            print("Found {0} faces!".format(len(faces)))

            left = 320
            right = 320
            top = 220
            bottom = 700

            #n = 0
            for (x, y, w, h) in faces:
                print(x, y, w, h)

            image = image[y-top:y+h+bottom, x-left:x+w+right]

            image_resize = cv2.resize(image, (549,673))

            print("terpotong_{1}{0}".format(str(file),str(x)))
            cv2.imwrite(os.path.join("DataOutput/", str(file)), image_resize)
            cv2.destroyAllWindows()
            
        mBox.showinfo('Informasi Penting','File gambar anda telah jadi pas poto')

    #--------------------------Komponen Form----------------------------------------------------------------------------------#

    def komponen(self):
	
		#form window
        frameFoto = Frame(self.parent,width=350,bg="#a1dbcd")
        frameFoto.grid(column=0,row=0,sticky=NW,pady=10,padx=10)

        frameKosong = Frame(self.parent,width=350,bg="#a1dbcd")
        frameKosong.grid(column=0,row=1,sticky=NW,pady=10,padx=10)

        frameBtn = Frame(self.parent,width=300,bg="#a1dbcd")
        frameBtn.grid(column=1,row=0,sticky=N ,pady=10,padx=20)

        frameBtn2 = Frame(self.parent,width=300,bg="#a1dbcd")
        frameBtn2.grid(column=2,row=0,sticky=N, pady=10,padx=20)

        frameFoot = Frame(self.parent,width=1050)
        frameFoot.grid(row=2,sticky=N,column=0,columnspan=35)
        
       
        self.lbfoot = Label(frameFoot,width=132,height=2,bg="#444",fg="white",text="Copyright@ By Wisnu Dwi Pamungkas")
        self.lbfoot.grid(row=0,column=0,sticky=S)


        #default image
        img = Image.open("asset/default.png")
        images = ImageTk.PhotoImage(img)
        
        self.lbimage = Label(frameFoto,image=images)
        self.lbimage.grid(row=0,column=0,sticky=NW,padx=10,pady=10,columnspan=2)
        self.lbimage.image = images

        self.btnBrowse = Button(frameFoto, text='Browse',command=self.opfile,width=22,height=2,bg="teal",fg="white",relief=FLAT)
        self.btnBrowse.grid(row=1,column=0,sticky=W,pady=10,padx=10)

        self.btnReset = Button(frameFoto, text='Reset',command=self.reset,width=22,height=2,bg="#F55858",fg="white",relief=FLAT)
        self.btnReset.grid(row=1,column=1,sticky=W)

        self.btnSave = Button(frameFoto, text='Save',command=self.save,width=49,height=2,bg="#4DBAF8",fg="white",relief=FLAT)
        self.btnSave.grid(row=3,column=0,sticky=W,pady=10,padx=10,columnspan=2)

        self.btnPasPoto = Button(frameFoto, text='Cropping Poto', command=self._paspoto, width=49, height=2, bg="#4DBAF8", fg="white",relief=FLAT)
        self.btnPasPoto.grid(row=5, column=0, sticky=W, pady=10, padx=10, columnspan=2)
        
        self.btnExit = Button(frameFoto, text='Exit', command=self._quit, width=49, height=2, bg="#4DBAF8", fg="white",relief=FLAT)
        self.btnExit.grid(row=7, column=0, sticky=W, pady=10, padx=10, columnspan=2)

        
        #Image Enhanced
        lb = Label(frameBtn, text='Image Enhance',height=2,width=28,bg="#444",fg="white",relief=FLAT)
        lb.grid(row=0,column=0,sticky=W,pady=10)
        
        self.trackColor = Scale(frameBtn,length=200,label="Color Balance",state='disabled',bg="white",fg="#444",\
                                relief=FLAT,bd=0, resolution=0.1,from_=1,to=10,orient=HORIZONTAL)
        self.trackColor.grid(row=1,column=0,sticky=W)
        self.trackColor.bind("<ButtonRelease-1>", self.OnColor)

        self.trackContrast = Scale(frameBtn,length=200,label="Contrast",state='disabled',bg="white",fg="#444",\
                                   relief=FLAT,bd=0, resolution=0.1,from_=1,to=10,orient=HORIZONTAL)
        self.trackContrast.grid(row=2,column=0,sticky=W)
        self.trackContrast.bind("<ButtonRelease-1>", self.OnContrast)
        
        self.trackBrightness = Scale(frameBtn,length=200,label="Brightness",state='disabled',bg="white",fg="#444",\
                                     relief=FLAT,bd=0, resolution=0.1,from_=1,to=10,orient=HORIZONTAL)
        self.trackBrightness.grid(row=3,column=0,sticky=W)
        self.trackBrightness.bind("<ButtonRelease-1>", self.OnBrightness)
        
        self.trackSharpness = Scale(frameBtn,length=200,label="Sharpness",state='disabled',bg="white",fg="#444",\
                                    relief=FLAT,bd=0,resolution=0.1,from_=1,to=10,orient=HORIZONTAL)
        self.trackSharpness.grid(row=4,column=0,sticky=W)
        self.trackSharpness.bind("<ButtonRelease-1>", self.OnSharpness)
        

        #Image Filter
        lb = Label(frameBtn2, text='Image Filter',height=2,width=28,bg="#444",fg="white",relief=FLAT)
        lb.grid(row=0,column=0,sticky=W,pady=10,columnspan=4)

        self.btnGray = Button(frameBtn2, text='Grayscale',command=self.gray,width=28,height=2,bg="white",fg="#444",relief=FLAT)
        self.btnGray.grid(row=1,column=0,sticky=W,pady=10,columnspan=4)

        self.btnContour = Button(frameBtn2, text='Contour',command=self.contour,width=15,height=2,bg="white",fg="#444",relief=FLAT)
        self.btnContour.grid(row=2,column=0,sticky=W,pady=10,columnspan=2)

        self.btnEmboss = Button(frameBtn2, text='Emboss',command=self.emboss,width=10,height=2,bg="white",fg="#444",relief=FLAT)
        self.btnEmboss.grid(row=2,column=2,sticky=W,pady=10,columnspan=2)

        lb_blur = Label(frameBtn2, text="Radius :",bg="#444",fg="white", width=4, bd=12)
        lb_blur.grid(row=4, column=0,sticky=W,pady=10)

        self.enBlur = Entry(frameBtn2,fg="white", bg="#444", width=7, bd=12, relief=FLAT)
        self.enBlur.grid(row=4, column=1,sticky=W)

        self.btnBlur = Button(frameBtn2, text='Blur',command=self.blur,width=10,height=2,bg="white",fg="#444",relief=FLAT)
        self.btnBlur.grid(row=4,column=2,sticky=W,columnspan=2)


        #Image Transpose
        lb = Label(frameBtn2, text='Image Transpose',height=2,width=28,bg="#444",fg="white",relief=FLAT)
        lb.grid(row=5,column=0,sticky=W,pady=10,columnspan=4)

        lb_flip = Label(frameBtn2, text="Flip :",bg="#444",fg="white", width=4, bd=12)
        lb_flip.grid(row=6, column=0,sticky=W,pady=10)

        self.btnFx = Button(frameBtn2, text='Horizontal',command=self.flip_x,width=9,height=2,bg="white",fg="#444",relief=FLAT)
        self.btnFx.grid(row=6,column=1,sticky=W)

        self.btnFy = Button(frameBtn2, text='Vertical',command=self.flip_y,width=10,height=2,bg="white",fg="#444",relief=FLAT)
        self.btnFy.grid(row=6,column=2,sticky=W,columnspan=2)

        lb_rotate = Label(frameBtn2, text="Rotate :",bg="#444",fg="white", width=4, bd=12)
        lb_rotate.grid(row=7, column=0,sticky=W,pady=10)

        self.btnRot = Button(frameBtn2, text='90',command=self.rotate_90,width=9,height=2,bg="white",fg="#444",relief=FLAT)
        self.btnRot.grid(row=7,column=1,sticky=W)

        self.btnRot = Button(frameBtn2, text='180',command=self.rotate_180,width=4,height=2,bg="white",fg="#444",relief=FLAT)
        self.btnRot.grid(row=7,column=2,sticky=W)

        self.btnRot = Button(frameBtn2, text='270',command=self.rotate_270,width=5,height=2,bg="white",fg="#444",relief=FLAT)
        self.btnRot.grid(row=7,column=3,sticky=W)

root = Tk()
Main(root, "Aplikasi Editor Foto & Cropping Foto  Batch Otomatis")
root.mainloop()