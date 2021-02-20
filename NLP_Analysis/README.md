### Text NLP Analysis

**User Stories**  
As a user, I want to  
basic search functionality using keywords  
be able to pass text to the API and get in return its sentiment  
pass text into an API in other languages that could be understood or translated  
automatically extract and classify text data, such as tweets, emails  

**Procedure based API**  
translated_text=translate(text)  
sentiment = get_sentiment(text)  
bias = compare(text1, text2)  

**Data Structure**  
ID, FileType, UserID, CreatedTime(TimeStamp), FileSize, NLP entities (Keywords), sentiment, Content of the file, Notes, File Tags, Permissions, ModifiedTime, File source, File authors, File Status(Uploaded, Under conversion, NLP processed)

**object**  
TEXT = {"TEXT_ID": "text_id",  
               "TEXT": "text",  
               "Sentiment": "semtiment",  
               "NLP": ["nlp1","nlp2","nlp3"]  
              }    

#### method
**File**  
Post /file    
Post /file/{File_ID}/FileURL    
Post /file/{File_ID}/File_Metadata    
Post /file/{File_ID}/TEXT  
Put /file/{fileID}  
Put /file/{File_ID}/FileURL    
Put /file/{File_ID}/File_Metadata    
Put /file/{File_ID}/TEXT  
Get /file/findByStatus  
Get /file/{File_ID}  
Get /file/{File_ID}/FileURL    
Get /file/{File_ID}/File_Metadata    
Get /file/{File_ID}/TEXT  
Delete /file/{File_ID}  

**User**  
Post /User/{User_ID}  
Put /User/{User_ID}  
Get /User/{User_ID}/allfiles  
Delete /User/{User_ID}  
Delete /User/{User_ID}/allfiles  

**Events**    
Event_Convert: File is converted to text in English  
Event_Process: NLP analysis request and process the analysis 
Event_Update: File is updated and re-analyze again

Create() - Post  
Delete() - Delete  
Update() - Put  
Read() - Get  



