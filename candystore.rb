n, q = gets.split.map(&:to_i)
h = Hash.new('nobody')
n.times do
  first, last = gets.split
  initials = first[0] + last[0]
  h[initials] = h.key?(initials) ? 'ambiguous' : "#{first} #{last}"
end
q.times { puts h[gets.chomp!] }