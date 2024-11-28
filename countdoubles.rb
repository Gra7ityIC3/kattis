n, m, *a = $<.read.split.map(&:to_i)
puts (0..n-m).count { |i| a[i, m].count(&:even?) >= 2 }