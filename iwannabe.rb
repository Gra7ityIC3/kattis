require 'set'

n, k = gets.split.map(&:to_i)
pokenoms = Array.new(n) { gets.split.map(&:to_i) }
set = Set.new()
3.times do |i|
  pokenoms.sort_by! { |x| -x[i] }
  k.times { |i| set.add(pokenoms[i]) }
end
puts set.size