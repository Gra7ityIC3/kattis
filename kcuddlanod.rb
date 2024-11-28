n, m = gets.split.map { |x| x.tr('25', '52').reverse.to_i }
puts n > m ? 1 : 2