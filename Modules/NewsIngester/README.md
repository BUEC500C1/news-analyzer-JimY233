### News feed Ingester

**User Stories**
As a user, I want to  
search based on keywords  
discover content from the WEB through url

**Procedure based API**
url = search_web(keyword)
checkurl(url)
content = get_url(url)
converted = convert(content)
final = format(converted)

**object**  
News = {  
    "ID:/document/User_ID/News_ID": {  
        "Uploadtime": "2021.2.17",  
        "NewsURL": "securefileuploader/file1.pdf",  
        "NewsMetadata": {"Authors": ["Jiaming Yu", "jimmy", "jiamingy"],  
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
**News File**  
Post /file/{File_ID}/FileURL    

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
Event_Searchbykeyword: searched url according to the keyword
Event_Download: Download from the web according to the url
Event_Save: Save the news file

Create() - Post  
Delete() - Delete  
Update() - Put  
Read() - Get  
