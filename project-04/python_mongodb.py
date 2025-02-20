
import pymongo
# not a good idea to include id and password in code files
client = pymongo.MongoClient("mongodb+srv://learnpython:learnpython@cluster0.x8mnc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["ytmanager"]


video_collection = db["videos"]

print(video_collection)