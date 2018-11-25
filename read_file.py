#-*- coding: UTF-8 -*-
import numpy as np
import time
import someclass

def read_file(filename, file_type):
    #service_type is boolean, true means outbound, false means inbound

    customer=[]

    # customer_ID_out = []
    # on_GPS_out = []
    # off_longitude = []
    # off_latitude = []

    with open(filename, 'r') as file_to_read:

        # j = 1  # 用于添加用户ID
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if not lines:
                break
                pass

            # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            carNO_tmp, on_time_tmp, on_GPS_tmp, on_difference_tmp, on_longitude_tmp, on_latitude_tmp, off_time_tmp, off_GPS_tmp, off_difference_tmp, off_longitude_tmp, off_latitude_tmp, distance_tmp = [
                i for i in lines.split( ',' )]

            if (file_type == True):
                off_lo = float( off_longitude_tmp )
                off_la = float( off_latitude_tmp )
                position=np.array([off_lo,off_la])
                id='O_' + on_GPS_tmp[11:13] + on_GPS_tmp[14:16] + on_GPS_tmp[17:19]

            else:
                # r.service_type = False
                on_lo = float( on_longitude_tmp )
                on_la = float( on_latitude_tmp )
                position=np.array([on_lo,on_la])
                id='I_'+ on_GPS_tmp[11:13] + on_GPS_tmp[14:16] + on_GPS_tmp[17:19]

            if(110<position[0]<120) and (20<position[1]<25):
                timeArray = time.strptime( on_GPS_tmp[0:19], "%Y-%m-%dT%H:%M:%S" )
                timestamp = time.mktime( timeArray )
                r=someclass.Demand(id,position,file_type,timestamp)
                if len(customer)!=0:
                    r.update_distance_dictionary(customer)

                # 时间字符串-->时间戳数据

                customer.append(r)
    return customer

