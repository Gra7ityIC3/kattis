h = Hash.new('eh')
$<.each do |line|
  break if line.length == 1
  a, b = line.split
  h[b] = a
end
$<.each { |line| puts h[line.chomp!] }