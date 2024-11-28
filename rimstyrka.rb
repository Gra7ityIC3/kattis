def r(s, t)
  (0...[s.length, t.length].min).find { |i| s[i] != t[i] } || 0
end

ans = 0
Array.new(gets.to_i) { gets.chomp!.reverse }.sort!.each_cons(2) do |s, t|
  ans = [ans, r(s, t)].max
end
puts ans