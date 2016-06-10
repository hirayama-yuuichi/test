import sched, time

s = sched.scheduler(time.time, time.sleep)

def print_time(a='default'):
     print("From print_time", time.time(), a)


def print_some_times():
     print(time.time())
     s.enter(10, 1, print_time)
     s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
     s.enter(5, 2, print_time, argument=('positional',))
     s.run()
     print(time.time())

#print_some_times()



def print_some_times2():
     print(time.time())
     s.enter(10, 1, print_time)
     s.run()
     print(time.time())
     s.enter(10, 1, print_time)
     s.run()
     print(time.time())



#print_some_times2()
from datetime import timedelta
import datetime
#a=datetime.datetime(2016,1,13,9,00)
#a+timedelta(seconds=5*60)


start_date_time=datetime.datetime(2016,1,13,9,00)
delta=5
time_count=150

exic_timeing=set(start_date_time+timedelta(seconds=tm*60) for tm in range( 0,time_count,delta) )
print(exic_timeing)


