import random
good_days_count = []
temperatures =[]
count =0

for i in range(0,7):
    temperatures.append(random.randint(26,41))

days_of_the_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday" ,"Friday", "Saturday"]

above_avg = []
for i in range(len(days_of_the_week)):
	if(temperatures[i] % 2 == 0):
		good_days_count.append(days_of_the_week[i])
		print(good_days_count)
		count += 1

#print(count)

#here is the finishing point of part-4


highest_temp = temperatures[0]
lowest_temp = temperatures[0]
highest_temp_day = days_of_the_week[0]
lowest_temp_day = days_of_the_week[0]

for i in range (7):
    if(temperatures[i] > highest_temp):
        highest_temp = temperatures[i]
        highest_temp_day = days_of_the_week[i]

    if(temperatures[i] < lowest_temp):
        lowest_temp = temperatures[i]
        lowest_temp_day = days_of_the_week[i]

sum_temp = sum(temperatures)
ave_temp = sum_temp / 7
for i in range(7):
    if temperatures[i] > ave_temp:
        result = temperatures[i]
        above_avg.append(days_of_the_week[result])

print("Temperatures for the week:", temperatures)
print("Good days for Shelly:", good_days_count)  # This seems to be work in progress, adjust as needed
print("The highest temperature was", highest_temp, "on", highest_temp_day)
print("The lowest temperature was", lowest_temp, "on", lowest_temp_day)
print("The average temperature was", avg_temp)
print("Days with temperatures above the average:", above_avg)

