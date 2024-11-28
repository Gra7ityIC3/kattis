while (n = gets.to_i) != 0
  a = Array.new(n) { gets.to_i }
  b = Array.new(n) { gets.to_i }
  h = Hash[a.sort.zip(b.sort!)]
  a.each { |x| puts h[x] }
  puts
end