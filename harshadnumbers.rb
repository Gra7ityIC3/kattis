n = gets.to_i
n += 1 until n % n.digits.sum == 0
puts n