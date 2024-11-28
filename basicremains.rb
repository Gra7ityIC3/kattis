while true
  b, p, m = gets.split
  break if b == '0'
  b = b.to_i
  p = p.to_i(b)
  m = m.to_i(b)
  puts (p % m).to_s(b)
end