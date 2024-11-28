n, a, b = gets.to_i, gets, gets
puts "Deletion #{a == (n.odd? ? b.tr('01', '10') : b) ? 'succeeded' : 'failed'}"