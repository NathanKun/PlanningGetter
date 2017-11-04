'''
Created on 2 août 2017

@author: jhe
'''


def formatDateString(dateStr):
    
    splited = dateStr.split(sep=" ")
    if len(splited) != 4:
        from util.log import logger
        logger.error("date string format error: " + dateStr)
        return "date string format error"
    
    newStr = splited[1] + "/" + splited[2] + "/" + splited[3]
    newStr = newStr.replace("janvier", "January") \
        .replace("février", "February") \
        .replace("mars", "March") \
        .replace("avril", "April") \
        .replace("mai", "May") \
        .replace("juin", "June") \
        .replace("juillet", "July") \
        .replace("août", "August") \
        .replace("septembre", "September") \
        .replace("octobre", "October") \
        .replace("novembre", "November") \
        .replace("décembre", "December")
        
    from datetime import datetime
    try:
        dt = datetime.strptime(newStr, '%d/%B/%Y')
    except:
        dt = datetime.strptime(newStr, '%B/%d/%Y')
    return dt