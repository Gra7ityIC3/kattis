r, c = gets.split.map(&:to_i)
w = Array.new(r + 2) { gets.split.map(&:to_i) }
e = [[0] * c, *Array.new(r + 1) { [135] * c }]
loop do
  ne = e.map(&:clone)
  (1..r + 1).each do |i|
    (0...c).each do |j|
      ne[i][j] = [0, [ne[i][j], e[i + 1][j] + w[i][j]].min].max if i < r + 1
      ne[i][j] = [0, [ne[i][j], e[i - 1][j] + w[i][j]].min].max
      ne[i][j] = [0, [ne[i][j], e[i][j + 1] + w[i][j]].min].max if j < c - 1
      ne[i][j] = [0, [ne[i][j], e[i][j - 1] + w[i][j]].min].max if j > 0
    end
  end
  break if e == ne
  e = ne
end
puts e[-1].min