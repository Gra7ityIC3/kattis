gets.to_i.times do
  h = Hash.new(0)
  gets.to_i.times { h[gets.split[1]] += 1 }
  ans = 1
  h.values.each { |v| ans *= v + 1 }
  puts ans - 1
end