p, t = gets.split.map(&:to_i)
a = Array.new(p, 0)
$<.each do |line|
  i, j = line.split.map(&:to_i)
  a[i - 1] += 2 ** j
end
puts a.uniq.size