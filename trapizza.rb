d, a, b, h = $<.map(&:to_f)
puts ['Jafn storar!', 'Mahjong!', 'Trapizza!'][Math::PI * (d / 2) ** 2 <=> (a + b) * h / 2]