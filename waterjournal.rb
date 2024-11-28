n, a, b = gets.split.map(&:to_i)
min, max = Array.new(n - 1) { gets.to_i }.minmax
if a == min && b == max
  puts *(a..b)
elsif a == min
  puts b
elsif b == max
  puts a
else
  puts -1
end