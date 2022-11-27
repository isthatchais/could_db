import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#from bottle import route, run, template, request, redirect, post

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#print everything in the DB
'''docs = db.collection('patient').get()
for doc in docs:
    print(doc.to_dict())'''

#qurey using a where and a comparision operator
'''docs = db.collection('patient').where('age', '>', 80).get()
for doc in docs:
    print(doc.to_dict())'''

#query using an array contains 
'''docs = db.collection('patient').where('diagnosis', 'array_contains', 'GLF').get()
for doc in docs:
    print(doc.to_dict())'''

#query using a string
'''docs = db.collection('patient').where('WB_status', '==', 'NWB').get()
for doc in docs:
    print(doc.to_dict())'''

#retreive doc.id then remove from medication list
'''docs = db.collection('patient').get()
for doc in docs:
    if doc.to_dict()['name']=='Jerry Smith':
        key = doc.id
        db.collection('patient').document(key).update({"medication": firestore.ArrayRemove(['Bupropion'])})'''

#retreive doc.id then add to medication list
'''docs = db.collection('patient').get()
for doc in docs:
    if doc.to_dict()['name']=='Jerry Smith':
        key = doc.id
        db.collection('patient').document(key).update({"medication": firestore.ArrayUnion(['Hydrocodone'])})'''

#retreive id then update age by one year
'''docs = db.collection('patient').get()
for doc in docs:
    if doc.to_dict()['name']=='Jerry Smith':
        key = doc.id
        db.collection('patient').document(key).update({"age": firestore.Increment(1)})'''

#retrive id then update Wb_status and medication
'''docs = db.collection('patient').get()
for doc in docs:
    if doc.to_dict()['name']=='Cindi Hill':
        key = doc.id
        db.collection('patient').document(key).update({"WB_status": "WBAT"})
        db.collection('patient').document(key).update({'medication': firestore.ArrayUnion(['Oxycodone'])})'''

#This looks like a better way to do what was done above
'''docs = db.collection('patient').where('name', '==', 'Cindi Hill').get()
for doc in docs:
    key = doc.id
    db.collection('patient').document(key).update({"WB_status": "NWB"})
    db.collection('patient').document(key).update({'medication': firestore.ArrayRemove(['Oxycodone'])})'''

#retreive id then delete field
'''docs = db.collection('patient').where('name', '==', 'Cindi Hill').get()
for doc in docs:
    key = doc.id
    db.collection('patient').document(key).update({"medication": firestore.DELETE_FIELD})'''

#retreive id then add field
'''docs = db.collection('patient').where('name', '==', 'Cindi Hill').get()
for doc in docs:
    key = doc.id
    db.collection('patient').document(key).update({"medication": firestore.ArrayUnion(['Ocycodone', 'Metformin', 'Gabepentin', 'Omeprazol', 'Tylenol', 'Multi-Vitiman'])})'''

#retrive id then update med list
'''docs = db.collection('patient').where('name', '==', 'Cindi Hill').get()
for doc in docs:
    key = doc.id
    db.collection('patient').document(key).update({"medication": firestore.ArrayRemove(['Multi-Vitamin'])})'''

#the doc came and wants everyone to take a multi vitamin 
'''docs = db.collection('patient').get()
for doc in docs:
    key = doc.id
    db.collection('patient').document(key).update({"medication": firestore.ArrayUnion(['Multi-Vitamin'])})'''

#Insurance is only reimbursing if they have a dx of weakness
'''docs = db.collection('patient').get()
for doc in docs:
    key = doc.id
    db.collection('patient').document(key).update({"diagnosis": firestore.ArrayUnion(['Weakness'])})'''

#Change Ground Level Fall to GLF
'''docs = db.collection('patient').where('diagnosis', 'array_contains', 'Ground Level Fall').get()
for doc in docs:
    key = doc.id
    db.collection('patient').document(key).update({'diagnosis': firestore.ArrayUnion(['GLF'])})
    db.collection('patient').document(key).update({'diagnosis': firestore.ArrayRemove(['Ground Level Fall'])})'''

#How many patients have the dx GLF
'''count = 0
docs = db.collection('patient').where('diagnosis', 'array_contains', 'GLF').get()
for doc in docs:
    count += 1
print('We have %d patients who are injured as a result of a ground level fall' % count)'''

#what are the total therapy minutes
"""minutes = 0
docs = db.collection('patient').get()
for doc in docs:
    i = 0
    i = doc.to_dict()['minutes']
    minutes += i
print('total therapy minutes = %d'% minutes)"""

#how many patients are 75 or older and what are the names
"""count = 0
names = []
docs = db.collection('patient').where('age', '>=', 75).get()
for doc in docs:
    names.append((doc.to_dict()['name']))
    count += 1
print('There are %d patients who are 75 or older.' % count)
for name in names:
    print(name)"""

#names and minutes
'''docs = db.collection('patient').get()
for doc in docs:
    print(doc.to_dict()['name']+ "  " + str(doc.to_dict()['diagnosis']) +"  "+ str(doc.to_dict()['minutes']))'''


#delete all documents
docs = db.collection('patient').get()
for doc in docs:
    key = doc.id
    db.collection('patient').document(key).delete()