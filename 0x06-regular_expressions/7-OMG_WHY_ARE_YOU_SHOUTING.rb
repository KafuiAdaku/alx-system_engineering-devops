#!/usr/bin/env ruby
# A regular expression matchin only caps
puts ARGV[0].scan(/[A-Z]+/).join(",")
