import sys
import yaml
import tkinter as tk
import tkinter.messagebox as m
import tkinter.filedialog as f
from tkinter.ttk import *
import os
import urllib.request
import json
import time
filepath = None

main=None
text=None
label=None
datall=None


main =tk.Tk()
main.title = 'B.bingTranslater'
main.geometry('480x270')
c=tk.StringVar()
c.set('0/0')
text = tk.StringVar()
text.set('파일 없음')
clientid = tk.StringVar()
clientid.set('client id')
clientsecret =tk.StringVar()
clientsecret.set ( 'client secret')
label = tk.ttk.Label(main , textvariable = text ,state = 'active')
label.pack()

label = tk.ttk.Label(main , text= 'clientid' ,state = 'active')
label.pack()

textbox1= tk.ttk.Entry(main,textvariable=clientid ,name = 'clientid' , width ='50')
textbox1.pack()

label = tk.ttk.Label(main , text = 'clientsecret' ,state = 'active')
label.pack()

textbox2= tk.ttk.Entry(main,textvariable=clientsecret ,name = 'clientsecret', width = '50')
textbox2.pack()




progressbar = tk.ttk.Label(main, textvariable=c )
progressbar.pack()
def selectbtn() :
    global filepath
    filepath = f.askopenfile(initialdir =os.getcwd(), title ='번역할 yaml', filetypes =(( 'YAML files','*.yaml') ,( 'YAML files','*.yml'))).name
    
    text.set(filepath) 
def process(request ,dataaa ,key) :
    global datall

    rescode =None
    response =urllib.request.urlopen(request,data=dataaa.encode('utf-8'))
    rescode = response.getcode()
    if rescode==None:
        time.sleep(1)
        rescode=response.getcode()
    if rescode == 200 : 
        resbody = response.read()
        resbody = json.loads(resbody.decode('utf-8'))
        datall[key] =resbody['message']['result']['translatedText']
        return True
    else :
        return False
def startbtn():
    

    global clientid 
    global clientsecret
    global clientid
    global filepath
    global progress
    global textbox1
    global textbox2
    global c
    global datall
    clientid = str(textbox1.get())
    clientsecret = str(textbox2.get())
    if not all([clientid, clientsecret, filepath]):
        m.showerror('Error', '모든 필드를 채워주세요.')
        return
    #process
    with open(filepath,encoding='utf-8') as f :
        datas = yaml.safe_load(f)
        datall = datas
        w= 0 
        for a in datas:
            dbdb = str(datas[a])
            url = 'https://naveropenapi.apigw.ntruss.com/nmt/v1/translation'
            dataaa = "source=en&target=ko&text="+ dbdb
            
            request =urllib.request.Request(url)
            request.add_header ( 'X-NCP-APIGW-API-KEY-ID',clientid)
            request.add_header('X-NCP-APIGW-API-KEY',clientsecret)
            
            
            
            if process(request=request,dataaa =dataaa ,key=a ):
                    
                w = w+1
                c.set(str(w))
                    
            else :
                m.ERROR('오류 ')
            
                
                        
    with open(f"{os.getcwd()}/result.yml" ,'w' ) as f :
        yaml.dump(datall,f, allow_unicode=True)
    
    m.showinfo('Success', f'완료 되었습니다. 파일 저장 경로는 {os.getcwd()}입니다.')
def endbtn():
    main.destroy()
    sys.exit()
selectbtn = tk.ttk.Button(main, text = '파일 선택' ,command = selectbtn )
selectbtn.pack()

startbtn = tk.ttk.Button(main ,text ='번역 실행',command= startbtn)
startbtn.pack();

endbtn = tk.ttk.Button(main, text = '종료' ,command =endbtn)
endbtn.pack();
main.mainloop();
                    