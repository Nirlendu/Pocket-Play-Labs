import re
import operator
#import sys


class logFile_parser(object):

    def __init__(self):
        self.get_users =  { 
                                'count' : 0,
                                'dict_dyno' : {},
                                'time_array' : []
                                }
        self.post_users =  { 
                                'count' : 0,
                                'dict_dyno' : {},
                                'time_array' : []
                                }
        self.get_friends_score =  { 
                                'count' : 0,
                                'dict_dyno' : {},
                                'time_array' : []
                                }
        self.get_friends_progress =  { 
                                'count' : 0,
                                'dict_dyno' : {},
                                'time_array' : []
                                }
        self.get_messages =  { 
                                'count' : 0,
                                'dict_dyno' : {},
                                'time_array' : []
                                }
        self.count_pending_messages = { 
                                'count' : 0,
                                'dict_dyno' : {},
                                'time_array' : []
                                }


    def calc_mode(self, time_array):
        """
        Calculates the mode
        """
        time_array.sort()
        x= 1
        count = 0
        while x <= len(time_array):
            count = count+1
            x = 2*x
        count = count - 1
        while count > 0:
            p = 1
            while p*(2**count)<=len(time_array):
                try:
                    if time_array[p*(2**count)] == time_array[(p+1)*(2**count)]:
                        return time_array[p*(2**count)]
                except:
                    break
                p = p + 1
            count = count - 1
        try:
            return time_array[0]
        except:
            pass


    def calc_mean(self, time_array):
        """
        Calculates mean
        """
        total_time = 0
        for i in time_array:
            total_time = total_time + i
        try:
            return float(total_time)/float(len(time_array))
        except:
            pass


    def calc_median(self, time_array):
        """
        Calculates median
        """
        #return 6
        if len(time_array)%2:
            return float(time_array[(len(time_array))/2])
        else:
            try:
                return float(time_array[(len(time_array)/2)-1] + time_array[(len(time_array)/2)])/float(2)
            except:
                pass


    def dyno(self, dictionary):
        try:
            return max(dictionary.iteritems(), key = operator.itemgetter(1))[0]
        except:
            return None


    def calc_stats(self, dictionary):
        """
        Calls mean, median and mode
        """
        print 'Count is ' + str(dictionary['count'])
        print 'Mean is ' + str(self.calc_mean(dictionary['time_array']))
        print 'Median is ' + str(self.calc_median(dictionary['time_array']))
        print 'Mode is ' + str(self.calc_mode(dictionary['time_array']))
        print 'Dyno that responded most is ' + str(self.dyno(dictionary['dict_dyno'])) + '\n'


    def url_valid(self,url):
        if re.match('GET/api/users/[0-9]*/count_pending_messages', url) or re.match('GET/api/users/[0-9]+/get_messages', url) or re.match('GET/api/users/[0-9]+/get_friends_progress', url) or re.match('GET/api/users/[0-9]+/get_friends_score', url) or re.match('POST/api/users/[0-9]+', url) or re.match('GET/api/users/[0-9]+', url):
            return 1
        return 0


    def create_dict(self, url, dyno, total_time):
        if re.match('GET/api/users/[0-9]*/count_pending_messages', url):
            self.count_pending_messages = self.store_data(self.count_pending_messages, dyno, total_time)
            return
        if re.match('GET/api/users/[0-9]+/get_messages', url):
            self.get_messages = self.store_data(self.get_messages, dyno, total_time)
            return
        if re.match('GET/api/users/[0-9]+/get_friends_progress', url):
            self.get_friends_progress = self.store_data(self.get_friends_progress ,dyno, total_time)
            return
        if re.match('GET/api/users/[0-9]+/get_friends_score', url):
            self.get_friends_score = self.store_data(self.get_friends_score, dyno, total_time)
            return
        if re.match('POST/api/users/[0-9]+', url):
            self.post_users = self.store_data(self.post_users ,dyno, total_time)
            return
        if re.match('GET/api/users/[0-9]+', url):
            self.get_users = self.store_data(self.get_users, dyno, total_time)
            return


    def store_data(self, ref_dict, dyno, total_time):
        ref_dict['count'] += 1
        if ref_dict['dict_dyno'].has_key(dyno):
            ref_dict['dict_dyno'][dyno] += 1
        else:
            ref_dict['dict_dyno'][dyno] = 1
        ref_dict['time_array'].append(total_time)
        return ref_dict


    def calculate(self):
        print 'Data for GET/api/users/{user_id}/count_pending_messages :'
        self.calc_stats(self.count_pending_messages)
        print 'Data for GET/api/users/{user_id}/get_messages :'
        self.calc_stats(self.get_messages)
        print 'Data for GET/api/users/{user_id}/get_friends_progress :'
        self.calc_stats(self.get_friends_progress)
        print 'Data for GET/api/users/{user_id}/get_friends_score :'
        self.calc_stats(self.get_friends_score)
        print 'Data for POST/api/users/{user_id} :'
        self.calc_stats(self.post_users)
        print 'Data for GET/api/users/{user_id} :'
        self.calc_stats(self.get_users)


    def parse(self, fileName):
        f = open(fileName)
        string = f.read()
        newLineSplit=string.split('\n')
        for i in newLineSplit:
            i = str(i)
            if i == '' or i == '\n':
                continue
            url_begin = i.find('path')
            url_end = i.find('host')
            url = i[url_begin + 5: url_end - 1]
            method_begin = i.find('method')
            method = i[method_begin + 7 : url_begin - 1]
            url = method + url
            if not self.url_valid(url):
                continue
            dyno_begin = i.find('dyno')
            if dyno_begin == -1:
                continue
            connectTime_begin = i.find('connect')
            if connectTime_begin == -1:
                continue
            dyno = i[dyno_begin+5:connectTime_begin-1]
            connect_ms_position = i.find('ms')
            try:
                connectTime = int(i[connectTime_begin+8:connect_ms_position])
            except:
                connectTime = 0
            serviceTime_begin = i.find('service=')
            if serviceTime_begin == -1:
                continue
            service_ms_position = i[serviceTime_begin:].find('ms')
            try:
                serviceTime = int(i[serviceTime_begin + 8 : serviceTime_begin + service_ms_position])
            except:
                serviceTime = 0
            self.create_dict(url, dyno , serviceTime + connectTime)
        self.calculate()


x = logFile_parser()
x.parse(str(sys.argv[1]))