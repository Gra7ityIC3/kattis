gets
puts $<.each_cons(2).count { |a, b| a == b }