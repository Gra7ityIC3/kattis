ax, ay, bx, by, cx, cy, dx, dy = gets.split.map(&:to_i)
puts [Math.hypot(ax - bx, ay - by), Math.hypot(cx - dx, cy - dy)].max