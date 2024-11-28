names, h = [], Hash.new(1)
$<.each do |line|
  first, last = line.split
  names << [last, first]
  h[first] ^= 1
end
names.sort!.each do |last, first|
  puts "#{first} #{last * h[first]}"
end