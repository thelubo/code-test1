# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 18:53:10 2022

@author: thelu
"""


Worker_info = {"experience workplace one":4,"experience workplace two":6,"experience workplace three":0}

print(Worker_info)      

Worker_values=Worker_info.values()
print(Worker_values)


required_experience = {"experience workplace one":5,"experience workplace two":3,"experience workplace three":1}


experience_values=required_experience.values()
print(experience_values)

d1=Worker_values
d2=required_experience
result={}


Worker_info = {"experience workplace one":4,"experience workplace two":6,"experience workplace three":0}
required_experience = {"experience workplace one":5,"experience workplace two":3,"experience workplace three":1}

result = {key: Worker_info[key]-required_experience[key] for key in Worker_info if key in required_experience}
print(result)


for value in result.values():
        if value > 0:
            print(value)



#print(Worker_info.values())
#print(required_experience.values())
#print(Worker_info["experience at workplace one"])
#workerkeys= required_experience.items()
#print(workerkeys)