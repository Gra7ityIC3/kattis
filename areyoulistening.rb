cx, cy, n = gets.split.map(&:to_i)
puts [Array.new(n) do
  x, y, r = gets.split.map(&:to_i)
  Math.hypot(cx - x, cy - y) - r
end.sort![2].floor, 0].max