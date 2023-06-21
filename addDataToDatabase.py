import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionattendanc-397d2-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={
    "689391":
        {
            "Name":"Suraj",
            "Department":"ECE",
            "Starting_year":"2020",
            "Total_Attendance":90,
            "Standing":"G",
            "Year":3,
            "Last_Attendance_Time":"2023-05-25 00:54:34"
        },
    "123456":
        {
            "Name":"Utkarsh",
            "Department":"ECE",
            "Starting_year":"2020",
            "Total_Attendance":22,
            "Standing":"G",
            "Year":1,
            "Last_Attendance_Time":"2023-05-25 00:54:34"
        },
    "234567":
        {
            "Name": "Shwetabh",
            "Department": "ECE",
            "Starting_year": "2020",
            "Total_Attendance": 11,
            "Standing": "G",
            "Year": 6,
            "Last_Attendance_Time": "2023-05-25 00:54:34"
        },
    "345678":
        {
            "Name": "Vaibhav",
            "Department": "ECE",
            "Starting_year": "2020",
            "Total_Attendance": 11,
            "Standing": "G",
            "Year": 6,
            "Last_Attendance_Time": "2023-05-25 00:54:34"
        },
    "321654":
        {
            "Name": "Mahraf",
            "Department": "ECE",
            "Starting_year": "2016",
            "Total_Attendance": 75,
            "Standing": "Average",
            "Year": 4,
            "Last_Attendance_Time": "2023-05-5 00:54:34"
        },
    "852741":
        {
            "Name": "Emily",
            "Department": "ETE",
            "Starting_year": "2020",
            "Total_Attendance": 10,
            "Standing": "G",
            "Year": 3,
            "Last_Attendance_Time": "2023-05-25 00:54:34"
        },
    "516234":
        {
            "Name":"Divyesh",
            "Department":"ECE",
            "Starting_year":"2020",
            "Total_Attendance":45,
            "Standing":"S",
            "Year":3,
            "Last_Attendance_Time":"2023-05-25 00:54:34",
        }
}

for key,value in data.items():
    ref.child(key).set(value)


