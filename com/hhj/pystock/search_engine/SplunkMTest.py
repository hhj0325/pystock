from com.hhj.pystock.search_engine.SplunkM import SplunkM

s = SplunkM()
s.add_event('src_ip = 1.2.3.4')
s.add_event('src_ip = 5.6.7.8')
s.add_event('dst_ip = 1.2.3.4')

print('search_all:src_ip, 5.6')
for event in s.search_all(['src_ip', '5.6']):
    print(event)
print('---')

print('search_any:src_ip, dst_ip')
for event in s.search_any(['src_ip', 'dst_ip']):
    print(event)
