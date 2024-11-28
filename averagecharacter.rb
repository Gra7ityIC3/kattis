s = gets.chomp!
puts (s.each_byte.sum / s.length).chr