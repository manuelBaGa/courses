'''
Scenario
Create a class representing a time interval;
the class should implement its own method for addition, subtraction on time interval class objects;
the class should implement its own method for multiplication of time interval class objects by an integer-type value;
the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
check the argument type, and in case of a mismatch, raise a TypeError exception.

HINT:

->just before doing the math, convert each time interval to a corresponding number of seconds to simplify the algorithm;
for addition and subtraction, you can use one internal method, as subtraction is just ... negative addition.

-> you can use the assert statement to validate if the output of the __str__ method applied to a time interval object equals the expected value.

Test data:

the first time interval (fti) is hours=21, minutes=58, seconds=50
the second time interval (sti) is hours=1, minutes=45, seconds=22
the expected result of addition (fti + sti) is 23:44:12
the expected result of subtraction (fti - sti) is 20:13:28
the expected result of multiplication (fti * 2) is 43:57:40

'''
class my_time():
    def __init__(self, hours, minutes, seconds) -> None:
        self.hour=hours
        self.minute=minutes
        self.second=seconds
        self.total_sec = self.hour*3600 + self.minute*60 + self.second

    def __sec2timeobj__(self,total_seconds):
        hours = total_seconds//3600
        minutes = (total_seconds - hours*3600)//60
        seconds = total_seconds - hours*3600 - minutes*60
        return f'{hours}:{minutes}:{seconds}'

    def __add__(self, time_ob):
        if type(time_ob) == int:
            sum_tot_sec = self.total_sec + time_ob
        else:
            sum_tot_sec = self.total_sec + time_ob.total_sec
        return my_time.__sec2timeobj__(self,sum_tot_sec)
    
    def __sub__(self, time_ob):
        if type(time_ob) == int:
            subs_tot_sec = self.total_sec - time_ob
        else:
            subs_tot_sec = self.total_sec - time_ob.total_sec
        return my_time.__sec2timeobj__(self,subs_tot_sec)
    
    def __mul__(self, multiplier):
        mul_tot_sec = self.total_sec*multiplier
        return my_time.__sec2timeobj__(self,mul_tot_sec)

fti = my_time(hours=21, minutes=58, seconds=50)
sti = my_time(hours=1, minutes=45, seconds=22)
tti = my_time(21,58,50)

assert fti+sti == "23:44:12"
assert fti-sti == "20:13:28"
assert fti*2 == "43:57:40"
assert tti+62 == "21:59:52"
assert tti-62 == "21:57:48"