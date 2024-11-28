$<.each do |line|
  nums, name = line.split.partition { |x| x.match?(/\d/) }
  puts "#{nums.sum(&:to_f) / nums.size} #{name.join(' ')}"
end