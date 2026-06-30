ans = gets.split.map do |s|
  if s.match?(/[a-zA-Z]/) && s.match?(/\d/)
    '*' * s.length
  else
    s
  end
end
puts ans.join(' ')