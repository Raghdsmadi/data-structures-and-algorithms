## Class 03 : BinarySearch

[Back to main](https://github.com/Raghdsmadi/data-structures-and-algorithms) 
******************************************

## Whiteboard 
![whiteboard](./chall4.PNG)

**********************************************************
## Approach & Efficiency

```
 Divide the **sorted** list into 2 prats from the middle. Check if the key value is in the first part pf the list or the second one, then slice the list where the key is located (first or second part). Keep dividing the list untill the middle value equals to the key, and return its index.

The space and time of the code were following the O(n2), because have a while loop which has (n) times, then we have the slicing which has the internal (n). So we got (n*n) which is (n2).
```
