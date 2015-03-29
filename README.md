# about
Because on my lenovo t540p I was not able to set screen brightness using keyboard I wrote this appindicator to set it. 

# before you start
```
sudo chmod o+w /sys/class/backlight/intel_backlight/brightness
```

# how to run
```
chmod u+x indicator.py
./indicator.py &
``` 

# works on
ubuntu 14.04, python 2.7.6

# bugs/todo
- this is my first python code.
- only two hardcoded levels of brightness
- use max_brigthness
- icon is not working :(
