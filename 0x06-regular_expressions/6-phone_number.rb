#!/usr/bin/env ruby
# Aregular expression matching a specific pattern
puts ARGV[0].scan(/^[0-9]{10}$/).join
