a, b = gets.split('/').map(&:to_i)
a, b = 5 * a - 160 * b, 9 * b
d = a.gcd(b)
puts "#{a / d}/#{b / d}"