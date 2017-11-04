#!/usr/bin/python3
'''
Created on 2 août 2017

@author: Junyang HE
'''

import sys, getopt

def main(argv):
    icsPath = ''
    username = ''
    password = ''
    nbWeeks = 8
    debug = False
    try:
        opts,_ = getopt.getopt(argv,"hdo:u:p:w:")
    except getopt.GetoptError:
        print('planningGetter.py [option]')
        print(' -o <path/to/save/calendar.ics> Required')
        print(' -u username Required')
        print(' -p password Required')
        print(' -w crawl specified number of weeks\' planning, between 1 and 24')
        print(' -d enable debug mode')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('planningGetter.py [option]')
            print(' -o <path/to/save/calendar.ics> Required')
            print(' -u username Required')
            print(' -p password Required')
            print(' -w crawl specified number of weeks\' planning, between 1 and 24')
            print(' -d enable debug mode')
            sys.exit()
        elif opt in ("-o"):
            icsPath = arg
        elif opt in ("-u"):
            username = arg
        elif opt in ("-p"):
            password = arg
        elif opt in ("-d"):
            debug = True
        elif opt in ("-w"):
            nbWeeks = arg
    
    if not icsPath:
        print('planningGetter.py -o <icsPath> -u <username> -p <password>')
        print(' -o <path/to/save/calendar.ics> is required')
        sys.exit(2)
    if not username:
        print('planningGetter.py -o <icsPath> -u <username> -p <password>')
        print(' -u username Required')
        sys.exit(2)
    if not password:
        print('planningGetter.py -o <icsPath> -u <username> -p <password>')
        print(' -p password Required')
        sys.exit(2)
    try:
        if not (int(nbWeeks) >= 1 and int(nbWeeks) <= 24):
            print('Argument incorrect, need to between 1 and 24')
            print(' -w crawl specified number of weeks\' planning, between 1 and 24')
            sys.exit(2)
    except:
        print('Argument incorrect, need to be an integer')
        print(' -w crawl specified number of weeks\' planning, between 1 and 24')
        sys.exit(2)
    
    
    
    from PlanningGetter import CrawlEservices, AnalyzeInnerHTML, IcsGenerator
    if debug:
        print('Run in debug mode')
        
    IcsGenerator.generateIcs(AnalyzeInnerHTML.analyse(inners=CrawlEservices.connectEsv(
        debug = debug, usr=username, pwd=password, nbWeeks=int(nbWeeks))), icsPath)

    
    

if __name__ == "__main__":
    main(sys.argv[1:])



