## Getting Admin ractf Writeup

| Problem Description | Points |
| ------------------- | ------ |
| See if you can get an admin account. | 300 |

Hey, this is my writeup about getting admin challenge on ractf. I like this challenge even though the challenge is simple, we will get 300 points after solve this challenge and our goal is login as admin. Okay, the challenge is running at 95.216.233.106:21805. as we know from previous challenge, there is a sql injection vulnerablity on the login page. We can bypass the login page and get into one of the user, after get the user i did some enumeration. While i checked the cookie, i knew the cookie is jwt(javascript web token) 

![](images/1.png)

| The Cookie | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjogIkhhcnJ5IiwgInByaXZpbGVnZSI6IDF9.A7OHDo-b3PB5XONTRuTYq6jm2Ab8iaT353oc-VPPNMU |

So, i tried to decode the cookie with jwt.io and got this.

![](images/2.png)

Based on picture we are in user Harry, so we must change harry to admin. I decided to search the secret key of jwt but i have no luck and i tried to sql injection the login form again using union select but before that i must order the column first. So i used this payload to search the column.

> admin' order by 1 -- 

You have to add 1 while the payload successfully executed until you get internal server error. After i did it i knew there is only 3 columns, so i use union select.

> admin' union select 1,2,3 -- 

After i launched the payload, i can login like ussualy but there is weird with the jwt cookie when i decode the jwt cookie harry user changed into 1 and i guess our sql injection payload was successfull launched.

![](images/3.png)

So, at this point we only need to change 1 into admin like this one:

> admin' union select "admin",2,3 -- 

When I tried login with the payload(as usual), I checked /admin to get the flag.

![](images/4.png)

| The Flag |
| -------- |
| ractf{j4va5cr1pt_w3b_t0ken} |

Okay, so that was my writeup about getting admin challenge thank you for reading. See you next time. 


