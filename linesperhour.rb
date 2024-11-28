n, lph = gets.split.map(&:to_i)
sum = cnt = 0
Array.new(n) { gets.to_i }.sort!.each do |loc|
  sum += loc
  break if sum > lph * 5
  cnt += 1
end
puts cnt