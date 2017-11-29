from com.hhj.pystock.search_engine.Bloomfilter import Bloomfilter

bf = Bloomfilter(10)
bf.add_value('dog')
bf.add_value('fish')
bf.add_value('cat')
bf.print_contents()
bf.add_value('bird')
bf.print_contents()
# Note: contents are unchanged after adding bird - it collides
for term in ['dog', 'fish', 'cat', 'bird', 'duck', 'emu']:
    print('{}: {} {}'.format(term, bf.hash_value(term), bf.might_contain(term)))
