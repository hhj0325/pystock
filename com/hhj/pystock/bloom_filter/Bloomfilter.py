class Bloomfilter(object):
    """
    A Bloom filter is a probabilistic data-structure that trades space for accuracy
    when determining if a value is in a set.  It can tell you if a value was possibly
    added, or if it was definitely not added, but it can't tell you for certain that
    it was added.
    """

    def __init__(self, size):
        """Setup the BF with the appropriate size"""
        self.values = [False] * size
        self.size = size

    def hash_value(self, value):
        """Hash the value provided and scale it to fit the BF size"""
        return hash(value) % self.size

    def add_value(self, value):
        """Add a value to the BF"""
        h = self.hash_value(value)
        self.values[h] = True

    def might_contain(self, value):
        """Check if the value might be in the BF"""
        h = self.hash_value(value)
        return self.values[h]

    def print_contents(self):
        """Dump the contents of the BF for debugging purposes"""
        print(self.values)

    def major_segments(self, s):
        """
        Perform major segmenting on a string.  Split the string by all of the major
        breaks, and return the set of everything found.  The breaks in this implementation
        are single characters, but in Splunk proper they can be multiple characters.
        A set is used because ordering doesn't matter, and duplicates are bad.
        """
        major_breaks = ' '
        last = -1
        results = set()
        # enumerate() will give us (0, s[0]), (1, s[1]), ...
        for idx, ch in enumerate(s):
            if ch in major_breaks:
                segment = s[last + 1:idx]
                results.add(segment)
                last = idx
        # The last character may not be a break so always capture
        # the last segment (which may end up being "", but yolo)
        segment = s[last + 1:]
        results.add(segment)
        return results

    def minor_segments(self, s):
        """
        Perform minor segmenting on a string.  This is like major
        segmenting, except it also captures from the start of the
        input to each break.
        """
        minor_breaks = '_.'
        last = -1
        results = set()
        for idx, ch in enumerate(s):
            if ch in minor_breaks:
                segment = s[last + 1:idx]
                results.add(segment)
                segment = s[:idx]
                results.add(segment)
                last = idx
        segment = s[last + 1:]
        results.add(segment)
        results.add(s)
        return results

    def segments(self, event):
        """Simple wrapper around major_segments / minor_segments"""
        results = set()
        for major in self.major_segments(event):
            for minor in self.minor_segments(major):
                results.add(minor)
        return results


bf = Bloomfilter(10)
# bf.add_value('dog')
# bf.add_value('fish')
# bf.add_value('cat')
# bf.print_contents()
# bf.add_value('bird')
# bf.print_contents()
# # Note: contents are unchanged after adding bird - it collides
# for term in ['dog', 'fish', 'cat', 'bird', 'duck', 'emu']:
#     print('{}: {} {}'.format(term, bf.hash_value(term), bf.might_contain(term)))

for term1 in bf.segments('src_ip = 1.2.3.4'):
        print(term1)

