from ntpath import join
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
from time import sleep
import os 


   
gauth = GoogleAuth() 
gauth.LocalWebserverAuth()        
drive = GoogleDrive(gauth) 

# estrutura de hierarquia das pastas da innova empreendimentos
    # 2022
        #03 - MARÇO DE 2022
            # 20.03.22                



def SendFilesToDrive(folder):

    print(folder)
    destinos = {"op07": "15eNEqP3wxFgPLGWaz3Sx_fZnCieGxMkX", "op06":"1zw3WNkmxnUSFJyOqp3k_jrAKXLbU4XgW", "op05":"11Pljj-hGrZSnzY9eyCm-dzi4veIE6INg", "opab01": "1nxkAAF8Woy_L2GWZ6M1047K_B7gALYs8", "escr":"1zQTsIhILte1xXSd-nzsuqnzZLpuAq3f0", "clod":"1Phg2rwsjyvni8PCPeIRKaIbk1rLWcXCS", "na": "174Fbft_BNsS9q3eTQUIaVcToZvKdzbVF", "almox":"1FFsF2P0mo4qZErTE-hBRvip_dBeh3PK-", "op04":"1C14kV0wAxFGxX56R07Z3_yVv4XYASra6", "bn":"1DwgBFFsmbcQV7C7xqd3urio64gVJEcxG", "pg":"1IsKpuD1nZW5cYEmR894u_p4nkXf_Nrsf", "cabedelo":"1iBTxNZFoKmWec1LXm4-6Ni47VoJrlI32", "aqbet": "18FX1VrCnT_yrXYSQjS5eKaCBQpDhx3E0", "aqth": "14ygca4DJwJwhP8L4FoUceTOeRbTtnW7Y", "c&s": "1sm_o_hEwcHf3rYfs9aLbv4Hyqc9TQfzn"}
    meses = {"01": "01 - JANEIRO DE 2022","02":"02 - FEVEREIRO DE 2022","03": "03 - MARÇO DE 2022","04": "04 - ABRIL DE 2022","05":"05 - MAIO DE 2022","06": "06 - JUNHO DE 2022", "07": "07 - JULHO DE 2022", "08": "08 - AGOSTO DE 2022", "09": "09 - SETEMBRO DE 2022", "10": "10 - OUTUBRO DE 2022", "11":"11- NOVEMBRO DE 2022", "12":"12 - DEZEMBRO DE 2022"}
    meses2 = {"01": "01 - JANEIRO DE 2021","02":"02 - FEVEREIRO DE 2021","03": "03 - MARÇO DE 2021","04": "04 - ABRIL DE 2021","05":"05 - MAIO DE 2021","06": "06 - JUNHO DE 2021", "07": "07 - JULHO DE 2021", "08": "08 - AGOSTO DE 2021", "09": "09 - SETEMBRO DE 2021", "10": "10 - OUTUBRO DE 2021", "11":"11- NOVEMBRO DE 2021", "12":"12 - DEZEMBRO DE 2021"}
    meses3 = {"01": "01 - JANEIRO DE 2019","02":"02 - FEVEREIRO DE 2019","03": "03 - MARÇO DE 2019","04": "04 - ABRIL DE 2019","05":"05 - MAIO DE 2019","06": "06 - JUNHO DE 2019", "07": "07 - JULHO DE 2019", "08": "08 - AGOSTO DE 2019", "09": "09 - SETEMBRO DE 2019", "10": "10 - OUTUBRO DE 2019", "11":"11- NOVEMBRO DE 2019", "12":"12 - DEZEMBRO DE 2019"}

    counter = 0
    for arquivo in os.listdir(folder):
        
        #altera o fluxo de execução do programa se o arquivo deve ir para OP07, OP06, etc.
        if "OP07" in arquivo:
            destino = destinos['op07']
        elif 'OP06' in arquivo:
            destino = destinos['op06']
        if 'OP05' in arquivo:
            destino = destinos['op05']
        elif 'OPAB01' in arquivo:
            destino = destinos['opab01']
        elif 'ESCR' in arquivo:
            destino = destinos['escr']
        elif "CLOD" in arquivo:
            destino = destinos['clod']
        elif "- NA -" in arquivo:
            destino = destinos['na']
        elif "ALMOX" in arquivo:
            destino = destinos['almox']
        elif "OP04" in arquivo:
            destino = destinos['op04']
        elif "- BN -" in arquivo:
            destino = destinos['bn']
        elif "- PG -" in arquivo:
            destino = destinos['pg']
        elif "CABEDELO" in arquivo:
            destino = destinos['cabedelo']
        elif "AQBET" in arquivo: 
            destino = destinos["aqbet"]
        elif "AQTH" in arquivo: 
            destino = destinos["aqth"]
        elif "C&S" in arquivo: 
            destino = destinos["c&s"]

        #fatia o nome do arquivo em dia, mes e ano pra ficar melhor de tratar esses valores
        day = arquivo.strip()[0:2]
        month = arquivo.strip()[3:5]
        year = arquivo.strip()[6:8]


        #passo 1 - tentar encontrar o ano que a nota se refere
        file_list = drive.ListFile({"q": f"'{destino}' in parents and trashed=false"}).GetList()
        for ano in file_list:
            if "20"+year == ano['title']:
                destino = ano['id']

        # passo 2 - tentar encontrar o mes referente a nota
        file_list = drive.ListFile({"q": f"'{destino}' in parents and trashed=false"}).GetList()
        titles = []
        
        for arq in file_list:
            titles.append(arq['title'])


        if year == '22':
            if meses[month] not in titles:
                title = meses[month]
                newFolder = drive.CreateFile({"title": f"{title}", "mimeType": "application/vnd.google-apps.folder", "parents": [{"kind": "drive#fileLink", "id": destino}]})
                newFolder.Upload()
                destino = newFolder['id']
                
            else:
                for mes in file_list:
                    if month in mes['title'][0:3]:
                        destino = mes['id']
        elif year == '21':
            if meses2[month] not in titles:
                title = meses2[month]
                newFolder = drive.CreateFile({"title": f"{title}", "mimeType": "application/vnd.google-apps.folder", "parents": [{"kind": "drive#fileLink", "id": destino}]})
                newFolder.Upload()
                destino = newFolder['id']
                
            else:
                for mes in file_list:
                    if month in mes['title'][0:3]:
                        destino = mes['id']
        elif year == '19':
            if meses3[month] not in titles:
                title = meses3[month]
                newFolder = drive.CreateFile({"title": f"{title}", "mimeType": "application/vnd.google-apps.folder", "parents": [{"kind": "drive#fileLink", "id": destino}]})
                newFolder.Upload()
                destino = newFolder['id']
                
            else:
                for mes in file_list:
                    if month in mes['title'][0:3]:
                        destino = mes['id']



        #passo 3 - tentar encontrar o dia referente a nota
        file_list = drive.ListFile({"q": f"'{destino}' in parents and trashed=false"}).GetList()
        titles = []
        for arq in file_list:
            titles.append(arq['title'])

        # se não existir um titulo dd.mm.yy que se enquadre, o programa cria a pasta e pega o id dela 
        if arquivo[0:8] not in titles:
            title = arquivo[0:8]
            newFolder = drive.CreateFile({"title": f"{title}", "mimeType": "application/vnd.google-apps.folder", "parents": [{"kind": "drive#fileLink", "id": destino}]})
            newFolder.Upload()
            destino = newFolder['id']
        else:
            #se a pasta existir, o programa varre a lista para tentar encontrar a mesma e seu id
            for dia in file_list:
                if day in dia['title'][0:2]:
                    #atribui o a variável destino o id da pasta final, onde o arquivo será enviado
                    destino = dia['id']
            
        #com tudo feito e a pasta de destino encontrado, é feito nas seguintes linhas o upload do arquivo para a sua pasta
        fileUp = drive.CreateFile({"parents": [{"id": destino}], "title": arquivo})
        fileUp.SetContentFile(folder+arquivo)
        fileUp.Upload()
        print('='*15)
        print(f"{arquivo} adicionado ao drive!")
        counter+=1
        print(f'quantidade: {counter}')
        print('='*15)
        # os.remove(folder + arquivo)
        


SendFilesToDrive("./files/")
