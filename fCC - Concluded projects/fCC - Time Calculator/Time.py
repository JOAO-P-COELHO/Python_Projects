# READ ME available in this folder

def add_time(start, duration, weekday=None): #0 - I take the parameters as strings and convert them in numbers
    start_elements = start.split(' ')
    start_element_hour = start_elements[0].split(':')
    start_hours = int(start_element_hour[0])
    start_minutes = int(start_element_hour[1])
    start_fuse = start_elements[1]
    fuse = start_fuse.lower()
    
    duration_elements = duration.split(':')
    duration_hours = int(duration_elements[0])
    duration_minutes = int(duration_elements[1])
    
    days_after = 0 #1 Initialing variables
    rest_hours = 0
    count_minutes = start_minutes + duration_minutes #2 - Starting with the math
    
    if weekday != None: #3 - If there is a weekday, I will transform it also
        weekday = weekday.lower()
        weekday = weekday.capitalize()
    
    def truncate(number): #4 - Useful function to convert numbers like 10.42 in 10 (it always "round" it low)
        return int(number * 10 ** 0) / 10 ** 0
    
    def hours_when_pm(count_hours, days_after=0): #5A - Functions that convert numbers to AM/PM 
        count_hours_12 = count_hours - 12
        fuse = "AM"
        days_after += 1
        return count_hours_12, fuse, days_after

    def hours_when_am(count_hours): #5B - Functions that convert numbers to AM/PM 
        count_hours_12 = count_hours - 12
        fuse = "PM"
        return count_hours_12, fuse
    
    def counting_minutes(count_minutes, count_hours): #6 - Function that converts minutes to hours
        if count_minutes >= 60:
            count_hours = count_hours + 1
            count_minutes = count_minutes - 60
   
        else:
            count_minutes = count_minutes
            count_hours = count_hours
        return count_minutes, count_hours
    
    
    def day_of_week(day): #7 - Function that converts weekdays to numbers (it will be useful later)
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
        
    week = ["no day", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"] #8 - Array of the weekdays (it will be useful later)
    
    days_after += truncate(duration_hours / 24) #9 - Start of the math to obtain the number of days later, if there is any
    rest_hours_of_day = (duration_hours / 24) - days_after
    rest_hours += round(rest_hours_of_day * 24)
    count_hours = start_hours + rest_hours
    count_minutes, count_hours = counting_minutes(count_minutes, count_hours)

#10 - The number of hours controls the number of "days later"
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


#11 - The number of days later controls the output
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
            number_days_week = days_after / 7 
            number_weeks = truncate(number_days_week)
            days_moving = round(((number_days_week) - number_weeks)*7)
            actual_number = day

            if days_moving + actual_number > 7:
                new_day = days_moving - (7-actual_number)
                week_day_final=week[new_day]
                print(f"{count_hours}:{count_minutes:02d} {fuse.upper()}, {week_day_final} ({int(days_after)} days later)")
            else:
                new_day = days_moving + actual_number
                week_day_final=week[new_day]
                print(f"{count_hours}:{count_minutes:02d} {fuse.upper()}, {week_day_final} ({int(days_after)} days later)")


#12 - Example:
add_time("8:16 PM", "466:02", "tuesday") #add_time("Hours in AM/PM", number of hours and minutes, a starting weekday)
# It returns: 12:03 AM, Thursday (2 days later)

## Project dificulty (out of 5): 4  
## Time spent: ~9 hours
## It passed all the 12 fCC's tests