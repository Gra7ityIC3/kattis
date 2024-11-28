n, d = gets.split.map(&:to_i)
freq = Hash.new(0)
gets.split.map(&:to_i).each { |a| freq[a / d] += 1 }
puts freq.values.sum { |v| v * (v - 1) / 2 }