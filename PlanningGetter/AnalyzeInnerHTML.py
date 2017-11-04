'''
Created on 1 août 2017

@author: Junyang HE
'''

def analyse(readFile=False, inners=[]):
    from bs4 import BeautifulSoup
    from PlanningGetter.util.FormatDateString import formatDateString
    from PlanningGetter import Lesson
    import io
    from PlanningGetter.util.log import logger
    logger.info("Analyzing started.")
    if not readFile:
        logger.debug("Data from param")
        blocks = inners
    else:
        logger.debug("Data from file")
        with io.open('test.txt', 'r', encoding='utf-8') as f:
            blocks = f.read().split("[[[Magic]]]")
        del blocks[-1]
    
    logger.debug(str(len(blocks)) + " blocks")
    
    lessons = []
    for block in blocks:
        # block = blocks[0]
        soup = BeautifulSoup(block, "lxml")
        mainDiv = soup.find_all('div')[1]
        assert 'ui-dialog-content' in mainDiv['class']
        assert 'ui-widget-content' in mainDiv['class']
        
        detailDiv = mainDiv.find_all(attrs={"class":"ui-panelgrid ui-widget panelgrid-info-epreuve"})
        detailDiv = detailDiv[0].find_all(attrs={"class":"ui-panelgrid-cell ui-grid-col-6"})
        
        if detailDiv[7].string:
            courseType = str(detailDiv[5].string) + " - " + str(detailDiv[7].string)
        else:
            courseType = str(detailDiv[5].string)

        tables = mainDiv.find_all('table')
        
        fromToTable = tables[0]
        resourceTable = tables[1]
        instructorsTable = tables[2]
        learnersTable = tables[3]
        gourpsTable = tables[4]
        courseTable = tables[5]

        resource = []
        resourceTds = resourceTable.find_all('td')
        if len(resourceTds) > 1:
            for i in range(0, len(resourceTds), 2):
                c1 = '' if resourceTds[i].string == None else resourceTds[i].string
                c2 = '' if resourceTds[i + 1].string == None else resourceTds[i].string
                resource.append(c1 + " - " + c2)
        else:
            resource.append(' ')
            
        instructors = []
        instructorTds = instructorsTable.find_all('td')
        if len(instructorTds) > 1:
            for i in range(0, len(instructorTds), 2):
                instructors.append(instructorTds[i].string + " " + instructorTds[i + 1].string)
        else:
            instructors.append(' ')
            
        learners = []
        learnerTds = learnersTable.find_all('td')
        for i in range(0, len(learnerTds), 2):
            if len(learnerTds[i].contents) > 1:
                learners.append(learnerTds[i].contents[1] + " " + learnerTds[i + 1].contents[1])
        
        groups = []
        groupTds = gourpsTable.find_all('td')
        for i in range(0, len(groupTds)):
            groups.append(groupTds[i].string)
            
        course = " "
        if len(courseTable.find_all('td')) > 1:
            c1 = '' if courseTable.find_all('td')[0].string == None else courseTable.find_all('td')[0].string
            c2 = '' if courseTable.find_all('td')[1].string == None else courseTable.find_all('td')[1].string

            course = c1 + " - " + c2
        
        dateStr = fromToTable.find_all('td')[1].string.replace(",", "")
        lesson = Lesson.Lesson(formatDateString(dateStr),
                               fromToTable.find_all('td')[3].string,
                               fromToTable.find_all('td')[7].string,
                               courseType, resource, instructors, learners, groups, course)
        # lesson.printLesson()
        
        lessons.append(lesson)
    
    logger.info("Analyze finished, " + str(len(lessons)) + " lessons.")

    return lessons

if __name__ == '__main__':
    analyse(readFile=True)






