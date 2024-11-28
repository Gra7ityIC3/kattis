u = Array.new(gets.to_i) { gets }
s = u.sort
puts u == s ? 'INCREASING' : u == s.reverse ? 'DECREASING' : 'NEITHER'