gets.to_i.times do
  puts gets.split.map(&:to_i).each_cons(2).sum { |x, y| [0, y - 2 * x].max }
end