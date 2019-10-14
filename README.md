# LearningPracticalPython
## Summary
A repository to store Practical Python project progress and notes.

## Installation
### Ubuntu
```
sudo apt-get install python3  
sudo apt-get install python3-pip  

-pip3 install virtualenv- 
sudo apt-get install python3-venv
sudo python3 -m venv myenv
```
## Key Points

new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))

is equal to:
new_list = [expression(i) for i in old_list if filter(i)]