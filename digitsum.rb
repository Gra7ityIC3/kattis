def f(x)
  return 0 if x == 0
  d = x % 10
  x /= 10
  d * (d - 1) / 2 + d * x.digits.sum + 10 * f(x) + x * 45
end

gets.to_i.times do
  a, b = gets.split.map(&:to_i)
  puts f(b + 1) - f(a)
end