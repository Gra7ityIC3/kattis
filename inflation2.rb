n = gets.to_i
sum = inflation = 0
freq = Hash.new(0)
gets.split.map(&:to_i).each do |p|
  sum += p
  freq[p] += 1
end

gets.to_i.times do
  s, x, y = gets.split
  x = x.to_i
  if s == 'INFLATION'
    inflation += x
    sum += n * x
  else
    y = y.to_i
    count = freq[x - inflation]
    freq[x - inflation] = 0
    freq[y - inflation] += count
    sum += count * (y - x)
  end
  puts sum
end