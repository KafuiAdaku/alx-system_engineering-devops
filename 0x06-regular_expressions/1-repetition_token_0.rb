#!/usr/bin/env ruby
# A regular expression to match repetition in words
puts ARGV[0].scan(/hbt{2,5}n/).join
