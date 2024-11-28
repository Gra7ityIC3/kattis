n, m = gets.split.map(&:to_i)
p = (1..n).to_a
m.times do
  a = gets.to_i
  p[a - 1], p[a] = p[a], p[a - 1]
end
puts p