def experiment(hat=0, expected_balls=0, num_balls_drawn=0, num_experiments=0): 

    dict_to_list = []
    
    list_expected_balls = expected_balls
    for element in list_expected_balls:
        number_reps = list_expected_balls[element]
        while number_reps > 0:
            dict_to_list.append(element)
            number_reps -= 1
    
    print(dict_to_list)
        
            
            
probability = experiment(expected_balls = {"red":2,"green":1})