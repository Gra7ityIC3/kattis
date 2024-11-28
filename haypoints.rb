m, n = gets.split.map(&:to_i)
h = Hash[Array.new(m) { gets.split }]
n.times do
  ans = 0
  while (line = gets) != ".\n"
    ans += line.split.sum { |word| h[word].to_i }
  end
  puts ans
end