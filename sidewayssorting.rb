loop do
  r, c = gets.split.map(&:to_i)
  break if r == 0
  puts Array.new(r) { gets.chomp!.chars }
    .transpose.sort_by! { |a| a.map(&:downcase) }
    .transpose.map(&:join), ''
end