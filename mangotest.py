import pymongo


client = pymongo.MongoClient("mongodb+srv://vaibhavmarkande1:Vaibhav9421516301@cluster0.anucy.mongodb.net/?retryWrites=true&w=majority")
db= client.test
print(db)

d = {'name' : 'sudhanshu',
    'email' : 'sudhanshu@ineuron.ai',
    'surname' : 'kumar'}

e = {'name' : 'sudhanshu',
    'email' : 'sudhanshu@ineuron.ai',
    'surname' : 'kumar'}

c = {'name' : 'sudhanshu',
    'email' : 'sudhanshu@ineuron.ai',
    'surname' : 'kumar'}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

