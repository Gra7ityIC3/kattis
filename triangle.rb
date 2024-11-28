$<.each_with_index do |line, i|
  n = line.to_i
  puts "Case #{i + 1}: #{Math.log10(3 ** (n + 1) >> n).to_i + 1}"
end