from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = True

def find_highest_bidder(bid_record):
  max_bid = 0
  user_won = ""
  for key in bid_record:
    if bid_record[key] > max_bid:
      max_bid = bid_record[key]
      user_won = key
  print(f"\nCongratulations {user_won}! You won the bid with ${max_bid}.")

while bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no' ")
  if should_continue == "no":
    bidding_finished = False
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
