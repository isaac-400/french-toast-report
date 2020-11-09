# french-toast-report

---

French toast sticks are one of the best breakfast items offered at 
[Class of '53 Commons Dining Hall](https://dining.dartmouth.edu/hours-and-locations/fall-term-dining-schedule) (foco). 
This command line app will email a set of users when this delectable dish is on the breakfast menu.

---
## How to:
1. populate the users.json file with email/name pairs of all your friends
2. set up the sending gmail account via [Yagmail](https://github.com/kootenpv/yagmail) by running to following in the python console: 
    ```python
    import yagmail
    yagmail.register(SENDING_EMAIL, yourpassword)
    ```
2. schedule main.py to execute once a day 
3. profit

---
To do:
- [ ] refactor user addition as command line argument
- [X] set up Yagmail integration
- [ ] set up unsubscribing 
- [ ] host



