m, n = gets.split.map(&:to_i)
d = m.gcd(n)
m /= d
n /= d
puts m.odd? && n.odd? ? d : 0