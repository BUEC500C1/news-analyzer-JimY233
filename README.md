# Homework 2
Jiaming Yu  
U72316560  

Three API modules: Secure File Uploader in `file_uploader` folder; Text NLP Analysis in `NLP` folder; News feed Ingester in `news_ingester` folder    
Stub function is in `Stub REST API implementation` folder    
Attention: On github, I did not include my google api key thus there is some issue in Github Actions but I have done AWS hosting successfully  
Here is where I store my google api key on EC2. The location is defined `/NLP/nlp/NLPAPI.py`, `/file_uploader/nlp/NLPAPI.py`and `/news_ingester/nlp/NLPAPI.py`  
<div align=center><img src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/google_key_location.PNG"/></div>

## Phase 2
Use Flask to implement api       
Three modules: Secure File Uploader in `file_uploader` folder; Text NLP Analysis in `NLP` folder; News feed Ingester in `news_ingester` folder     

In each folder, `app.py` is the api runned locally in my own computer and `ec2_*.py` is used on EC2      
Difference 1 for each `app.py` and `ec2_*.py`: the file location for database is different     
Before testing in your own computer, please change the file location for database to a suitable place for each `app.py` and `ec2_*.py`    
<div align=center><img src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/file_location.PNG"/></div>  
Difference 2 for each `app.py` and `ec2_*.py`: debug and port number    
<div align=center><img src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/api_hosting.PNG"/></div>  
Locally: run command `python app.py`      
Locally debugging: http://127.0.0.0/5000     
On EC2: `sudo python3 ec2_*.py`     
EC2 link: ec2-52-15-71-138.us-east-2.compute.amazonaws.com:443      
(On EC2, requirements like Flask should be installed with `sudo`)       

html files are kind of different even when they have the same name but in different api modules     
Use session to secure the user, every request check session['user_id'], if not, return to login website. Thus people can not directly go to .../upload without logging in   

**File Uploader**  
Please check `file_uploader` folder    
`app.py` is the api runned locally in my own computer and `ec2_fileuploader.py` is used on EC2  
html files are saved in templates folder  
Use PyPDF2 to convert pdf to text and save the text part in sqlite3 database "mydatabase.db", all three apis shares the same database       
It also has nlp analysis function and use nltk and google cloud language api to implement nlp analysis and the functions are saved in `/file_uploader/nlp` folder  
On EC2 Run `sudo python3 ec2_fileuploader.py`  
<div align=center><img src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_run.PNG"/></div>

Then we go to EC2 link  
and meet the login website (html file is `login.html` in templates folder)  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_login.PNG"/></div>

We can register one account (`register.html`)  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_register.PNG"/></div>

After logging in, we can see the upload system (`upload.html`)  
Username is shown in "Hello username" and all files under this user_id will also be shown  
As we can see, we can check whether the files with the same name is already in the database and decide to update it  
If the file is the first time uploaded, "save" will show.  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_upload.PNG"/></div>
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_update.PNG"/></div>
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_save.PNG"/></div>

Then we can click "Analyze" to nlp analyze the articles, we can select the article to analyze  
Username is shown in "Hello username" and all files under this user_id will also be shown  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_select.PNG"/></div>

After selected the files to analyze, we can do nlp analysis  
Username is shown in "Hello username" and all files under this user_id will also be shown  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_analysis1.PNG"/></div>
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_keyword.PNG"/></div>
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_sentiment.PNG"/></div>
keyword frequency and sentiment analysis is shown  

**NLP Analysis**  
Please check `NLP` folder  
`app.py` is the api runned locally in my own computer and `ec2_nlp.py` is used on EC2    
html files are saved in templates folder  
alayze the files saved in sqlite3 database "mydatabase.db" (share the database with other two api)  
It also has nlp analysis function and use nltk and google cloud language api to implement nlp analysis and the functions are saved in `/NLP/nlp` folder  
On EC2 Run `sudo python3 ec2_nlp.py`  
<div align=center><img src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_nlp.PNG.PNG"/></div>

All is the same in the file uploader api but when you log in, you skip the upload and directly go to nlp analysis  

**News Ingester**  
Please check `news_ingester` folder    
`app.py` is the api runned locally in my own computer and `ec2_news.py` is used on EC2   
html files are saved in templates folder  
Use News Api to download news according to keyword. Functions are in `/news_ingester/news`  
Saved in sqlite3 database "mydatabase.db",  all three apis shares the same database       
It also has nlp analysis function and use nltk and google cloud language api to implement nlp analysis and the functions are saved in `/news_ingester/nlp` folder  
On EC2 Run `sudo python3 ec2_fileuploader.py`  
<div align=center><img src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_news_run.PNG"/></div>

Then we go to EC2 link  
and meet the login website (html file is `login.html` in templates folder)  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_news_login.PNG"/></div>

We can register one account (`register.html`)  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_file_register.PNG"/></div>

After logging in, we can see the news ingester system (`ingest.html`)  
Username is shown in "Hello username" and all files under this user_id will also be shown  
You can decide the keyword and number of news you want to download and save to the database  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_news_ingest.PNG"/></div>

Then we can click "Analyze" to nlp analyze the articles, we can select the article to analyze. Here I implement primary key and thus we just need to input 1,2,3 as news_id  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_news_select.PNG"/></div>

After selected the files to analyze, we can do nlp analysis  
<div align=center><img width='600'src="https://github.com/BUEC500C1/news-analyzer-JimY233/blob/main/Figures/ec2_news_sentiment.PNG"/></div>



## Phase 1
Please check `Stub REST API implementation` folder  
Three APIs: Secure File Uploader/Ingester; Text NLP Analysis; News feed Ingester    
Stub implementation and documenting part are explained in `Stub REST API implementation` folder  

### User Stories

**Secure File Uploader/Ingester**    
As a User, I want to  
upload various file types (pdf, docx,csv, etc.)  
be alerted if there were issues with uploading their files  
convert file types (e.g. from word, pdf to text)  
search for past files they have uploaded  
re-upload files when uploading fails  
secure uploading process  
keep my content private and safe  

**Text NLP Analysis:**  
As a user, I want to  
basic search functionality using keywords  
be able to pass text to the API and get in return its sentiment  
pass text into an API in other languages that could be understood or translated  
automatically extract and classify text data, such as tweets, emails  

**News feed Ingester**  
As a user, I want to  
search based on keywords  
discover content from the WEB through url

### Decision
For each module, make a decision:  Procedure-based or entity-based  
For each module, decide on operations, data and status

**Secure File Uploader/Ingester**   
Entity-based API  
Data: File{title,paragraph,sentence}  
Operations: create(upload - convert), delete, read(check_status), update(upload again)  
Status: Success, In process, Failure with error message (Convert failure; Upload failure - Space not enough;  
Upload failure - file type not supported; Upload failure - file broken; Upload failure - Internet connection problem)  

**Text NLP Analysis**  
Procedure based API  
translated_text=translate(text)  
sentiment = get_sentiment(text)  
bias = compare(text1, text2)  

Data: text  
Status: Success, Failure  

**News feed Ingester**   
Procedure based API  
url = search_web(keyword)  
checkurl(url)  
content = get_url(url)  
converted = convert(content)  
final = format(converted)  

(Or maybe Entity-based API  
Data: File{keyword, articles}   
Operations: create(search(keyword)), delete, read(check_status), update(search and upload again)   
Status: Success, Failure)  



