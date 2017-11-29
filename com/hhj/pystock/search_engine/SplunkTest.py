from com.hhj.pystock.search_engine.Splunk import Splunk

s = Splunk()
s.add_event('src_ip = 1.2.3.4')
s.add_event('src_ip = 5.6.7.8')
s.add_event('dst_ip = 1.2.3.4')
print(s.events)

print('search:1.2.3.4')
for event in s.search('1.2.3.4'):
    print(event)
print('---')

print('search:src_ip')
for event in s.search('src_ip'):
    print(event)
print('---')

print('search:ip')
for event in s.search('ip'):
    print(event)
print('---')