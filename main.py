import matplotlib.pyplot as plt
import os

###################
#### Functions ####
###################

def station_names_numbers():
    '''
    Reads in the header and returns a dictionary which maps the station name on to the station number
    '''
    with open(path+'/KNMI_20200825.txt') as dataset:
        header = []
        for i in range(0,99):                                              #  The header
            header.append(dataset.readline())
        stations_info = []
        for i,line in enumerate(header):
            if i in range(5,55):                                           #  The stations in the header
                stations_info.append(line.replace(':','').strip('#').split('  '))
                station_names = []
                station_numbers = []
        for i,line in enumerate(stations_info):
            station_names.append(line[-1].strip('\n'))
            station_numbers.append(line[0])        
        station_names_key = dict(zip(station_names,station_numbers))
        return station_names_key 


def variable_name_position():
    '''
    Reads in the last-but-one line of the header with the list of variable names and returns a dictionary to map a variable name to its position in the
    list (starting with 0), i.e. to map a variable to the corresponding column index in the data.
    '''
    with open(path+'/KNMI_20200825.txt') as dataset:
        i=0
        while i != 98:                                                    #  The last-but-one line of the header                                      
            line_to_read=dataset.readline()
            i+=1
        list_of_variables = line_to_read.strip('#').split(',')
        position_in_list = []
        for j,value in enumerate(list_of_variables):            
            list_of_variables[j]=value.strip()
            position_in_list.append(j)
        variables_positions = dict(zip(list_of_variables,position_in_list))
    return variables_positions 


def numerical_data():
    '''
    Reads in all the data (following the header), returning it as a nested list.  Empty fields are replaced with the None.
    '''
    data_after_header = []
    with open(path+'/KNMI_20200825.txt') as dataset:
        for i,data in enumerate(dataset):                                
            if i>98:                                                     #  The actual data
                data_after_header.append(data.split(','))
        for i,value in enumerate(data_after_header):     
            for j,inner_value in enumerate(value):
                if inner_value.strip() == '':
                    data_after_header[i][j] = None
                elif j != 0 and j != 1:
                    data_after_header[i][j] = float(data_after_header[i][j])
            value[0] = int(value[0].strip())
    return data_after_header


def plot_generator(data_task1,data_task2,data_task3,station):               
    '''
    Uses the outputs from the three functions described above, along with a station name (not number!) and a set of variable names, to
    make plots for the given station The quantities are averaged over the whole time period covered by the data for that station, 
    and plotted vs. the month on the x-axis.
    '''                                                                  
    max_temp = [[] for i in range(12)]                             
    min_temp = [[] for i in range(12)]                             #  We define lists to store the data before we process it
    daily_sum_rain = [[] for i in range(12)]                       
    sunshine_duration = [[] for i in range(12)]  

    max_avar_temp = []                                    #  We define lists to store the final avaraged values
    min_avar_temp = []                                      
    daily_avar_sum_rain = []
    avar_sunshine_duration = [] 


    #months = ['{:2d}'.format(i).replace(' ','0') for i in range(1,13)]                      #  months as numbers derived from the data for visualization
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']      # a list of month names
    for key,value in data_task1.items():
        if key==station:
            station_number=int(value)

    for inner_value in data_task3:
        if inner_value[0]==station_number:
            parent_month=int(inner_value[1][4:6])
            if inner_value[data_task2['TX']] != None:                        
                max_temp[parent_month-1].append(inner_value[data_task2['TX']])                   
            if inner_value[data_task2['TN']] != None:                       
                min_temp[parent_month-1].append(inner_value[data_task2['TN']])
            if inner_value[data_task2['RH']] != None:
                if inner_value[data_task2['RH']] == -1: 
                    inner_value[data_task2['RH']] = 0
                daily_sum_rain[parent_month-1].append(inner_value[data_task2['RH']])
            if inner_value[data_task2['SQ']] != None:                    
                if inner_value[data_task2['SQ']] == -1:
                    inner_value[data_task2['SQ']] = 0
                sunshine_duration[parent_month-1].append(inner_value[data_task2['SQ']])                       
                        
    if max_temp == [[]]*12 :                                     
        print('No maximum temp data for this month')              
    else: 
        for i in range(len(max_temp)):                                                   
            max_avar_temp.append(sum(max_temp[i])*0.1/len(max_temp[i]))
    if min_temp == [[]]*12:
        print('No minimum temp data for this month')     
    else:    
        for i in range(len(min_temp)):                             
            min_avar_temp.append(sum(min_temp[i])*0.1/len(min_temp[i]))        
    if daily_sum_rain == [[]]*12:
        print('No 24-hour sum of precipitation data for this month')     
    else:
        for i in range(len(daily_sum_rain)):
            daily_avar_sum_rain.append(sum(daily_sum_rain[i])*(0.1/24)/len(daily_sum_rain[i]))  
    if sunshine_duration == [[]]*12:
        print('No sunshine duration data for this month')     
    else:
        for i in range(len(sunshine_duration)):
            avar_sunshine_duration.append(sum(sunshine_duration[i])*0.1/len(sunshine_duration[i])) 
 
    # The monthly averages of maximum temperature (in Celsius)

    if max_avar_temp != []:                      
        fig = plt.figure()
        plt.plot(months,max_avar_temp, 'red')
        plt.bar(months,max_avar_temp)
        plt.xlabel('Months')
        plt.ylabel('Temperature (℃)')
        plt.title('Monthly Avarage of Maximum Temperature')
        plt.grid()
        plt.show()

    # The monthly averages of minimum temperature (in Celsius)

    if min_avar_temp != []:
        fig = plt.figure()
        plt.plot(months,min_avar_temp, 'red')
        plt.bar(months,min_avar_temp)
        plt.xlabel('Months')
        plt.ylabel('Temperature (℃)')
        plt.title('Monthly Avarage of Minimum Temperature')
        plt.grid()
        plt.show()
    
    # The daily avarage sum of precipitation (in mm/hour)

    if daily_avar_sum_rain != []:
        fig = plt.figure()
        plt.plot(months,daily_avar_sum_rain, 'red')  
        plt.bar(months,daily_avar_sum_rain)
        plt.xlabel('Months')
        plt.ylabel('Height (mm/h)')
        plt.title('Monthly Avarage of the Daily Sum of Precipitation')
        plt.grid()
        plt.show()
    
    # The avarage duration of sunshine (in hours)

    if avar_sunshine_duration != []:
        fig = plt.figure()
        plt.plot(months,avar_sunshine_duration, 'red')  
        plt.bar(months,avar_sunshine_duration)
        plt.xlabel('Months')
        plt.ylabel('Time (h)')
        plt.title('Monthly Avarage of the Total Duration of Sunshine')
        plt.grid() 
        plt.show()

#######################
#### Main Program #####
#######################

path = os.getcwd()
station= "STAVOREN"                                          #  Write the name of tha station that we want to investigate
plot_generator(station_names_numbers(),variable_name_position(),numerical_data(),station)

