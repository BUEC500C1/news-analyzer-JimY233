Data Structure:  

ID, FileType, UserID, CreatedTime(TimeStamp), FileSize, NLP entities (Keywords), sentiment, Content of the file, Notes, File Tags, Permissions, ModifiedTime, File source, File authors, File Status(Uploaded, Under conversion, NLP processed)

ID:/document/User_ID/File_ID  
UploadTime:  
FILE URL:https://newsanalyzer/file1.pdf,  
File_Metadata:{  
Authors[],  
Timestamp,  
File source,  
File size,  
File tags[]  
},
TEXT:{  
TEXT_ID,  
TEXT  
Sentiment,  
NLP[]  
}

Post /file  
Post /User  
Post /file/File_Metadata  
Post /file/TEXT

Events:
Event_Upload: File is uploaded
Event_Convert: file is converted to text
Event_Update: File is updated

Create()
Delete()
Update()
Read()


