$<.each do |line|
  puts line.split.map(&:to_i).reduce(:lcm)
end