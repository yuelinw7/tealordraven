import csv
import re

for i in range(1,100):
    with open ('./log/logfile'+str(i),'r',encoding='gb18030', errors='ignore') as f:
        content=f.read()
        ip=re.findall(r'\|(.*)\|',content)
        tp=re.findall(r'\((.+?/s)',content)    
        # print(ip,tp)

    if ip!=[]:
        if ip[0]!='' and tp[0] != '':
            a = ip[0][:]
            b = tp[0][:]
            string=a+','+b
            print(string)
            with open ('data.csv','a+') as f:
                f.write(string+'\n')
   