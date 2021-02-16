Data Structure:

ID
FileType
UserID
CreatedTime(TimeStamp)
FileSize
NLP entities (Keywords)
sentiment
Content of the file
Notes
File Tags
Permissions
ModifiedTime
File source
File authors

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

User
[
]

Post /file
Post /User
Post /file/File_Metadata
Post /file/TEXT

Events:


