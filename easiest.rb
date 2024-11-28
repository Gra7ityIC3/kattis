while (n = gets.to_i) != 0
  p, q = 11, n.digits.sum
  p += 1 until (n * p).digits.sum == q
  puts p
end