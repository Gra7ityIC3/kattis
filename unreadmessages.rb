n, m = gets.split.map(&:to_i)
h, ans = Hash.new(0), 0
(1..m).each do |i|
  s = gets.to_i
  ans += n - i + h[s]
  h[s] = i
  puts ans
end