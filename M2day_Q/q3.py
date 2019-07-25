'''3.	Write a program to determine the work hours of the day entered based on the timetable provided below.

Mon	Tue	Wed	Thu	Fri	Sat	Sun
3	3	3	3	3	3	0
2	2	2	2	2	1	0
2	2	2	1	1	0	0
	
Example:
Input: Thu
		Output: [3,2,1]
	
Input: Sat
Output: [3,1,0]

'''
day={'Mon':[3,2,2],'Tue':[3,2,2],'Wed':[3,2,2],'Thu':[3,2,1],'Fri':[3,2,1],'Sat':[3,1,0],'Sun':[0,0,0]}
days=input('Enter the day:')
print(day[days])