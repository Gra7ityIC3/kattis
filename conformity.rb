h = Hash.new(0)
gets.to_i.times { h[gets.split.map(&:to_i).sort!] += 1 }
puts h.values.count(max = h.values.max) * max