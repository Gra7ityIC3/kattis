gets.to_i.times do |i|
  gets
  puts "Case ##{i + 1}: #{gets.split.map(&:to_i).reduce(:^)}"
end