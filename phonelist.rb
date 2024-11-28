gets.to_i.times do
  a = Array.new(gets.to_i) { gets.chomp! }.sort!
  puts a.each_cons(2).any? { |a, b| b.start_with?(a) } ? 'NO' : 'YES'
end