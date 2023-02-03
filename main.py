import os
Varjpg=0
Varjpeg=0
Varmp3=0
Vartxt=0
Varjs=0
Varpdf=0

def convertMp3(filename):
    if not 'MP3' in os.listdir():
     os.mkdir('MP3')
    global Varmp3
    Varmp3=Varmp3+1
    os.rename(filename,f"MP3/{Varmp3}.mp3")

def convertJpg(filename):
    if not 'JPG' in os.listdir():
      os.mkdir('JPG')
    global Varjpg
    Varjpg=Varjpg+1
    os.rename(filename,f"JPG/{Varjpg}.jpg")


def convertJpeg(filename):
    if not 'JPEG' in os.listdir():
     os.mkdir('JPEG')
    global Varjpeg
    Varjpeg=Varjpeg+1
    os.rename(filename,f"JPEG/{Varjpeg}.jpeg")
def convertPdf(filename):
    if not 'PDF' in os.listdir():
     os.mkdir('PDF')
    global Varpdf
    Varpdf=Varpdf+1
    os.rename(filename,f"PDF/{Varpdf}.pdf")
def convertJs(filename):
    if not 'JS' in os.listdir():
     os.mkdir('JS')
    global Varjs
    Varjs=Varjs+1
    os.rename(filename,f"JS/{Varjs}.js")
def convertTxt(filename):
    if not 'TXT' in os.listdir():
     os.mkdir('TXT')
    global Vartxt
    Vartxt=Vartxt+1
    os.rename(filename,f"TXT/{Varjpeg}.txt")

def checkFun(filename,ext):
   
   if(ext=='mp3'):
       convertMp3(filename)
   elif(ext=='jpg'):
       convertJpg(filename)
   elif(ext=='jpeg'):
       convertJpeg(filename)
   elif(ext=='pdf'):
       convertPdf(filename)
   elif(ext=='txt'):
        convertTxt(filename)
   elif(ext=='js'):
       convertJs(filename)
  
    

totalFiles=os.listdir()
for file in totalFiles:
    try:
       ext=file.split('.')[1]
       checkFun(file,ext)
    except:
       print(f"{file} Directory is Created..")

