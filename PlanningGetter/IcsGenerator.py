'''
Created on 3 août 2017

@author: jhe
'''

def generateIcs(lessons, path=''):
    from icalendar import Calendar, Event
    from datetime import datetime
    #import pytz
    from PlanningGetter.util.log import logger
    import random
    random.seed(233333)
    
    #tz = pytz.timezone('Europe/Paris')
    
    cal = Calendar()
    cal.add('prodid', '-//Catprogrammer.com//ESIGELEC Planning//FR')
    cal.add('version', '2.0')
    cal.add('method', 'publish')
    cal.add('X-WR-TIMEZONE', 'Europe/Paris')
    
    for lesson in lessons:
        e = Event()
        e.add('summary', lesson.courseType + " " + lesson.course)
        
        y = lesson.date.year
        m = lesson.date.month
        d = lesson.date.day
        fromH = int(lesson.fromTime.split(":")[0])
        fromM = int(lesson.fromTime.split(":")[1])
        toH = int(lesson.toTime.split(":")[0])
        toM = int(lesson.toTime.split(":")[1])
        
        e.add('dtstart', datetime(y,m,d,fromH,fromM,0))
        e.add('dtend', datetime(y,m,d,toH,toM,0))
        #e.add('dtstamp', datetime.now(tz=tz))
        e.add('dtstamp', datetime.now())
        e.add('uid', lesson.date.strftime('%Y%m%d') + lesson.fromTime.replace(":", "") + '/' + str(random.randint(0, 1000001)) + '@catprogrammer.com')
        e.add('description', lesson.instructors[0] + ", " + str(len(lesson.learners)) + " students")
        
        room = ""
        for r in lesson.room:
            room += r + ", "
        if not room.isspace():
            room = room[:-2]
            e.add('location', room)
        
        instructor = ""
        for orga in lesson.instructors:
            instructor += orga + ", "
        if not instructor.isspace():
            instructor = instructor[:-2]
            e.add('organizer', instructor)
        
        for group in lesson.groups:
            if not group.isspace():
                e.add('attendee', group)
        
        cal.add_component(e)
        
    logger.info("ICS generated.")
    
    import io
    if not path:
        with io.open('cal.ics','wb') as f:
            f.write(cal.to_ical())
    else:
        with io.open(path,'wb') as f:
            f.write(cal.to_ical())
    

if __name__ == '__main__':
    from PlanningGetter import AnalyzeInnerHTML
    generateIcs(AnalyzeInnerHTML.analyse(True, []), path='')