require 'set'

n, t = gets.split.map(&:to_i)
a = gets.split.map(&:to_i)
case t
when 1
  set = Set.new
  puts a.any? { |x| set.include?(7777 - x) || !set.add(x) } ? 'Yes' : 'No'
when 2
  puts a.uniq.size == n ? 'Unique' : 'Contains duplicate'
when 3
  h = Hash.new(0)
  puts a.find { |x| (h[x] += 1) > n / 2 } || -1
when 4
  a.sort!
  puts n.odd? ? a[n / 2] : "#{a[n / 2 - 1]} #{a[n / 2]}"
else
  puts a.sort!.select { |x| x.between?(100, 999) }.join(' ')
end