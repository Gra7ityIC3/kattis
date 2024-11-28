while (n = gets.to_i) != 0
  puts Array.new(n) { gets }.sort_by { |a| a[0, 2] }, ''
end