n = gets.to_i
ans = []
(1..Integer.sqrt(n)).each do |i|
  ans << i - 1 << n / i - 1 if n % i == 0
end
ans.pop if ans[-1] == ans[-2]
puts ans.sort!.join(' ')