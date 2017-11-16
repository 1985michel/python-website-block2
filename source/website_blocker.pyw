import time
from datetime import datetime as dt

host_temp =r"C:\Users\michel\git\SiteBlock\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"

host = hosts_path

redirect="127.0.0.1"

website_list=["www.facebook.com","facebook.com"]
website_list.append("www.youtube.com")
website_list.append("www.youtube.com.br")
website_list.append("www.ahnegao.com.br")
website_list.append("youtube.com")
website_list.append("web.whatsapp.com")


#value = 8 <= dt.now().hour < 18



while True:
    if 8 <= dt.now().hour <= 19 or dt.now().hour >= 22:#17
        print("Back to work")
        with open(host,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun time!")
        with open(host,"r+") as file:
            content = file.readlines()
            file.seek(0) #retornando o ponteiro para o inicio do documento
            for line in content:
                #se nao houver nenhum site da lista na linha, escreva a linha
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate() #apaga tudo para baixo no documento
                
               
    time.sleep(30) #faz o programa esperar 5 segundos
    
"""
 how to configure the Schedule Task on windows

i) In "Program/script", browse the file path of pythonw.exe (e.g. C:\Users\Me\Desktop\pythonw.exe)

ii) In "Add arguments (optional)", put in the file name of your script (e.g. website_blocker.pyw)

iii) In "Start in (optional)", put in the file path of the folder that contains your script (e.g. C:\Users\Me\Desktop\Folder)

I got the solution from here: https://stackoverflow.com/questions/44727232/scheduling-a-py-file-on-task-scheduler-in-windows-10

"""

