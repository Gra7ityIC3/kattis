n = gets.to_i
a = b = 0
n.times do |i|
  s = gets.to_i
  a += s * 0.8 ** i
  b += s * (i * 0.8 ** (i - 1) + (n - 1 - i) * 0.8 ** i)
end
puts a / 5, b / 5 / n