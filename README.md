
# Loop Objects


Example usage:

```py 
my_loop = Loop(10,lambda x: x * 2 ,1)
print("loop created") 
result = my_loop.manual_next()
```


These loops may be called out of order, and combined with async in order to make a compelling new workflow.


```py 
value = await my_loop.async_manual_next()
my_loop.arg += 1
print("doing more stuff")
for num in range(0,10):
    total+=1

if (my_loop.iteration_finished):
    values[value] = value
```
<br>
<hr>


<b>Loop Object class members</b>

`iterations` is the number of times you would like this loop to run
```py
result = my_loop.manual_next()
if (result == True):
    my_loop.iterations += 1
```
<br>

`func` is the function to be executed by the loop <br>

```py
func = lambda x: x * 2
iterations= 10
my_loop = Loop(iterations,func,arg=1)
```
<br>

`arg` member is the value to be passed to the next iteration of the loop

```py
for iteration in my_loop:  
    print(iteration)
    my_loop.arg +=1
```

<b>note that any of args, iterations, or func may be changed during runtime of the loop object.</b><br>
<br>


`iteration_finished` should be used to be sure you have finished an async iteration of the loop before running code relying on that.
    <br>
```py   
result = my_loop.async_manual_next()
if my_loop.iteration_finished:
    total += result
```
<br>

`async_manual_next` is used to run an iteration of the loop  object asynchronously:

```py 
value = await my_loop.async_manual_next()
my_loop.arg += 1
#more computations happening

while (x < 10):
    x+=1 #another loop happens in the time we wait
         #for an iteration of loop object to finish

if (my_loop.iteration_finished):
    response[value] = value
```
<b>Note that if you don't write async code as your function to be executed in the loop, this code will run synchronously .</b>

<br>

`manual_next` is used to call iterations of synchronous code in a loop object, outside of calling the iterator. `iteration_finished` is not needed to be called if your loop is synchronous, because the code within will have been executed before moving to the next line.

```py 
value = my_loop.manual_next()
my_loop.arg += 1
```