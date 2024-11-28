n, p = gets.split.map(&:to_i)
sum = ans = 0
gets.split.map(&:to_i).each do |x|
  sum += x - p
  ans = [ans, sum].max
  sum = 0 if sum < 0
end
puts ans