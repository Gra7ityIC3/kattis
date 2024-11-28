a, b, c, d = gets.each_char.map { |d| ('%04b' % d.to_i).tr('01', '.*') }
4.times { |i| puts "#{a[i]} #{b[i]}   #{c[i]} #{d[i]}" }