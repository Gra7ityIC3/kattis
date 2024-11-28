s = gets
puts s.scan(/.{#{s.length / 3}}/).sort![1]