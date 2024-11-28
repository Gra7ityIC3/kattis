h = Hash.new(0)
gets.to_i.times do
  s, a = gets.split
  h[s] += a.to_i
end
puts h.max_by(&:last)[0]