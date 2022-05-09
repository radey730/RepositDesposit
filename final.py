import requests, math, time, pathlib, csv #import libraries

API_KEY = 'zYYA7iW9nJ5dZ8NBMaBGcfDmjCFiYbWx'
base_url= 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Embiid&api-key=zYYA7iW9nJ5dZ8NBMaBGcfDmjCFiYbWx'
#using params parameter from the requests.get() method to pass in the API key 
parameters={'q':'Embiid', 'api-key': API_KEY}
 
response=requests.get(base_url,params=parameters)
 
content = response.json()
#print(content)
total_pages = content['response']['meta']['hits']
print(total_pages)
 
total_pages = math.ceil(total_pages/10)
print(total_pages)

parameters['page']=0
response=requests.get(base_url,params=parameters)


parameters['fq']='document_type:("article")'
 
parameters['begin_date']='20201222'
parameters['end_date']='20210516'
print(parameters)

d_sn_filters='document_type:("article") AND section_name: ("NBA")'
 
#for i in range(total_pages):
#    parameters['page']=i
 #   response=requests.get(base_url,params=parameters)
   # content = response.json()
  #  for i in content['response']['docs']:
    #    print(i['headline']['main'])
   # time.sleep(10)

fl_tuple=('keywords','pub_date','web_url')
parameters['fl']=fl_tuple
 
embiid_data=[]
#!!!PUTTING IT  ALL TOGETHER
for i in content ['response']['docs']:
   pub_date=i['pub_date']
   web_url=i['web_url']
   for v in i ['keywords']:
       keyword=v['value']
       embiid_data.append({'date':pub_date,'web_url':web_url, 'keywords':keyword})

print(embiid_data) #prints all data gathered into a list in the terminal

cwd=pathlib.Path.cwd() #creates path object that represents current directory
 
current_dir=cwd/"embiid_data" #creates new path object that will be used to make a folder to store the .csv file
 
current_dir.mkdir(exist_ok=True) #creates new folder directory for collected data

python_file = current_dir/"embiid_data.csv" #creates path to csv file
python_file.touch() #selects the file that was just created
 
with python_file.open(mode='a', encoding='utf-8', newline='') as python_final: #opens csv file and sets it to write mide
    writer=csv.DictWriter(python_final, fieldnames=["date", "web_url", "keywords"]) #creates each field name so 
    writer.writeheader() #creates header for data
    writer.writerows(embiid_data) #fills each row with all of the collected data