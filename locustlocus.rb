ans = 1 << 30
gets.to_i.times do
  y, c1, c2 = gets.split.map(&:to_i)
  ans = [ans, y + c1.lcm(c2)].min
end
puts ans