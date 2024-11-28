s, d = gets.split
puts ("%0#{s.size}b" % (s.reverse.tr('AB', '01').to_i(2) + d.to_i)).reverse.tr('01', 'AB')