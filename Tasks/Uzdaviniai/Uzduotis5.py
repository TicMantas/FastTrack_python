shoe_prices = [8.90, 4.90, 13.20, 8.80, 14.00, 12.00]
budget = 20


sorted_prices = sorted(shoe_prices)
print(sorted_prices)
cheapest_pair = sorted_prices[:2]
print(cheapest_pair)
remaining_after_cheapest = budget - sum(cheapest_pair)
print(f'Money Left :  {remaining_after_cheapest:.2f}$')

best_pair = None
least_remaining = budget

for i in range(len(shoe_prices)):
    for shoes in range(i + 1, len(shoe_prices)):
        total_cost = shoe_prices[i] + shoe_prices[shoes]
        remaining = budget - total_cost

        if 0 <= remaining < least_remaining:
            least_remaining = remaining
            best_pair = (shoe_prices[i], shoe_prices[shoes])


print(f"a) Cheapest shoes: {cheapest_pair}, Remaining money: €{remaining_after_cheapest:.2f}$")
print(f"b) Best pair within budget: {best_pair}, Remaining money: €{least_remaining:.2f}$")
