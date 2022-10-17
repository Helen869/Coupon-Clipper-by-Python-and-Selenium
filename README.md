# Interaction-Coupon-Clipper-by-Python-and-Selenium

I like to shopping at Jewelosco(also known as Safeway in other area), but every time I have to applying the digital coupons manually. With this project, the coupons in my interested categories and weekly ad could be loaded automatically. Delay added in page loading, inputing and clipping intentionally to avoid bot dections.

Marianos is my another favourite local grovery store, but it can reconagnize selenium as bot easily. Please refer to issues for details.

### Method to Acchieve:
Combine Selenium automation testing tool with Python 

### Function:
Complete the following functions:
```css
Login automatically

Clip all digital coupons by catagory search result

Clip all weekly ad couopns
```
### How to run:
Package Selenium and Yaml is required
In config.yml file , set up email, password and catagories.
Run file JW_CPCliper.py

####Example of config.yml file as following:
userinfo:
  email: "sfw12345@gmail.com"
  passowrd: "12345abcde"
catagory: [coca, fish]

### To do:
Run the funtion automatically with script , for example run the script every Wednesday  at 1am
Retrieve Rewards summary with expire date
Email/text reminder for interested coupons or expiring rewards
