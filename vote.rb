gets.to_i.times do
  votes = (1..gets.to_i).map { |i| [gets.to_i, i] }.sort
  if 2 * votes[-1][0] > votes.sum(&:first)
    puts "majority winner #{votes[-1][1]}"
  elsif votes[-1][0] == votes[-2][0]
    puts "no winner"
  else
    puts "minority winner #{votes[-1][1]}"
  end
end