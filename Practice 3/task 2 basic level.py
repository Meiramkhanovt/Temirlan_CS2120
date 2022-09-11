def season_events(number_of_months):
    if (number_of_months==1 or number_of_months==2 or number_of_months==12):
        if (number_of_months==1):{
            print('You were born in January. White snow fell outside the window')  
        }
        elif (number_of_months==12):{
        print('You were born in December. White snow fell outside the window') 
        }
        else:{
         print('You were born in February. White snow fell outside the window') 
        }
    elif (number_of_months==3 or number_of_months==4 or number_of_months==5):
        if (number_of_months==3):{
             print('You were born in March. Birds sang beautiful songs') 
        }
        elif (number_of_months==4):{
            print('You were born in April. Birds sang beautiful songs')
        }
        else:{
            print('You were born in May. Birds sang beautiful songs')
        }
    elif (number_of_months==6 or number_of_months==7 or number_of_months==8):
            if number_of_months==6:{
                print('You were born in June. The sun shone brighter than ever')
            }
            elif number_of_months==7:{
                print('You were born in July. The sun shone brighter than ever')
            }
            else:{
                print('You were born in August. The sun shone brighter than ever')
            }
    elif (number_of_months==9 or number_of_months==10 or number_of_months==11):
        if(number_of_months==9):{
            print('You were born in September. The harvest was incredible')
        }
        elif(number_of_months==11):{
            print('You were born in November. The harvest was incredible')
        }
        else:{
            print('You were born in October. The harvest was incredible')
        }
    else:
        print('Something went wrong')
number=int(input('In which month were you born? '))
season_events(number)
#pr 3 tas 2