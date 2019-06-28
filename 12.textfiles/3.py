"""
You are given a file called logfile.txt that lists log-on and log-off times for users of a
system. A typical line of the file looks like this:
Van Rossum, 14:22, 14:37
Each line has three entries separated by commas: a username, a log-on time, and a log-off
time. Times are given in 24-hour format. You may assume that all log-ons and log-offs occur
within a single workday.
Write a program that scans through the file and prints out all users who were online for at
least an hour.
"""
lines=[line.strip() for line in open('12.textfiles/logfile.txt')]
log_info=[line.split(',') for line in lines]

for line in log_info:
    for j in range (len(line)):
        line[j]=line[j].strip()
    
    if (int(line[2][0:2])+int(line[2][-2:])/60)-(int(line[1][0:2])+int(line[1][-2:])/60)>=1:
        print(line)
