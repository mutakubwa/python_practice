#!/usr/bin/env python3

import re
import operator
import sys
import csv

'''
Run With three arguments:
1. error message csv file
2. Error stattistics csv file
3. syslog file to analyse
error_message.csv user_statistics.csv syslog.log
'''
def sortDictByValue(dict_var):
    sortedDict = sorted(dict_var.items(), key=operator.itemgetter(1), reverse = True)
    return sortedDict

def sortDictByValueUser(dict_var):
    sortedDict = sorted(dict_var.items(), key=operator.itemgetter(0))
    return sortedDict

#Pattern to get errors and homany times each was generated
def getLogPattern(pattern, filename):
    
    regex = re.compile(pattern)
    dict_log = {}
    with open(filename,"r") as log:
        for line in log.readlines():
            result = regex.search(line.strip())
            if result is not None:
                if result[1] not in dict_log:
                    dict_log[result[1]] = 1
                else:
                    dict_log[result[1]] = dict_log.get(result[1], 0) + 1

        log.close()
    return dict_log

def getLogPatternByUser(pattern, filename):
    
    regex = re.compile(pattern)
    dict_log = {}

    with open(filename,"r") as log:
        for line in log.readlines():
            result = regex.search(line.strip())
            if result is not None:
                if result.group(2) not in dict_log:
                    dict_log[result.group(2).strip()] = {'INFO':0 , 'ERROR': 0}
                dict_log[result.group(2).strip()][result.group(1).strip()] += 1
        log.close()
    return dict_log

#write items in dict to csv
def writeToCsv(filename, dict_var):
    sort_val = sortDictByValue(dict_var)
    with open(filename,"w", newline="\n") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Error','Count'])
        for item in sort_val:
            writer.writerow( [ item[0].strip() ,item[1] ] )
    csv_file.close()


#write items in dict to csv
def writeToCsvByUser(filename, dict_var):
    sort_val = sortDictByValueUser(dict_var)
    with open(filename,"w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Username','INFO','ERROR'])
        for user in sort_val:
            writer.writerow([ user[0] ,user[1]['INFO'], user[1]['ERROR'] ])
                
    csv_file.close()

#example pattern for errors and number of times they occur
##pattern1 =  r"ticky: ERROR ([\w' ]*)"

#example pattern for errors and info messages by user
##pattern2 =  r"ticky: (ERROR|INFO) [\w#' \[\]]*[\( )]*([\w.]*)[\) ]*"

