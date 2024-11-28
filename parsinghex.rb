$<.each do |line|
  line.scan(/0[xX][0-9a-fA-F]+/).each { |h| puts "#{h} #{h.to_i(16)}" }
end