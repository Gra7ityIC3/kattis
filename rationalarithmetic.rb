gets.to_i.times do
  x1, y1, op, x2, y2 = gets.split
  x1, y1, x2, y2 = x1.to_i, y1.to_i, x2.to_i, y2.to_i
  a, b = case op
  when '+' then [x1 * y2 + x2 * y1, y1 * y2]
  when '-' then [x1 * y2 - x2 * y1, y1 * y2]
  when '*' then [x1 * x2, y1 * y2]
  else [x1 * y2, y1 * x2]
  end
  a, b = -a, -b if b < 0
  d = a.gcd(b)
  puts "#{a / d} / #{b / d}"
end