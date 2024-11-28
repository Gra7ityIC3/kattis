h = Hash.new(0)
gets.to_i.times { h[gets] += 1 }
m = h.values.min
puts h.select { |k, v| v == m }.keys.sort