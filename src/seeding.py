from src.models import db, User, Class
import uuid
from random import choice

def generateCredentials(count, username_prefix='user'):
    credentials = []
    for _ in range(count):
        uid = uuid.uuid4().hex  # 32-char hex string
        username = f"{username_prefix}_{uid[:8]}"  # e.g., user_1a2b3c4d
        password = uuid.uuid4().hex  # 32-char unique password
        credentials.append((username, password))
    return credentials

class Seeder:

    def __init__(self):
        
        # Lists for seeding the User table
        self.fNames = [
            "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander",
            "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo",
            "Jack", "Owen", "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt", "Matthew",
            "Luke", "Asher", "Carter", "Julian", "Grayson", "Leo", "Jayden", "Gabriel", "Isaac", "Lincoln",
            "Anthony", "Hudson", "Dylan", "Ezra", "Thomas", "Charles", "Christopher", "Jaxon", "Maverick", "Josiah",
            "Isaiah", "Andrew", "Elias", "Joshua", "Nathan", "Caleb", "Ryan", "Adrian", "Miles", "Eli",
            "Nolan", "Christian", "Aaron", "Cameron", "Ezekiel", "Colton", "Luca", "Landon", "Hunter", "Jonathan",
            "Santiago", "Axel", "Easton", "Cooper", "Jeremiah", "Angel", "Roman", "Connor", "Jameson", "Robert",
            "Greyson", "Jordan", "Ian", "Carson", "Jaxson", "Leonardo", "Nicholas", "Dominic", "Austin", "Everett",
            "Brooks", "Xavier", "Kai", "Jose", "Parker", "Adam", "Jace", "Wesley", "Kayden", "Silas"
        ]
        self.lNames = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
            "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
            "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
            "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
            "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
            "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
            "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
            "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
            "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
            "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez"
        ]
        self.classNames = [
    "English I", "English II", "English III", "English IV", "Honors English I", "Honors English II", "Honors English III", "AP English Language", "AP English Literature", "Creative Writing",
    "Algebra I", "Geometry", "Algebra II", "Pre-Calculus", "Calculus", "Honors Algebra II", "Statistics", "AP Calculus AB", "AP Calculus BC", "AP Statistics",
    "Biology", "Honors Biology", "Chemistry", "Honors Chemistry", "Physics", "Earth Science", "Environmental Science", "Anatomy and Physiology", "AP Biology", "AP Chemistry",
    "World History", "U.S. History", "Civics", "Economics", "Geography", "AP U.S. History", "AP World History", "AP Government", "Psychology", "AP Psychology",
    "Spanish I", "Spanish II", "French I", "French II", "German I", "German II", "Latin I", "Latin II", "AP Spanish Language", "ASL I",
    "Art I", "Art II", "Digital Art", "Graphic Design", "Photography", "Theater Arts", "Drama", "Band", "Choir", "Music Theory",
    "Physical Education", "Health", "Weight Training", "Team Sports", "Dance", "Yoga and Fitness", "Driver's Education", "Sports Medicine", "Recreational Sports", "Intro to Kinesiology",
    "Intro to Computer Science", "Web Design", "Game Development", "Python Programming", "AP Computer Science Principles", "AP Computer Science A", "Robotics", "Digital Media", "Cybersecurity Basics", "IT Fundamentals",
    "Business Math", "Accounting", "Entrepreneurship", "Marketing", "Personal Finance", "Career Prep", "Speech and Debate", "Yearbook", "Journalism", "Student Leadership"]


    def getStudent(self):
        cred = generateCredentials(1)
        return User(username=cred[0][0], password=cred[0][1], fname=choice(self.fNames), lname=choice(self.lNames), role="student")
    
    def getFaculty(self):
        cred = generateCredentials(1)
        return User(username=cred[0][0], password=cred[0][1], fname=choice(self.fNames), lname=choice(self.lNames), role="faculty")
    
    def getClass(self):
        cred = generateCredentials(1)
        return Class(name=choice(self.classNames))
    
