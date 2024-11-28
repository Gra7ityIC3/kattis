gets
ans, cur = 1, ''
gets.each_char do |c|
  cur << c
  if ans == cur.to_i
    ans += 1
    cur = ''
  end
end
puts ans