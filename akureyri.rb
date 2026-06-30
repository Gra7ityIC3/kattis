h = Hash.new(0)
gets.to_i.times do
  gets
  h[gets.chomp] += 1
end
h.each { |key, value| puts "#{key} #{value}" }