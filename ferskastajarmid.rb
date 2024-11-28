memes = []
gets.to_i.times do
  name, controversiality, coolness = gets.split
  memes << [-controversiality.to_i * coolness.to_i, name]
end
puts memes.sort![0][1]