from pymongo import MongoClient


class DatabaseManager:
    def __init__(self, db_name):
        self.client = MongoClient("localhost", 27017)
        self.db_name = db_name
        self.db = self.client["Student_Advisor_DB"]
        self.students = self.db["students"]
        self.advisors = self.db["advisors"]
        self.student_advisor = self.db["student_advisor"]

    def add_data(self, collection_name, data):
        collection = getattr(self, collection_name)
        collection.insert_one(data)
        existing_entry = collection.find_one(data)
        if existing_entry:
            print("Member already exists in the data.")
        else:
            collection.insert_one(data)

    def list_data(self, collection_name):
        collection = getattr(self, collection_name)
        return list(collection.find({}, {"_id": 0}))

    def delete_row(self, collection_name, row_id):
        collection = getattr(self, collection_name)
        collection.delete_one({"_id": row_id})

    def search(self, collection_name, query):
        collection = getattr(self, collection_name)
        return list(collection.find(query, {"_id": 0}))

    def update(self, collection_name, query, new_data):
        collection = getattr(self, collection_name)
        collection.update_one(query, {"$set": new_data}, upsert=True)

    def add_student(self, data):
        self.add_data("students", data)

    def add_advisor(self, data):
        self.add_data("advisors", data)

    def add_student_advisor_relation(self, student_id, advisor_id):
        data = {"student_id": student_id, "advisor_id": advisor_id}
        self.add_data("student_advisor", data)

    def list_students(self):
        return self.list_data("students")

    def list_advisors(self):
        return self.list_data("advisors")

    def list_student_advisor_relations(self):
        return self.list_data("student_advisor")

    def list_advisors_with_no_students(self):
        advisors_with_students = [rel["advisor_id"] for rel in self.student_advisor.find({}, {"advisor_id": 1})]
        return list(self.advisors.find({"_id": {"$nin": advisors_with_students}}, {"_id": 0}))

    def count_most_students_advisor(self):
        pipeline = [
            {"$group": {"_id": "$advisor_id", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 1}
        ]
        result = list(self.student_advisor.aggregate(pipeline))
        if result:
            advisor_id = result[0]["_id"]
            advisor = self.advisors.find_one({"_id": advisor_id})
            return advisor
        else:
            return None

    def list_advisors_with_students(self):
        pipeline = [
            {"$lookup": {"from": "student_advisor", "localField": "_id", "foreignField": "advisor_id",
                         "as": "students"}},
            {"$match": {"students": {"$ne": []}}},
            {"$project": {"name": 1, "surname": 1, "students": 1}}
        ]
        return list(self.advisors.aggregate(pipeline))
