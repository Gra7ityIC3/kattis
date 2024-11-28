require 'prime'

while true
  p, a = gets.split.map(&:to_i)
  break if p == 0
  puts !p.prime? && a.pow(p, p) == a ? 'yes' : 'no'
end