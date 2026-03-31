import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
  "name": "陳武林",
  "mail": "wlchen@pu.edu.tw",
  "lab": 665
},

{
  "name": "王耀德",
  "mail": "ytwang@pu.edu.tw",
  "lab": 686
},

{
  "name": "康贊清",
  "mail": "tckang@pu.edu.tw",
  "lab": 783
}

]

doc_ref = db.document("靜宜資管/tcyang")
doc = doc_ref.get()
result = doc.to_dict()
print("文件內容為：{}".format(result))
print("教師姓名："+result.get("name"))
print("教師郵件：" + result["mail"])
collection_ref = db.collection("靜宜資管")
for doc in docs:
  collection_ref.add(doc)
