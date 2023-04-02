import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://realtimefacerecognition-15565-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "19MH1A0501":
        {
            "name": "Gangadhar",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0502":
        {
            "name": "Amar",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0503":
        {
            "name": "U",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0504":
        {
            "name": "Teja",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0505":
        {
            "name": "Sravan",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0506":
        {
            "name": "Tandava",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0507":
        {
            "name": "Maha",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0508":
        {
            "name": "Detan",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0509":
        {
            "name": "Lakshmi",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0510":
        {
            "name": "Koti",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0511":
        {
            "name": "Ganesh",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0512":
        {
            "name": "Dadi Sravan",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0513":
        {
            "name": "Akash",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0514":
        {
            "name": "Harika",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0515":
        {
            "name": "Alekhya",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0516":
        {
            "name": "Sanjay",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0517":
        {
            "name": "Naveen",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0518":
        {
            "name": "Sruthi",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0519":
        {
            "name": "Somnath",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0520":
        {
            "name": "Yesawanth",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0521":
        {
            "name": "Akhil",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0522":
        {
            "name": "Teddy",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0523":
        {
            "name": "Phane",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0524":
        {
            "name": "Haarika",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0525":
        {
            "name": "Revathi",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0526":
        {
            "name": "Basha",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0527":
        {
            "name": "Vijaya",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0528":
        {
            "name": "Renuka",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0529":
        {
            "name": "Rakesh",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0530":
        {
            "name": "Pramodh",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0531":
        {
            "name": "Naveen",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0532":
        {
            "name": "Adithya",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0533":
        {
            "name": "Meghana",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0534":
        {
            "name": "Sanjay Bro",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0535":
        {
            "name": "Priyanka",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0536":
        {
            "name": "Serious",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0537":
        {
            "name": "Shekhar",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0538":
        {
            "name": "Shiva",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0539":
        {
            "name": "Moses",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0540":
        {
            "name": "Vennela",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0541":
        {
            "name": "Manideep",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0542":
        {
            "name": "Gopal",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0543":
        {
            "name": "Anudeep",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0544":
        {
            "name": "Srinivas",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0545":
        {
            "name": "Jyoshnavi",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0546":
        {
            "name": "Subhash",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0547":
        {
            "name": "Keerthana",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0548":
        {
            "name": "Swaroop",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0549":
        {
            "name": "Gangaraju",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0550":
        {
            "name": "Basheer",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0551":
        {
            "name": "Ravindra",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0552":
        {
            "name": "Kowsalya",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0553":
        {
            "name": "Ramam",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0554":
        {
            "name": "Pravalika",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0555":
        {
            "name": "Reddy",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0556":
        {
            "name": "Ramesh",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0557":
        {
            "name": "Akhil avins",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0558":
        {
            "name": "Geetha",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0559":
        {
            "name": "Alekhya Specs",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "19MH1A0560":
        {
            "name": "Harika Yerra",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0501":
        {
            "name": "Naveena",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0502":
        {
            "name": "Bro",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0503":
        {
            "name": "Uma",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0504":
        {
            "name": "Vivek",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0505":
        {
            "name": "Le Specs",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0506":
        {
            "name": "Rohit",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0507":
        {
            "name": "Siva Sai",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0508":
        {
            "name": "Lakshmi LE",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0509":
        {
            "name": "Vinay",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0510":
        {
            "name": "Sahithi",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0511":
        {
            "name": "Ravi",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20MH5A0512":
        {
            "name": "Kishore",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
