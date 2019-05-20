import os
import texttable
import time
import math

##print(datetime.date.timetuple())
####print(time.ctime())


class TimeMetric:
    def __init__(self, time_zone):
        self.time_zone = time_zone

    def grab_time(self, time_range, time_input):
        y = 0
        if type(time_range) is int:
            y = math.floor(time_input % time_range)

        elif len(time_range) == 2:
            if time_range[0] > time_range[1]:
                time_range = [time_range[1], time_range[0]]

            time_min = time_range[0]
            time_max = time_range[1]

            y = math.floor((time_input % time_max - time_input % time_min) / time_min)

        else:
            input('Incorrect time range')
            return None

        return y

    def show_time(self):
        day_time = time.time()
        day_time += self.time_zone * 60 * 60
        day_time = day_time % (60 * 60 * 24)

        day_10_hours = day_time / 24 * 10 / 60 / 60 * 100 * 100

        godzina = self.grab_time([60*60, 60*60*24],day_time)
        minuty = self.grab_time([60,60*60],day_time)
        sekundy = self.grab_time(60,day_time)
        text_normal_time = '{0}h :{1}m :{2}s'.format(godzina, minuty, sekundy)

        godzina = self.grab_time([100 * 100, 60*60*24], day_time)
        minuty = self.grab_time([100, 100 * 100], day_time)
        sekundy = self.grab_time(100, day_time)
        text_decimal_standard_sec = '{0}h :{1}m :{2}s'.format(godzina, minuty, sekundy)

        godzina = self.grab_time([100 * 100, 100 * 100 * 10], day_10_hours)
        minuty = self.grab_time([100, 100 * 100], day_10_hours)
        sekundy = self.grab_time(100, day_10_hours)
        text_decimal_10h = '{0}h :{1}m :{2}s'.format(godzina, minuty, sekundy)

        beats = math.floor((day_10_hours / 100)%1000)
        text_beat = '{0}'.format(str(beats))

        table = texttable.Texttable()
        table.header(['Normal Time\n (timezone:{0})'.format(str(self.time_zone)), 'Decimal Minute\n(standard sec)',
                      'Decimal Day\n(10h clock)', 'Swatch Internet Time\n(.beats)'])
        table.add_row([text_normal_time, text_decimal_standard_sec, text_decimal_10h, text_beat])
        table.set_cols_align(['c', 'c', 'c', 'c'])
        table.set_cols_width([15, 15, 15, 20])
        print(table.draw())

app = TimeMetric(1)
time_0 = math.floor(time.time())
while True:
    os.system('cls')
    app.show_time()
    print('Watch enabled for: {0}s'.format(math.floor(time.time()-time_0)))
    time.sleep(0.1)
    
