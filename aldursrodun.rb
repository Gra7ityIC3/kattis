gets
gets.split.map(&:to_i).permutation.find(lambda { puts 'Neibb' }) do |p|
  if p.each_cons(2).all? { |a, b| a.gcd(b) > 1 }
    puts p.join(' ')
    break
  end
end