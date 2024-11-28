ans = %w[keys phone wallet]
gets.to_i.times { ans.delete(gets.chomp!) }
puts ans.empty? ? 'ready' : ans