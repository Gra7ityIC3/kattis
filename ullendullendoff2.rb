n = gets.to_i
ans = Array.new(n) { gets }
ans[0], ans[12 % n] = ans[12 % n], ans[0]
puts ans