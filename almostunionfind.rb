MAX_N = 200001

$parent = Array.new(MAX_N)
$size = Array.new(MAX_N)
$sum = Array.new(MAX_N)

def find(x)
  $parent[x] == x ? x : $parent[x] = find($parent[x])
end

def union(x, y)
  x, y = find(x), find(y)
  return if x == y
  x, y = y, x if $size[x] < $size[y]
  $parent[y] = x
  $size[x] += $size[y]
  $sum[x] += $sum[y]
end

def move(x, y)
  rx, ry = find(x), find(y)
  return if rx == ry
  $size[rx] -= 1
  $size[ry] += 1
  $sum[rx] -= x
  $sum[ry] += x
  $parent[x] = ry
end

while gets
  n, m = $_.split.map(&:to_i)
  (1..n).each do |i|
    j = n + i
    $parent[i] = $parent[j] = j
    $size[j] = 1
    $sum[j] = i
  end
  m.times do
    op, p, q = gets.split.map(&:to_i)
    case op
    when 1 then union(p, q)
    when 2 then move(p, q)
    else puts "#{$size[find(p)]} #{$sum[find(p)]}"
    end
  end
end