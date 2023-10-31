#!/usr/bin/env ruby
def match_phone_number(input)
  regex = /^\d{10}$/
  if input.match?(regex)
    puts "The string '#{input}' is a valid 10-digit phone number!"
  else
    puts "The string '#{input}' is not a valid 10-digit phone number."
  end
end

# Accepting user input as argument
argument = ARGV[0]

# Calling the method with the provided argument
match_phone_number(argument)
