'''
tkinter示範程式--text+scrollbar的應用
'''
import tkinter as tk
import requests
import json
import math
from PIL import Image, ImageTk
from io import BytesIO
import tkinter.messagebox 


def _newPage(thisPage):     #使用這個自訂函式來取得每一頁的資料
    
    movieUrl=urlOMDB+movieName+"&apikey="+myKey+"&page="+str(thisPage)
    datA=json.loads(requests.get(movieUrl).text)    #取得的資料轉換成JSON檔的格式
    '''
    with open(movieName+"(s).json","a",encoding="utf-8") as filE:
        json.dump(datA,filE,ensure_ascii=False,indent=4)
    '''
    return(datA)
#s
def _hit1():
    try:
        listBox.delete(0,tk.END)
        global urlOMDB,movieName,myKey
        
        urlOMDB="http://www.omdbapi.com/?s="    #參數改成[s]
        myKey="52e16be"
        
        moviE=enteR.get()
        movieName="+".join(moviE.split())
        #print(movieName)
        
        movieUrl=urlOMDB+movieName+"&apikey="+myKey
        dictFile=json.loads(requests.get(movieUrl).text)
        
        totaL=int(dictFile["totalResults"])     #取得相關電影的總數
        pageS=math.ceil(totaL/10)+1         #計算總頁數
        
        if dictFile:
            countS=0
            print("==============================================")
            for myPage in range(1,pageS):
                dataS=_newPage(myPage)
                for iteM in dataS["Search"]:
                    countS=countS+1
                    
                    print(str(countS)+"."+"---------------------------")
                    listBox.insert(tk.END, str(countS)+"."+"---------------------------"+'\n')
                    
                    print(iteM["Title"])
                    listBox.insert(tk.END, iteM["Title"]+'\n')
                    
                    print(iteM["Year"])
                    listBox.insert(tk.END, iteM["Year"]+'\n')
                    
                    print(iteM["imdbID"])
                    listBox.insert(tk.END, iteM["imdbID"]+'\n')
                    
                    print(iteM["Type"])
                    listBox.insert(tk.END, iteM["Type"]+'\n')
            print("==============================================")
            listBox.insert(tk.END, ('='*30)+'\n')
            
            print("相關電影總共有: "+str(totaL)+" 部")   
            listBox.insert(tk.END, "相關電影總共有: "+str(totaL)+" 部"+'\n')
            
        else:
            print("找不到相關電影資訊!!") 
            listBox.insert(tk.END, "找不到相關電影資訊!!")
    except:
        listBox.insert(tk.END, "NotFind")
#t
def _hit2():
    try:
        listBox.delete(0,tk.END)
        urlOMDB="http://www.omdbapi.com/?t="  #使用OMDB所提供的參數[t]
        myKey="1e70702f"     #請使用你自己的apikey
        
        moviE=enteR.get()
        movieName="+".join(moviE.split())   #將[super man]組合成[super+man]
        #print(movieName)
        
        movieUrl=urlOMDB+movieName+"&apikey="+myKey     #請求資料時得付上自己的apikey
        #print(movieUrl)
        
        dictFile=json.loads(requests.get(movieUrl).text)
        print(dictFile)
        
        for item in dictFile:
            if isinstance(dictFile.get(item), str):
                listBox.insert(tk.END, item+': '+dictFile.get(item)+'\n')
                listBox.insert(tk.END,'\n')
            else:
                listBox.insert(tk.END, item+'\n')
                for nuM in range(0,3):
                    for itemSInList in dictFile.get(item)[nuM]:
                        listBox.insert(tk.END, '\t'+itemSInList+': '+dictFile.get(item)[nuM].get(itemSInList)+'\n')
                        listBox.insert(tk.END,'\n')
        '''                
        with open(movieName+"(t).json","w",encoding="utf-8") as filE:
            json.dump(dictFile,filE,ensure_ascii=False,indent=4)
        '''
    except:
        listBox.insert(tk.END,'NotFind')
#t>poster
def _hit3():
    #listbox選取的值
    lisTloC=listBox.curselection()
    urLimG=listBox.get(lisTloC)
    if not urLimG is None:
        if 'Poster:' in urLimG:
            urLimG=urLimG.replace('Poster: ','')
            #開啟網路圖片
            webImg=requests.get(urLimG)
            img= Image.open(BytesIO(webImg.content))
            w, h= img.size
            if w>400:
                h= int(h*400/w)
                w=400
            if h>600:
                w= int(w*600/h)
                h=600
            img= img.resize((w,h))
            tk_img= ImageTk.PhotoImage(img)
        
            wiN1=tk.Toplevel(wiN)
            wiN1.title("Image!!!")
            wiN1.geometry("{}x{}+1100+20".format(400,600))
            wiN1.resizable(False, False)
            lbPic = tk.Label(wiN1, text='test', width=400, height=600)
            lbPic.pack()
            lbPic['image']= tk_img
            lbPic.image= tk_img
        else:
            tk.messagebox.showwarning("警告","請選 Poster:")
    

    

def _hit4():
    listBox.delete(0,tk.END)
    
def _hit5():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()


wiN = tk.Tk()
wiN.title("OMDB(ST)!!!")
wiN.geometry("1500x1000+10+0")
wiN.resizable(False, False)
wiN.configure(background='black')

enteR=tk.Entry(wiN,font=("Arial",16),bd=5)
enteR.pack() 

btN1 = tk.Button(wiN, text="搜尋電影(s)!!", fg="green", font=("Arial Black", 18), width=10, height=1, command=_hit1)
btN1.place(x=300,y=45) 

btN2 = tk.Button(wiN, text="搜尋電影(t)!!", fg="green", font=("Arial Black", 18), width=10, height=1, command=_hit2)
btN2.place(x=500,y=45)

btN3 = tk.Button(wiN, text="Poster!!",  fg="blue", font=("Arial Black", 18), width=10, height=1, command=_hit3)
btN3.place(x=700,y=45) 

btN4 = tk.Button(wiN, text="清除!!",  fg="orange", font=("Arial Black", 18), width=10, height=1, command=_hit4)
btN4.place(x=900,y=45)

btN5 = tk.Button(wiN, text="離開!!",  fg="red", font=("Arial Black", 18), width=10, height=1, command=_hit5)
btN5.place(x=1100,y=45) 

sBar=tk.Scrollbar(wiN)
sBar.pack(side=tk.RIGHT,fill=tk.Y)

list_str=tk.StringVar()
listBox=tk.Listbox(wiN, font=("Arial Black", 20), fg ="white", bg ="black", yscrollcommand=sBar.set,height=40,  listvariable=list_str,  selectmode=tk.EXTENDED)
#listBox.pack(side=tk.BOTTOM, fill=tk.BOTH)
listBox.place(x=0,y=110,width=1482,height=890)
sBar.config(command=listBox.yview)

wiN.mainloop()

