'''
Created on 2 août 2017

@author: Junyang HE
'''

class Lesson(object):
    date = ""
    fromTime = ""
    toTime = ""
    type = ""
    room = []
    instructors = []
    learners = []
    groups = []
    course = []
    
    def __init__(self, date, fromTime, toTime, courseType, room, instructors, learners, groups, course):
        self.date = date
        self.fromTime = fromTime
        self.toTime = toTime
        self.courseType = courseType
        self.room = room
        self.instructors = instructors
        self.learners = learners
        self.groups = groups
        self.course = course
        
    def printLesson(self):
        print("Date: " + self.date.strftime('%Y-%m-%d') + "    From: " + self.fromTime + "    To: " + self.toTime)
        print("Type: " + self.courseType)
        if len(self.room) > 1:
            print("Room: " + ''.join(str(e) + ", " for e in self.room))
        elif len(self.room) == 1:
            print("Room: " + self.room[0])
            
        if len(self.instructors) > 1:
            print("Intervenant: " + ''.join(str(e) + ", " for e in self.instructors))
        elif len(self.instructors) == 1:
            print("Intervenant: " + self.instructors[0])
            
        print("Learners: " + str(len(self.learners)))
        print("Groups: " + str(len(self.groups)))
        print("Course: " + self.course)
        print("\n")
        #print(*self.learners, sep='\n')
        #print(*self.groups, sep='\n')