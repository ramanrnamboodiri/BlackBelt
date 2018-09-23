import datetime

now = datetime.datetime.now()
print ("Current date and time using instance attributes:")
print ("Current  Year: \t %d \n\t Month:\t %d \n\t Day: \t %d \n\t Hour: \t %d \n\t Minute: %d \n\t Second: %d" % (now.year, now.month, now.day, now.hour, now.minute, now.second))
