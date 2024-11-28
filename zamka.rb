l, d, x = $<.map(&:to_i)
puts (l..d).find { |n| n.digits.sum == x }, d.downto(l).find { |m| m.digits.sum == x }