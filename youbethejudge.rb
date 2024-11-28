require 'prime'

puts (a, b, c = $<.read.split.map { |x| x =~ /^[1-9]\d*/ ? x.to_i : 0 }).size == 3 &&
      a.even? && 3 < a && a <= 10 ** 9 &&
      a == b + c && b.prime? && c.prime? ? 1 : 0