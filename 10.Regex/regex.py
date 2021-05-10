import re

if __name__ == "__main__":

    pattern = re.compile('\/dev\/sd..+')

    df = '''
udev            1005887    642  1005245    1% /dev
tmpfs           1008584    704  1007880    1% /run
/dev/sda2        305216  17183   288033    6% /
none            1008584      2  1008582    1% /sys/fs/cgroup
none            1008584      3  1008581    1% /run/lock
none            1008584     91  1008493    1% /run/shm
none            1008584     31  1008553    1% /run/user
/dev/sda1         97536    309    97227    1% /boot
/dev/sda5       1811520 362336  1449184   21% /usr
/dev/sda7        329968     25   329943    1% /tmp
/dev/sda8        264000  14697   249303    6% /var
/dev/sda3      22446080 959030 21487050    5% /home
/dev/sda6      19931136  36284 19894852    1% /opt
'''

    x = re.findall(pattern, df)

    for item in x:
        result = item.split()
        print(f'Match ---> {result[0]} {result[1]} {result[3]} {result[5]}')

    print('--- ---')