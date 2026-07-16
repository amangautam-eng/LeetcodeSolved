# Write your MySQL query statement below


with heavymeeting as
(select employee_id,week(meeting_date,0) as week,year(meeting_date),sum(duration_hours) as work
from meetings
group by employee_id,week(meeting_date,1),year(meeting_date)
having sum(duration_hours)>20)

select t1.employee_id,t2.employee_name,t2.department,t1.meeting_heavy_weeks
from (select employee_id,count(work) as meeting_heavy_weeks 
        from heavymeeting
        group by employee_id
        having count(week)>=2
        order by count(week) desc) as t1

left join employees as t2
on t1.employee_id=t2.employee_id
order by t1.meeting_heavy_weeks desc,t2.employee_name 

