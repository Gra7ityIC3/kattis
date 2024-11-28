a, b, c, d = gets.split.map(&:to_i)
k = c.lcm(d)
puts b / k - (a - 1) / k