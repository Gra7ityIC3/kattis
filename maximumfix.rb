n = gets.to_i
h = Hash.new(0)
gets.split.map(&:to_i).each.with_index(1) { |x, i| h[x > i ? n - x + i : i - x] += 1 }
puts h.max_by { |k, v| [v, -k]}.join(' ')