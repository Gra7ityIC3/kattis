res = 1
gets.to_i.times do
  a, op, b = gets.split
  a, b = a.to_i, b.to_i
  res = case op
  when '+' then a + b - res
  when '-' then (a - b) * res
  when '*' then (a * b) ** 2
  else (a + 1) / 2
  end
  puts res
end