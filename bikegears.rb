gets
gets.split.map(&:to_i).product(gets.split.map(&:to_i)).sort do |(f1, b1), (f2, b2)|
  f1 * b2 == f2 * b1 ? f1 <=> f2 : f1 * b2 <=> f2 * b1
end.each do |f, b|
  puts "(#{f},#{b})"
end