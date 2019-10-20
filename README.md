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

pipenv is now commonly used to manage packages and environments together.

new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))

is equal to:
new_list = [expression(i) for i in old_list if filter(i)]

Typing "python3" in the console allows for direct execution.
f = open("examplefilename.txt","w")
f.write("Example file text here")
f.flush()  confirms the file content without having to close the file.
f.close() confirms changes and closes the file.
f.tell() indicates the position of the cursor.
f.seek(0) returns the cursor to the start of the document.  