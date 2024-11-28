xg, yg, xd, yd = gets.split.map(&:to_f)
$<.each do |line|
  x, y = line.split.map(&:to_f)
  if 2 * Math.hypot(x - xg, y - yg) < Math.hypot(x - xd, y - yd)
    puts "The gopher can escape through the hole at (#{x},#{y})."
    exit
  end
end
puts 'The gopher cannot escape.'