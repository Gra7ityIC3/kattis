l, d, n = gets.split.map(&:to_i)
a = Array.new(n) { gets.to_i } << 6 - d << l - 6 + d
puts a.sort!.each_cons(2).sum { |x, y| (y - x) / d - 1}