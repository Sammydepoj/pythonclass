class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name='john'
        self.age='32'
        self.tracks=["FE","BE"]
        self.score=88.5

    def change_name(self,name):
        print(name)  
        return name

    def change_age(self,age):
        print(int(age))  
        return int(age)

    def add_tracks(self,tracks):
        print(tracks)  
        return tracks

    def get_score(self,score):
        print(float(score))  
        return float(score)    



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score(55.74)
