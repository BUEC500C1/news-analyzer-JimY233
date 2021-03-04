# Homework 2
Jiaming Yu
U72316560

## Phase 2
Use Flask to implement api  
Details are in app.py  
It use PyPDF2 to convert pdf to text and save the text part in sqlite3 database "mydatabase.db"  
It uses upload.html in templates  
It implement login by checking username and password in database.  
nlp analysis is in nlp folder  

## Phase 1
Three APIs: Secure File Uploader/Ingester; Text NLP Analysis; News feed Ingester  
Stub implementation and documenting part are explained in Modules folder

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



