#!/usr/bin/env ruby
# Aregular expression matching a specific pattern
puts ARGV[0].scan(/^\d{10}/).join
