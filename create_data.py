import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#add with auto id

data = {'name': 'Jerry Smith', 'age':70, 'diagnosis': ['Respratory failure', 'DM type 2'], 'WB_status': 'WBAT', 'minutes': 60, 'medication': ['Omeprazole', 'Oxycodone', 'Tylenol', 'Carvedilol', 'Furosemide', 'Bupropion']}
db.collection('patient').add(data)

data0 = {'name': 'Dixie Johnson', 'age':68, 'diagnosis': ['Ground Level Fall', 'L hip fx'], 'WB_status': 'WBAT', 'minutes': 58, 'medication': ['Tramadol', 'Tylenol', 'Vitiman D', 'Furosemide', 'Fluoxetine']}
db.collection('patient').add(data0)

data1 = {'name': 'Carri Anerson', 'age':55, 'diagnosis': ['TIA', 'GERD', 'Dementia'], 'WB_status': 'WBAT', 'minutes': 44, 'medication': ['Benadryl', 'Tylenol', 'Omeprazole']}
db.collection('patient').add(data1)

data2 = {'name': 'Cindi Hill', 'age':77, 'diagnosis': ['GLF', 'R Femur fx'], 'WB_status': 'TTWB', 'minutes': 30, 'medication': ['Valium', 'Valtrex', 'Voltaren Gel', 'Omeprazole']}
db.collection('patient').add(data2)

data3 = {'name': 'Karen Smith', 'age':79, 'diagnosis': ['MVA', 'Multiple fxs'], 'WB_status': 'NWB', 'minutes': 90, 'medication': ['Metformin', 'Losartan', 'Gabepentin', 'Omeprazole']}
db.collection('patient').add(data3)

data4 = {'name': 'Clair Robertson', 'age':84, 'diagnosis': ['Influenza', 'DM type 2'], 'WB_status': 'WBAT', 'minutes': 75, 'medication': ['Atrovastatin', 'Amozicillin', 'Lisinopril','Levothyroxine']}
db.collection('patient').add(data4)

data5 = {'name': 'Susan Wilcox', 'age':90, 'diagnosis': ['Post Covid', 'CKD'], 'WB_status': 'WBAT', 'minutes': 48, 'medication': ['Adalimumab', 'Apixaban','Etenercept', 'Ustekinumab']}
db.collection('patient').add(data5)

data6 = {'name': 'Claudia Young', 'age':87, 'diagnosis': ['GLF','Pelvic Fx'], 'WB_status': 'WBAT', 'minutes': 60, 'medication': ['Hydrocodone', 'Gabatentin', 'Tylenol']}
db.collection('patient').add(data6)

data7 = {'name': 'Carolyn Ford', 'age':72, 'diagnosis': ['Lumbar Fusion'], 'WB_status': 'WBAT', 'minutes': 75, 'medication': ['Oxycodone', 'Accupril']}
db.collection('patient').add(data7)

data8 = {'name': 'Lauri West', 'age':84, 'diagnosis': ['Morbid Obesity', 'GLF', 'Tibial Plateau fx'], 'WB_status': 'TDWB', 'minutes': 40, 'medication': ['Oxycodone', 'Metformin', 'Tylenol', 'Carvedilol', 'Furosemide', 'Bupropion']}
db.collection('patient').add(data8)

data9 = {'name': 'Patti Thompson', 'age':91, 'diagnosis': ['GLF', 'Tibia fx'], 'WB_status': 'PWB', 'minutes': 85, 'medication': ['Oxycodone','Metformin', 'Losartan', 'Gabepentin', 'Omeprazole', 'Tylenol']}
db.collection('patient').add(data9)

data10 = {'name': 'Terry Bone', 'age':57, 'diagnosis': ['RSV', 'GLF', 'R Hip fx'], 'WB_status': 'WBAT' ,'minutes': 65, 'medication': ['Oxycodone', 'Tylenol', 'Carvedilol', 'Furosemide', 'Bupropion', 'Metformin']}
db.collection('patient').add(data10)

data11 = {'name': 'Coral Smith', 'age':89, 'diagnosis': ['GLF', 'R Femoral Neck fx', 'AKI'], 'WB_status': 'WBAT', 'minutes': 75, 'medication': ['Hydrocodone', 'Metformin', 'Losartan', 'Gabepentin', 'Omeprazole']}
db.collection('patient').add(data11)