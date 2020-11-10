import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCSG9ymA4J2DKE8rjKIHDWgDNqBZTCxYBA",
    "authDomain": "data-analysis-68b5a.firebaseapp.com",
    "databaseURL": "https://data-analysis-68b5a.firebaseio.com",
    "projectId": "data-analysis-68b5a",
    "storageBucket": "data-analysis-68b5a.appspot.com",
    "messagingSenderId": "459401032843",
    "appId": "1:459401032843:web:ceebc4f914699af25f508e",
    "measurementId": "G-RQM08K7B6C"
  }

app = pyrebase.initialize_app(config=firebaseConfig)

storage = app.storage()

#Up lên
# storage.put("WORLDCUP.xlsx")

#Tải xuống
storage.child("WORLDCUP.xlsx").download(path="", filename="file.xlsx")