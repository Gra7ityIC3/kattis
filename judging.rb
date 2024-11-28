n = gets.to_i
h1 = Array.new(n) { gets }.tally
h2 = Array.new(n) { gets }.tally
puts h1.sum { |k, v| [v, h2[k] || 0].min }