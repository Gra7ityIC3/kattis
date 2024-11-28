gets.to_i.times do
  m, *a = gets.split.map(&:to_i)
  if a.each_cons(2).map { |a, b| b - a }.uniq.size == 1
    puts 'arithmetic'
  elsif a.sort!.each_cons(2).map { |a, b| b - a }.uniq.size == 1
    puts 'permuted arithmetic'
  else
    puts 'non-arithmetic'
  end
end