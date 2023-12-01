def add_time(start, duration, weekday=None): 
    start_elements = start.split(' ')
    start_element_hour = start_elements[0].split(':')
    start_hours = int(start_element_hour[0])
    start_minutes = int(start_element_hour[1])
    start_fuse = start_elements[1]
    fuse = start_fuse.lower()
    
    duration_elements = duration.split(':')
    duration_hours = int(duration_elements[0])
    duration_minutes = int(duration_elements[1])
    
    days_after = 0
    rest_hours = 0
    count_minutes = start_minutes + duration_minutes
    
    if weekday != None:
        weekday = weekday.lower()
        weekday = weekday.capitalize()
    
    def truncate(number):
        return int(number * 10 ** 0) / 10 ** 0
    
    def hours_when_pm(count_hours, days_after=0):        
        count_hours_12 = count_hours - 12
        fuse = "AM"
        days_after += 1
        return count_hours_12, fuse, days_after

    def hours_when_am(count_hours):
        count_hours_12 = count_hours - 12
        fuse = "PM"
        return count_hours_12, fuse
    
    def counting_minutes(count_minutes, count_hours):
        if count_minutes >= 60:
            count_hours = count_hours + 1
            count_minutes = count_minutes - 60
   
        else:
            count_minutes = count_minutes
            count_hours = count_hours
        return count_minutes, count_hours
    
    
    def day_of_week(day):
        weekday = 0
        if day == "Monday":
            weekday = 1
        elif day == "Tuesday":
            weekday = 2
        elif day == "Wednesday":
            weekday = 3
        elif day == "Thursday":
            weekday = 4
        elif day == "Friday":
            weekday = 5
        elif day == "Saturday":
            weekday = 6
        elif day == "Sunday":
            weekday = 7 
        
        return weekday
        
    week = ["no day", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
    
    days_after += truncate(duration_hours / 24)

    rest_hours_of_day = (duration_hours / 24) - days_after

    rest_hours += round(rest_hours_of_day * 24)
    count_hours = start_hours + rest_hours
    count_minutes, count_hours = counting_minutes(count_minutes, count_hours)

    if duration_hours >= 24:
        if count_hours >= 12 and count_hours < 13 and fuse == "pm":
            count_hours = 12
            days_after += 1
            fuse = "am"    
        
        elif count_hours >= 12 and count_hours < 13 and fuse == "am":
            count_hours = 12
            fuse = "pm" 
            count_hours, fuse, days_after = hours_when_am(count_hours)
        
        elif count_hours >= 13 and fuse == "pm":
            count_hours, fuse, days_after = hours_when_pm(count_hours, days_after)
        
        elif count_hours >= 13 and fuse == "am":
            count_hours, fuse, days_after = hours_when_am(count_hours)
            
    elif duration_hours < 24:
        if count_hours >= 12 and count_hours < 13 and fuse == "pm":
            count_hours = 12
            days_after += 1
            fuse = "am"    
        
        elif count_hours >= 12 and count_hours < 13 and fuse == "am":
            count_hours = 12
            fuse = "pm" 
            
        elif count_hours >= 13 and fuse == "pm":
            count_hours, fuse, days_after = hours_when_pm(count_hours)
        
        elif count_hours >= 13 and fuse == "am":
            count_hours, fuse = hours_when_am(count_hours)


    if days_after == 0:
        if weekday == None:
            print(f"{count_hours}:{count_minutes:02d} {fuse.upper()}")
        elif weekday != None:
            print(f"{count_hours}:{count_minutes:02d} {fuse.upper()}, {weekday}")   
    elif days_after == 1:
        if weekday == None:
            print(f"{count_hours}:{count_minutes:02d} {fuse.upper()} (next day)")
        elif weekday != None:
            tomorrow = day_of_week(weekday)
            print(f"{count_hours}:{count_minutes:02d} {fuse.upper()}, {week[tomorrow+1]} (next day)")  
    elif days_after > 1:
        if weekday == None:
            print(f"{count_hours}:{count_minutes:02d} {fuse.upper()} ({int(days_after)} days later)")
        elif weekday != None:
            day = day_of_week(weekday)
            print(day)
            number_days_week = day / 7 
            print(number_days_week)
            number_weeks = truncate(number_days_week)
            days_moving = round(((number_days_week) - number_weeks)*7)
            print(days_moving)
            actual_number = 2

            if days_moving + actual_number > 7:
                new_day = days_moving - (7-actual_number)
            else:
                new_day = days_moving + actual_number
                week_day_final=week[new_day]
                print(f"{count_hours}:{count_minutes:02d} {fuse.upper()}, {week_day_final} ({int(days_after)} days later)")

 
add_time("8:16 PM", "466:02", "tuesday")

# Project dificulty (out of 5): 4  
# Time spent: xxx hours