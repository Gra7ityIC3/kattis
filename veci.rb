x = gets.to_i
puts x.digits.permutation.map { |p| p.join.to_i }.sort!.find { |y| y > x } || 0