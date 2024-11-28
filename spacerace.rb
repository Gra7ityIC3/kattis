gets
gets
puts $<.map(&:split).min_by { |a| a[2].to_f }[0]