#-----importing different libaries------#
import tkinter as tk
import tkinter.scrolledtext as scrol
from tkinter import  Canvas, Frame
import tkinter.ttk as ttk
import tkinter.filedialog as fl
from tkinter import messagebox

import os
from os import path

import IPython.display as display

#----------Importing DB and PC libaries------------------#

from DBDataFunction import Dbdata
from PCDataFunction import Pcdata

#-----------Defining The Global Variable----------------#

AAXfiles=[]
BAXfiles=[]
files=[]
Savingpath=['']
BAXnames=[]
AAXnames=[]
IconPath=''
ListIO=[]
#-----------------------Getting The Icon Path-----------------------#

IconPath=path.realpath('Codeanalysis.ico')

#--------------Function For Getting the File Location---------#

def Getfileloacation():
    global AAXfiles
    global BAXfiles
    global AAXnames
    global BAXnames

    AAXfiles=[]
    BAXfiles=[]

    aaxfilename=''
    baxfilename=''
    filelocation = fl.askdirectory()
    for r, d1, f in os.walk(filelocation):
        for _ in f:
            extension=_[-4:]
            if extension =='.AAX':
                AAXfiles.append(os.path.join(r, _))
            elif extension =='.BAX':
                BAXfiles.append(os.path.join(r, _))
            else : pass
    for _ in BAXfiles:
        pos=_.find('\\')
        pos1=pos+1
        BAXnames.append(_[pos1])
        baxfilename=baxfilename+_[pos1:]+'\n'
    
    Dblistbox.delete('1.0',tk.END)
    Dblistbox.insert(tk.END,baxfilename)

    TotalDbFiles.delete('1.0',tk.END)
    TotalDbFiles.insert(tk.END,str(len(BAXfiles)))

    for _ in AAXfiles:
        pos=_.find('\\')
        pos1=pos+1
        AAXnames.append(_[pos1])
        aaxfilename=aaxfilename+_[pos1:]+'\n'
    Pclistbox.delete('1.0',tk.END)
    Pclistbox.insert(tk.END,aaxfilename)

    TotalPcFiles.delete('1.0',tk.END)
    TotalPcFiles.insert(tk.END,str(len(AAXfiles)))

    AnalyseDB.configure(bg='red2')
    AnalysePC.configure(bg='red2')
    Alarm.configure(bg='red2')
    IOList.configure(bg='red2')
    comment.configure(bg='red2')
    FileLocbt.configure(text='Browse File Location',bg='Gold')

#--------------Function For Getting the File Location ENDS---------#

#--------------Function For Getting the File SAVING Location---------#

def FilesavingLocation():
    global Savingpath
    filelocation = fl.askdirectory()
    Savingpath[0]=filelocation

    Savelocation.delete('1.0',tk.END)
    Savelocation.insert(tk.END,filelocation)

    AnalyseDB.configure(bg='red2')
    AnalysePC.configure(bg='red2')
    Alarm.configure(bg='red2')
    IOList.configure(bg='red2')
    comment.configure(bg='red2')
    


#----------APPLICATION WINDOW CREATION---------------#

window=tk.Tk()
window.geometry('700x700')
window.title('AdvantAnalysisAndPreconversionTool-------By Subhanjit')
Heading=tk.Label(window,text='ADVANT-ANALYSIS-PRECONVERSION-TOOL',fg='Red',compound=tk.CENTER,font=('ARIAL BOLD',15))
Heading.pack()
#------- All Lables ---------#

Dblist=tk.Label(window,text='DB File List (.BAX)',font=('Arial',10))
Dblist.place(x=490,y=36)

Pclist=tk.Label(window,text='PC File List (.AAX)',font=('Arial',10))
Pclist.place(x=270,y=36)

label1=tk.Label(window,text="(--Keep all the AAX and \n BAX file in one folder--)",font=('Arial',10))
label1.place(x=22,y=110)

label2=tk.Label(window,text="(----All the Analysed File , Alarm List , Comment List and other Files will be Saved in this Location----)",font=('Arial',10))
label2.place(x=22,y=235)

label3=tk.Label(window,text='ANALYSIS',font=('Arial Bold',15),fg='Black',width=15)
label3.place(x=3,y=272)

label4=tk.Label(window,text='PRECONVERSION',font=('Arial Bold',15),fg='Black',width=15)
label4.place(x=20,y=530)

label5=tk.Label(window,text='Enter the Special charaters without space ..(@#$..)',font=('Arial',10))
label5.place(x=10,y=560)

label6=tk.Label(window,text='Project Name *',font=('Arial',10))
label6.place(x=400,y=328)

label7=tk.Label(window,text='Project Id *',font=('Arial',10))
label7.place(x=400,y=388)

label8=tk.Label(window,text='Your Email Id *',font=('Arial',10))
label8.place(x=400,y=448)

label9=tk.Label(window,text='LOAD TO SERVER',font=('Arial Bold',15),fg='Black',width=15)
label9.place(x=410,y=272)


#---------All Lables END-------#

Dblistbox=scrol.ScrolledText(window,height=5,width=22,borderwidth=2,relief="solid",bg='Light gray')
Dblistbox.place(x=480,y=60)

TotalDbFiles=tk.Text(window,height=1,width=4,bg='azure')
TotalDbFiles.place(x=615,y=36)

TotalPcFiles=tk.Text(window,height=1,width=4,bg='azure')
TotalPcFiles.place(x=395,y=36)

Pclistbox=scrol.ScrolledText(window,height=5,width=22,borderwidth=2,relief="solid",bg='Light gray')
Pclistbox.place(x=260,y=60)

FileLocbt=tk.Button(window,text=' Browse File Location ',font=('Arial',12),bg='Gold',command=Getfileloacation)
FileLocbt.place(x=20,y=60)

SaveLocbt=tk.Button(window,text=' Browse Saving Location ',font=('Arial',12),bg='Gold',command=FilesavingLocation)
SaveLocbt.place(x=20,y=160)

Savelocation=tk.Text(window,height=2,width=84,bg='Light Blue')
Savelocation.place(x=10,y=200)



#-------ANALYSIS---------#
##**This part will do the analysis of the AAX and BAX files**##

       #*BAX Analysis.... Calling the Analysis function and analysing BAX file

def BaxAnalysisFun():
    global BAXfiles
    global BAXnames
    global Savingpath
    global ListIO


    if not(len(BAXfiles)==0):

        DBanlyse=Dbdata.Dbdata()

        for _ in BAXfiles:
            ListIO=ListIO+DBanlyse.Analysis(_,Savingpath[0])
        messagebox.showinfo('STATUS','DONE')
        Iograph()

        AnalyseDB.configure(bg='Green')
    else:
        messagebox.showinfo('STATUS','NO BAX')
    

AnalyseDB=tk.Button(window,text='ANALYSE DB',font=('Arial Bold',10),bg='red2',fg='snow',width=15,relief='groove',command=BaxAnalysisFun)
AnalyseDB.place(x=30,y=310)
##--------------------------------------------------------------------------------------------------##



##------------------------------COMBINED DB ANALYSIS----------------------------------------------------##
#This will combined the DB data to give a combined analysis#

def CombineDBdata():

    global BAXfiles
    global Savingpath
    global BAXnames

    summerypath=''
    content1=''

    summerypath = summerypath + Savingpath[0] + '/DbCombine.BAX'

    if not(len(BAXfiles)==0) and not(len(Savingpath[0])==0) and not('DbCombine' in BAXnames):
        for _ in BAXfiles:
            myfile=open(_,'r')
            for a in myfile:
                line1=a.strip()
                content1=content1+line1+'\n'
            myfile.close()
        newfile=open(summerypath,'w')
        newfile.write(content1)
        newfile.close()
        FileLocbt.configure(text='RE-Browse File Location',bg='orange')
        messagebox.showinfo('STATUS','DONE')
    
    elif ('DbCombine' in BAXnames):
        messagebox.showerror('FILE','Already \n Generated')

    elif Savingpath[0]=='':
        messagebox.showerror('PATH','NO SAVING \n LOCATION')

    else:
        messagebox.showerror('FILE','NO BAX')

DbCombine=tk.Button(window,text='COMBINE DB',font=('Arial Bold',10),bg='red2',fg='snow',width=15,relief='groove',command=CombineDBdata)
DbCombine.place(x=510,y=150)

##---------------------------------------------------------------------------------------------------------##


        #*AAX Analysis..... Calling the AAx Analysis Function and Analysing AAX file
def AaxAnalysisFun():
    global AAXfiles
    global AAXnames
    global Savingpath

    if not(len(AAXfiles)==0):

        PCanlyse=Pcdata.Pcdata()

        for _ in AAXfiles:
            PCanlyse.Analysis(_,Savingpath[0])
        messagebox.showinfo('STATUS','DONE')

        AnalysePC.configure(bg='Green')
    else:
        messagebox.showinfo('STATUS','NO AAX')

AnalysePC=tk.Button(window,text='ANALYSE PC',font=('Arial Bold',10),bg='red2',fg='snow',width=15,relief='groove',command=AaxAnalysisFun)
AnalysePC.place(x=30,y=345)
##--------------------------------------------------------------------------------------------------##

      #*AlarmList..... Calling the BAX Alarm List Function the Alarm Lists will be generated.......
def Alarmlist():
    global BAXfiles
    global BAXnames
    global Savingpath

    if not(len(BAXfiles)==0):

        DBanlyse=Dbdata.Dbdata()

        for _ in BAXfiles:
            DBanlyse.Alarmlist(_,Savingpath[0])
        messagebox.showinfo('STATUS','DONE')
        Alarm.configure(bg='Green')
    else:
        messagebox.showinfo('STATUS','NO BAX')

Alarm=tk.Button(window,text='ALARM LIST',font=('Arial Bold',10),bg='red2',fg='snow',width=15,relief='groove',command=Alarmlist)
Alarm.place(x=30,y=380)

##--------------------------------------------------------------------------------------------------##

      #*IOList..... Calling the BAX IO List Function the IO Lists will be generated....... 
def IOlistComplete():
    global BAXfiles
    global Savingpath
    global BAXnames

    if not(len(BAXfiles)==0):

        DBanlyse=Dbdata.Dbdata()

        for _ in BAXfiles:
            DBanlyse.CompleteIoList(_,Savingpath[0])
        messagebox.showinfo('STATUS','DONE')
        IOList.configure(bg='Green')
    else:
        messagebox.showinfo('STATUS','NO BAX')

IOList=tk.Button(window,text='IO LIST',font=('Arial Bold',10),bg='red2',fg='snow',width=15,relief='groove',command=IOlistComplete)
IOList.place(x=30,y=415)

##-------------------------------------------------------------------------------------------------------##

       #*CommentList.....Calling the AAX Comment List Function and Comments will be generated.........
def CommentFun():
    global AAXfiles
    global AAXnames
    global Savingpath

    if not(len(AAXfiles)==0):

        PCanlyse=Pcdata.Pcdata()

        for _ in AAXfiles:
            PCanlyse.Comments(_,Savingpath[0])
        messagebox.showinfo('STATUS','DONE')
        comment.configure(bg='Green')
    else:
        messagebox.showinfo('STATUS','NO AAX')

comment=tk.Button(window,text='COMMENT LIST',font=('Arial Bold',10),bg='red2',fg='snow',width=15,relief='groove',command=CommentFun)
comment.place(x=30,y=450)

def Seqdetails():
    global AAXfiles
    global AAXnames
    global Savingpath

    if not (len(AAXfiles) == 0):

        PCanlyse = Pcdata.Pcdata()

        for _ in AAXfiles:
            PCanlyse.SeqDetails(_, Savingpath[0])
        messagebox.showinfo('STATUS', 'DONE')
        SeqDetl.configure(bg='Green')
    else:
        messagebox.showinfo('STATUS', 'NO AAX')

SeqDetl=tk.Button(window,text='SEQ DETAILS',font=('Arial Bold',10),bg='red2',fg='snow',width=15,relief='groove',command=Seqdetails)
SeqDetl.place(x=30,y=485)

##---------------------------------------------------------------------------------------------------------##

def SearchCustom():
    global AAXfiles
    global AAXnames
    global Savingpath

    if not (len(AAXfiles) == 0):

        PCanlyse = Pcdata.Pcdata()

        for _ in AAXfiles:
            PCanlyse.Search(_, Savingpath[0])
        messagebox.showinfo('STATUS', 'DONE')
        Search.configure(bg='Green')
    else:
        messagebox.showinfo('STATUS', 'NO AAX')

Search=tk.Button(window,text='SEARCH',font=('Arial Bold',10),bg='red2',fg='snow',width=15,relief='groove',command=SearchCustom)
Search.place(x=450,y=550)
        #*Combined PC analyis ------ This will combine all the PCfile and will give one complete analysis......
def Combinedpcanalysis():

    global AAXfiles
    global Savingpath
    global AAXnames

    summerypath=''
    content1=''

    summerypath = summerypath + Savingpath[0] + '/PcCombine.AAX'

    if not(len(AAXfiles)==0) and not(Savingpath[0]=='') and not('PcCombine.AAX' in AAXnames):

        for _ in AAXfiles:
           myfile=open(_,'r')
           for a in myfile:
               line1=a.strip()
               content1=content1+line1+'\n'
           myfile.close()
        
        newfile=open(summerypath,'w')
        newfile.write(content1)
        newfile.close()
        FileLocbt.configure(text='RE-Browse File Location',bg='orange')
        messagebox.showinfo('STATUS','DONE')

    elif ('PcCombine.AAX' in AAXnames):
        messagebox.showerror('FILE','Already \n Generated')

    elif Savingpath[0]=='':
        messagebox.showerror('PATH','NO SAVING \n LOCATION')

    else:
        messagebox.showerror('FILE','NO AAX')

PCCombine=tk.Button(window,text='COMBINE PC',font=('Arial Bold',10),bg='red2',fg='snow',width=15,relief='groove',command=Combinedpcanalysis)
PCCombine.place(x=280,y=150)


#-----------ADVANCE ANALYSIS---------------#


n=tk.StringVar()

advanceAnly=ttk.Combobox(window,width=20,textvariable=n)
advanceAnly['value']=('-Select-','IO-Overview','IOType-Overview')
advanceAnly.current(1)
advanceAnly.place(x=190,y=465)

Graph=Canvas(window,width=160,height=160,bg='LightBlue')
Graph.place(x=183,y=300)


def prop(max,n):
    return 360*n/max 

def Iograph():
    global ListIO
    if(ListIO[3]!=0):
        bar1=ttk.Progressbar(Graph,orient=tk.VERTICAL,length=135)
        bar1.place(x=5,y=5)
        bar1['value']=(ListIO[0]/ListIO[3])*100
        bar2=ttk.Progressbar(Graph,orient=tk.VERTICAL,length=135)
        bar2.place(x=35,y=5)
        bar2['value']=(ListIO[1]/ListIO[3])*100
        bar3=ttk.Progressbar(Graph,orient=tk.VERTICAL,length=135)
        bar3.place(x=65,y=5)
        bar3['value']=(ListIO[2]/ListIO[3])*100
        barlable1=ttk.Label(Graph,text='S100',background='LightBlue')
        barlable1.place(x=3,y=140)
        barlable2=ttk.Label(Graph,text='S800',background='LightBlue')
        barlable2.place(x=35,y=140)
        barlable3=ttk.Label(Graph,text='S400',background='LightBlue')
        barlable3.place(x=65,y=140)
        
    else:
        pass

def Iotypegrapg():
    Graph.create_arc((10,10,150,150), fill="RED", outline="RED", start=prop(100,0), extent = prop(100,20))
    Graph.create_arc((10,10,150,150), fill="Yellow", outline="YELLOW", start=prop(100,20), extent = prop(100,30))
    Graph.create_arc((10,10,150,150), fill="GREEN", outline="GREEN", start=prop(100,50), extent = prop(100,25))
    Graph.create_arc((10,10,150,150), fill="Blue", outline="BLUE", start=prop(100,75), extent = prop(100,25))

def DisplayGraph():
    
    if (advanceAnly.get()=='IO-Overview'):
        Iograph()
    elif (advanceAnly.get()=='IOType-Overview'):
        Iotypegrapg()
    else:
       pass


DisGraph=tk.Button(window,text='DISPLAY',font=('Arial Bold',10),bg='Blue',fg='snow',width=15,relief='groove',command=DisplayGraph)
DisGraph.place(x=190,y=490)



#--------PRECONVERSION---------#

chartername=tk.StringVar()

charlist = tk.Entry(window,width=40,textvariable=chartername)
charlist.place(x=20,y=580)


def PcSplchar():
    global AAXfiles
    Splstr=charlist.get()

    Splremove=Pcdata.Pcdata()

    if not(len(AAXfiles)==0) and not(len(Splstr)==0):

        for _ in AAXfiles:
            Splremove.Remove_Spl_Char(_,Splstr)

        messagebox.showinfo('STATUS','DONE')

    elif len(AAXfiles)==0:
        messagebox.showinfo('STATUS','NO AAX')
    else:
        messagebox.showinfo('STATUS','No \n Characteres')

        
RemovePCSpl=tk.Button(window,text='MODIFY PC',font=('Arial Bold',10),bg='Dark Green',fg='White',width=15,command=PcSplchar)
RemovePCSpl.place(x=10,y=625)

##-------------------------------------REMOVE PC SPECIAL CHARACTERS---------------------------------------##

RemoveDBSpl=tk.Button(window,text='MODIFY DB',font=('Arial Bold',10),bg='Dark Green',fg='White',width=15)
RemoveDBSpl.place(x=150,y=625)
RemoveDBSpl.configure(state=tk.DISABLED)


#---------PROJECT DETAILS----------#

chartername2=tk.StringVar()
chartername3=tk.StringVar()
chartername4=tk.StringVar()

projname = tk.Entry(window,width=40,textvariable=chartername2)
projname.place(x=400,y=305)

projid = tk.Entry(window,width=40,textvariable=chartername3)
projid.place(x=400,y=365)

emailid = tk.Entry(window,width=40,textvariable=chartername4)
emailid.place(x=400,y=425)

Loadbt=tk.Button(window,text='TRANSFER',bg='Yellow',width=10)
Loadbt.place(x=460,y=480)
Loadbt.configure(state=tk.DISABLED)


#--------------PROJECTIONS---------------#

#--------------Advance Tools-------------#

Advancetool= ttk.Progressbar()



window.mainloop()
