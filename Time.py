def add_time(start=None, duration=None, weekday=None): 
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
        print("minutos tem de dar 63:",count_minutes)
        print("horas tem de começar 11", count_hours)
        if count_minutes >= 60:
            count_hours = count_hours + 1
            count_minutes = count_minutes - 60
   
        else:
            count_minutes = count_minutes
            count_hours = count_hours
        print("minutres agora tem de dar 03:", count_minutes)   
        print("count_hours tem de dar 12:", count_hours)
        return count_minutes, count_hours
    
    days_after += truncate(duration_hours / 24)
    print("days after:", days_after)
    rest_hours_of_day = (duration_hours / 24) - days_after
    print("remaining of the day:", rest_hours_of_day)
    rest_hours += round(rest_hours_of_day * 24)
    print("rest of day", rest_hours)
    count_hours = start_hours + rest_hours
    print("count_hours:", count_hours)
    count_minutes, count_hours = counting_minutes(count_minutes, count_hours)
    print("minutes: ", count_minutes)
    print("hours: ", count_hours)
    print("o fuso ainda deveria ser o mesmo:",fuse )

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
        print(f"{count_hours}:{count_minutes:02d} {fuse.upper()}")
    elif days_after == 1:
        print(f"{count_hours}:{count_minutes:02d} {fuse.upper()} (next day)")
    elif days_after > 1:
        print(f"{count_hours}:{count_minutes:02d} {fuse.upper()} ({int(days_after)} days later)")

add_time("6:30 PM", "205:12")


# Quando o período de tempo a somar é superior a  24h há bug. Tem que se arranjar maneira dessas horas (por exemplo, 200 horas) se converterem em dias e o valor de horas restante ser somado
# Guardar este código e usá-lo só para casos específicos - fica como projeto pouco dificil e pouco util
# Resolver este problema usando antes uma conversão para as 24h    
    