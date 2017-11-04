# PlanningGetter
Crawl your ESIGELEC planning and save as iCalendar .ics file
Use cron to run it regulary and save the ics file in a directory where can be accessed via the Internet, and import the link to your Google Calendar.

***
## Usage
    python planningGetter.py [option]
    options:
         -o <path/to/save/calendar.ics> Required
         -u <username> Required
         -p <password> Required
         -w <number> crawl specified number of weeks' planning, between 1 and 24
         -d enable debug mode
     
