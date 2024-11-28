n = gets.to_i
a = gets.split.map(&:to_i)
t = gets.split.map(&:to_i)
p = gets.split.map(&:to_i)
if a.sum > 2 * a[p[0] - 1]
  puts 1, p.rotate!.join(' ')
else
  puts n == 2 ? 0.25 : 0.5, p.join(' ')
end