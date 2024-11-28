gets.split.each do |word|
  key = word.chars.map(&:ord).reduce(:gcd)
  puts key
  puts word.chars.map { |c| (c.ord / key).to_s(3) }.join(' ')
end