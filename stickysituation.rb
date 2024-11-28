gets
puts gets.split.map(&:to_i).sort!.each_cons(3).any? { |a, b, c| a + b > c } ? 'possible' : 'impossible'