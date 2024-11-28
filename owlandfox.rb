gets.to_i.times do
  n = gets.to_i
  sum = n.digits.sum
  n -= 1 until n.digits.sum + 1 == sum
  puts n
end