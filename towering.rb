*h, x, y = gets.split.map(&:to_i)
h.sort!.reverse!.combination(3).each do |c|
  puts (c << h - c).join(' ') if c.sum == x
end