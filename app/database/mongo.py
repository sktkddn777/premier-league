from bson.objectid import ObjectId
import motor.motor_asyncio
import pymongo

MONGO_DETAILS = "mongodb://localhost:27017"
# client = pymongo.MongoClient(MONGO_DETAILS, username="root", password="example")

# db = client["data"]
# mycollection = db["patient"]
# othercollection = db["doctor"]

# patient_record = {
#    "Name": "Maureen Skinner",
#    "Age": 87,
#    "Sex": "F",
#    "Blood pressure": [{"sys": 156}, {"dia": 82}],
#    "Heart rate": 82
# }

# doctor_record = {
#    "Name": "Simpson",
#    "Age": 23,
#    "Sex": "M",
#    "Blood pressure": [{"sys": 170}, {"dia": 67}],
#    "Heart rate": 100
# }

# mycollection.insert_one(patient_record)
# othercollection.insert_one(doctor_record)


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS, username="root", password="example")

database = client.teams

team_collection = database.get_collection("teams_collection")


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }