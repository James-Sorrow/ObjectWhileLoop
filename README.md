
# Loop Objects


Example usage:

```py 
my_loop = Loop(10,lambda x: x * 2 ,1)
print("loop created")  #executing out of order- drop the loop and come back to it at any time
result = my_loop.manual_next()
```


These loops may be called out of order, and combined with async in order to make a compelling new workflow.


```py 
value = await my_loop.async_manual_next()
my_loop.arg += 1
```


<h2>note that if you don't write async code as your function to be executed in the loop this code will run synchronously.</h2>
<br>

`func` is the function to be executed by the loop <br>
`arg` member is the value to be passed to the next iteration of the loop