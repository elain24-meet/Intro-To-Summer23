import random
good_days_count = []
temperatures = list(random.random(26,41))
days_of_the_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday" ,"Friday", "Saturday"]
for i in range(len(days_of_the_week)):
	if(temperatures[i] % 2 == 0):
		good_days_count.append(days_of_the_week)
		print(good_days_count)
		count += 1

print(count)
