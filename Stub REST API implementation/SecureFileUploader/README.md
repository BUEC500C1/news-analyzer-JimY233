### Secure File Uploader/Ingester

**User Stories**  
As a User, I want to  
upload various file types (pdf, docx,csv, etc.)  
be alerted if there were issues with uploading their files  
convert file types (e.g. from word, pdf to text)  
search for past files they have uploaded  
re-upload files when uploading fails  
secure uploading process  
keep my content private and safe  

**Entity-based API**    
Data: File{title,paragraph,sentence}  
Operations: create(upload - convert), delete, read(check_status), update(upload again)  
Status: Success, In process, Failure with error message (Convert failure; Upload failure - Space not enough;  
Upload failure - file type not supported; Upload failure - file broken; Upload failure - Internet connection problem) 

**Data Structure**  
ID, FileType, UserID, CreatedTime(TimeStamp), FileSize, NLP entities (Keywords), sentiment, Content of the file, Notes, File Tags, Permissions, ModifiedTime, File source, File authors, File Status(Uploaded, Under conversion, NLP processed)

**object**  
File = {  
    "ID:/document/User_ID/File_ID": {  
        "Uploadtime": "2021.2.17",  
        "FileURL": "securefileuploader/file1.pdf",  
        "FileMetadata": {"Authors": ["Jiaming Yu", "jimmy", "jiamingy"],  
                         "Modifiedtime": "2021.2.17",  
                         "File source": "google",  
                         "File size": "15MB",  
                         "File tags": ["tag1","tag2","tag3"]  
                        },  
      "TEXT": {"TEXT_ID": "text_id",  
               "TEXT": "text",  
               "Sentiment": "semtiment",  
               "NLP": ["nlp1","nlp2","nlp3"]  
              }    
    }  
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
Event_Upload: File is uploaded  
Event_Convert: file is converted to text  
Event_Update: File is updated  

Create() - Post  
Delete() - Delete  
Update() - Put  
Read() - Get  


