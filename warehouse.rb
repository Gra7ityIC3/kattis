gets.to_i.times do
  h = Hash.new(0)
  gets.to_i.times do
    name, count = gets.split
    h[name] += count.to_i
  end
  puts h.size
  h.sort_by { |name, count| [-count, name] }.each do |name, count|
    puts "#{name} #{count}"
  end
end