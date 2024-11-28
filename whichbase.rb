gets.to_i.times do
  k, s = gets.split
  puts "#{k} #{s =~ /[89]/ ? 0 : s.to_i(8)} #{s.to_i} #{s.to_i(16)}"
end