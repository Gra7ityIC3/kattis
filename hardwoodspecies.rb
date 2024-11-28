h, n = Hash.new(0), 0
$<.each do |line|
  h[line.chomp!] += 1
  n += 1
end
h.sort.each { |k, v| puts "#{k} #{v * 100.0 / n}" }