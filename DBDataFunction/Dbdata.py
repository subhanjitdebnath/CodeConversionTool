from datetime import datetime
import xlsxwriter as xl
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

class Dbdata():

# Contents:1.AnalysisTool 2.AlarmList 3.RemoveSpecialCharacter 4. Complete IO List 5. Event Treat Analysis



    def __init__(self):
        pass

#1.Analysis Tool
##-----------------START OF ANALYSIS METHOD------------------------##

    def Analysis(self,Filepath,SavingPath):

        '''Analysis(self,Filepath,Savingpath)..
        This module will take the DB file and do analysis for the same.
        While using this function please pass only BAX files '''

        SpecialCharter=''
        DBelemntstr=''
        Filename=''
        AnalysedContent=''' '''
        DIcount=0
        DOcount=0
        AIcount=0
        AOcount=0
        TotalS100IO=0
        DXcount=0
        AXcount=0
        TotalS400IO=0
        DI8count=0
        DO8count=0
        AI8count=0
        AO8count=0
        TotalS800IO=0
        MMCXcount=0
        SEQcount=0
        PIDCONcount=0
        TTDVARcount=0
        TEXTcount=0
        DBdictionary={}
        IOlist=[]
        StartDb=False
        SplTotal=0
        NameswithSpl=''

        pos=Filepath.find('\\')
        npos=pos+1
        Filename=Filename+Filepath[npos:]

        myfile=open(Filepath,'r')
        for _ in myfile:
            line1=_.strip()
            if 'END GENERAL DEFAULTS' in line1:
                StartDb=True

            elif StartDb and not(':' in line1) and not(len(line1)==0):
                if 'D'==line1[0] and 'I'==line1[1] and line1[2] in '123456789' and '.' in line1 and not('DI800' in line1):
                    DIcount=DIcount+1
                    DBdictionary['DI']=DIcount
                elif 'D'==line1[0] and 'O'==line1[1] and line1[2] in '123456789' and '.' in line1 and not('DO800' in line1):
                    DOcount=DOcount+1
                    DBdictionary['DO']=DOcount
                elif 'A'==line1[0] and 'I'==line1[1] and line1[2] in '123456789' and '.' in line1 and not('AI800' in line1):
                    AIcount=AIcount+1
                    DBdictionary['AI']=AIcount
                elif 'A'==line1[0] and 'O'==line1[1] and line1[2] in '123456789' and '.' in line1 and not('AO800' in line1):
                    AOcount=AOcount+1
                    DBdictionary['AO']=AOcount
                elif 'D'==line1[0] and 'X'==line1[1] and line1[2] in '123456789' and '.' in line1:
                    DXcount=DXcount+1
                    DBdictionary['DX']=DXcount
                elif 'A'==line1[0] and 'X'==line1[1] and line1[2] in '123456789' and '.' in line1:
                    AXcount=AXcount+1
                    DBdictionary['AX']=AXcount
                elif 'D'==line1[0] and 'I'==line1[1] and '8'==line1[2] and'0'==line1[3] and '0'==line1[4] and '.' in line1:
                    DI8count=DI8count+1
                    DBdictionary['DI8']=DI8count
                elif 'D'==line1[0] and 'O'==line1[1] and '8'==line1[2] and'0'==line1[3] and '0'==line1[4] and '.' in line1:
                    DO8count=DO8count+1
                    DBdictionary['DO8']=DO8count
                elif 'A'==line1[0] and 'I'==line1[1] and '8'==line1[2] and'0'==line1[3] and '0'==line1[4] and '.' in line1:
                    AI8count=AI8count+1
                    DBdictionary['AI8']=AI8count
                elif 'A'==line1[0] and 'O'==line1[1] and '8'==line1[2] and'0'==line1[3] and '0'==line1[4] and '.' in line1:
                    AO8count=AO8count+1
                    DBdictionary['AO8']=AO8count
                elif 'M'==line1[0] and 'M'==line1[1] and 'C'==line1[2] and'X'==line1[3]:
                    MMCXcount=MMCXcount+1
                    DBdictionary['MMCX']=MMCXcount
                elif 'S'==line1[0] and 'E'==line1[1] and 'Q'==line1[2]:
                    SEQcount=SEQcount+1
                    DBdictionary['SEQ']=SEQcount
                elif 'PIDCON' in line1:
                    PIDCONcount=PIDCONcount+1
                    DBdictionary['PIDCON']=PIDCONcount
                elif 'TTDVAR' in line1:
                    TTDVARcount=TTDVARcount+1
                    DBdictionary['TTDVAR']=TTDVARcount
                elif 'TEXT(20)' in line1:
                    TEXTcount=TEXTcount+1
                    DBdictionary['TEXT(20)']=TEXTcount
                else:
                    pass
            elif StartDb and not(len(line1)==0):
                if ':NAME' in line1:
                    for _ in line1:
                        a=_.lower()
                        if not(a in SpecialCharter) and not(a in 'qwertyuiopasdfghjklzxcvbnm1234567890_:'):
                            SpecialCharter=SpecialCharter+_+' '
                            SplTotal=SplTotal+1
                            NameswithSpl =NameswithSpl+ line1+'\n'
            elif 'END DB' in line1:
                StartDb=False
            else:
                pass
        myfile.close()
        for k,v in DBdictionary.items():
            DBelemntstr= DBelemntstr +'        ' + 'ELEMENT TYPE : ' + k + '   ---- QTY : '+ str(v) + '\n'

            if 'AI' == k or 'AO'==k or 'DI'==k or 'DO'==k:
                TotalS100IO = TotalS100IO + v
            elif 'AI8' == k or 'AO8'==k or 'DI8'==k or 'DO8'==k:
                TotalS800IO = TotalS800IO + v
            elif 'AX' == k or  'DX'==k:
                TotalS400IO = TotalS400IO + v
        TotalIOCount= 'Total S100 IO = ' + str(TotalS100IO) + '\n' +'        ' + 'Total S800 IO = ' + str(TotalS800IO) + '\n' +'        ' + 'Total S400 IO = ' + str(TotalS400IO)

        AnalysedContent= ''' ******* This is file generated by preconversion tool on  {}  From File : {} ***************
        
        Special Charaters Present In Name= ({}) . *If blank means no special character. _ is not special character.*
        
        Total names with special characters ={}
        {}
        Physical Elements Details:

{}

        ------------------------------------
        {}
        '''.format(date_time,Filename,SpecialCharter,SplTotal,NameswithSpl,DBelemntstr,TotalIOCount)
        newfilename = SavingPath + '/Analysis_'+Filename+'.txt'
        myfile = open(newfilename,'w')
        myfile.write(AnalysedContent)
        myfile.close()
        IOlist.append(TotalS100IO)
        IOlist.append(TotalS800IO)
        IOlist.append(TotalS400IO)
        IOlist.append(TotalS100IO+TotalS800IO+TotalS400IO)
        return IOlist

    
   ##-------------------END OF ANALYSIS METHOD ----------------------## 




#2.AlarmList
   ##-------------------START OF ALARM MODULE-----------------------##

    def Alarmlist(self,FilePath,SavingPath):

        '''Alarmlist(self,Filepath,Savingpath)..
        This module will take the DB file and do find Alarm list for the same.
        While using this function please pass only BAX files '''

        StartDb=False
        AlarmRow=['NIL','NIL','NIL']
        row=1
        col=0
        Filename=''
        pos=FilePath.find('\\')
        npos=pos+1
        Filename=Filename+FilePath[npos:]

        xlfilename=SavingPath + '/Alarmlist_'+Filename+'.xlsx'
        wb=xl.Workbook(xlfilename)
        sh1=wb.add_worksheet('Alarms')
        sh1.write(0,0,'IOAddress')
        sh1.write(0,1,'NAME')
        sh1.write(0,2,'DESCRIPTION')
        Alarmlist=''' 
        IoAddress     NAME        Description                       
'''

        myfile=open(FilePath,'r')
        for _ in myfile:
            line1=_.strip()
            if 'END GENERAL DEFAULTS' in line1:
                StartDb=True
            elif StartDb and not(len(line1)==0):
                if 'DI'in line1 and '.'in line1 and not(':' in line1):
                        dummy6=line1.split()
                        AlarmRow[0]=dummy6[0]
                elif 'AIC' in line1 and not(':' in line1):
                        dummy6=line1.split()
                        AlarmRow[0]=dummy6[0]   
                elif 'DIC' in line1 and not(':' in line1):
                        dummy6=line1.split()
                        AlarmRow[0]=dummy6[0]
                elif ':NAME' in line1:
                        dummy7=line1.split()
                        AlarmRow[1]=dummy7[1]
                elif ':DESCR' in line1:
                        dummy8=line1.split()
                        AlarmRow[2]=dummy8[1]
                elif ':NORM_TR' in line1 and '1' in line1:
                        Alarmlist=Alarmlist+'\n'+AlarmRow[0]+' \t'+AlarmRow[1]+'\t'+'||'+' \t\t'+AlarmRow[2]
                        col=0
                        sh1.write(row,col,AlarmRow[0])
                        col=col+1
                        sh1.write(row,col,AlarmRow[1])
                        col=col+1
                        sh1.write(row,col,AlarmRow[2])
                        row=row+1
                elif 'END DB' in line1:
                    StartDb=False
                else :
                    pass
            else:
                pass
        myfile.close()
        wb.close()
        Content=''' ******* This is file generated by preconversion tool on  {}  From File : {} ***************

        '''.format(date_time,Filename)
        Content=Content+Alarmlist

        newfilename = SavingPath + '/Alarmlist_'+Filename+'.txt'
        myfile = open(newfilename,'w')
        myfile.write(Content)
        myfile.close()


##-------------------END OF ALARM LIST METHOD-----------------------------##




#3.RemoveSpecialCharacter

##-------------------START OF SPECIAL CHARACTER REMOVAL METHOD---------------------##

    def Remove_Spl_Char(self,FilePath,SpecialList):
        ''' Remove_Spl_Char(self,FilePath,SpecialList)
        Filepath =[...Str...]
        SpecialList=[..List..]
        This module removes the special characters from the BAXfiles.'''
        StartDB=False
 
        myfile=open(FilePath,'r')
        for _ in myfile:
            line1=_.strip()
            if 'END GENERAL DEFAULTS' in line1:
                StartDB=True
            elif StartDB:
                if ':NAME' in line1:
                        for _ in SpecialList:
                            newline=line1.replace(_,'_')
                            line1=newline
                else:
                    pass
            content=content+line1+"\n"

        myfile.close()
        myfile=open(FilePath,'w')
        myfile.write(content)
        myfile.close()


##--------------------END OF SPECIAL CHARACTER REMOVAL METHOD---------------------##

#4.COMPLETE IO LIST 

##------------------------START OF COMPLETE IO LIST METHOD------------------------##

    def CompleteIoList(self,Filepath,SavingPath):
        ''' CompleteIoList(self,Filepath,SavingPath)
        Filepath=[---Str---]
        SavingPath=[---Str---]
        This module will give you complete IO list '''
        StartDb=False
        IOListRow=['','','']
        row=1
        col=0
        Filename=''
        pos=Filepath.find('\\')
        npos=pos+1
        Filename=Filename+Filepath[npos:]
        IOlist='''IOADDRESS       NAME          DESCRIPTION
        '''

        
        xlfilename=SavingPath + '/IOLIST_'+Filename+'.xlsx'
        wb=xl.Workbook(xlfilename)
        sh1=wb.add_worksheet('IOList')

        sh1.write(0,0,'IOAddress')
        sh1.write(0,1,'NAME')
        sh1.write(0,2,'DESCRIPTION')

        myfile=open(Filepath,'r')
        for _ in myfile:
            line1=_.strip()
            if 'END GENERAL DEFAULTS' in line1:
                StartDb=True
            elif StartDb :
                if 'DI'in line1 and '.'in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0]
                elif 'DO' in line1 and '.' in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0]    
                elif 'AI' in line1 and '.' in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0]   
                elif 'AO' in line1 and '.' in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0]   
                elif 'DX' in line1 and '.' in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0] 
                elif 'AX' in line1 and '.' in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0]
                   
                elif 'DI8' in line1 and '.' in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0]
                   
                elif 'DO8' in line1 and '.' in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0]
                   
                elif 'AI8' in line1 and '.' in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0]
                    
                elif 'AO8' in line1 and '.' in line1 and not(':' in line1)and not(len(line1)==0):
                    dummy=line1.split()
                    IOListRow[0]=dummy[0]
                
                elif ':NAME' in line1 and not(len(line1)==0):
                    dummy1=line1.split()
                    try:
                        IOListRow[1]=dummy1[1]
                    except:
                        pass

                elif ':DESCR' in line1 and not(len(line1)==0):
                    dummy2=line1.split()
                    try:
                        IOListRow[2]=dummy2[1]
                    except:
                        pass

                elif (len(line1)==0) and not(IOListRow[0]==''):
                    IOlist=IOlist + '\n' +IOListRow[0] + '{:^20}'.format('')+IOListRow[1]+ '\t''\t' + IOListRow[2]
                    col=0
                    sh1.write(row,col,IOListRow[0])
                    col=col+1
                    sh1.write(row,col,IOListRow[1])
                    col=col+1
                    sh1.write(row,col,IOListRow[2])
                    IOListRow[0]=''
                    IOListRow[1]=''
                    IOListRow[2]=''
                    row=row+1


                else:
                    pass

            elif 'END DB' in line1:
                StartDb=False

            else:
                pass
        myfile.close()

        wb.close()
        Content=''' ******* This is file generated by preconversion tool on  {}  From File : {} ***************

        '''.format(date_time,Filename)
        Content=Content+IOlist

        newfilename = SavingPath + '/IOLIST_'+Filename+'.txt'
        myfile = open(newfilename,'w')
        myfile.write(Content)
        myfile.close()

##-----------------------END OF COMPLETE IO LIST METHOD--------------------------##
                    
##-----------------------Event Treat Analysis---------------------------------##




