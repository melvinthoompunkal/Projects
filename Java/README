
# Multi-Threaded File Reader in Java

This Java project demonstrates basic multithreading by reading integers from a file and summing them using two separate threads.

## Overview

The program performs the following steps:

1. **Thread 1 (`t1`)** reads integers from a file (`integers.txt`) and stores them in an `ArrayList<Integer>`.
2. **Thread 2 (`t2`)** waits for Thread 1 to finish, then computes the sum of the integers and prints the result.

## File Structure

```

integers.txt Must be placed at /Users/melvinthoompunkal/Downloads/ 
```

> **Note**: The file path is hardcoded in the program. Update the path if your file is stored elsewhere.

## Requirements


* An `integers.txt` file containing integer values separated by whitespace (space, newline, etc.)

## How to Run

1. Clone the repository or download the `Main.java` file.

2. Make sure the `integers.txt` file exists at:

   ```
   /Users/melvinthoompunkal/Downloads/integers.txt
   ```

   > You can change the file path in the code to point to another location if needed.

3. Compile and run the program:

4. The sum of the integers will be printed to the console.

## Example

If `integers.txt` contains:

```
10 20 30
40
50
```

The output will be:

```
150
```

## Notes

* This program demonstrates a potential **race condition** if `Thread 2` starts before `Thread 1` finishes. However, the use of `t1.join()` ensures that `Thread 2` waits until all numbers are read before summing.
* All exceptions are handled with basic `printStackTrace()`, which can be improved for production-level code.

##What I learned


Through this project, I learned how to use multithreading in Java to perform concurrent tasks. I created two threads: one to read integers from a file and another to compute their sum. 
This taught me how to work with `Thread` objects, override the `run()` method, and use `start()` and `join()` to control the execution order. 
I also gained experience handling file input using `FileReader` and `Scanner`, managing exceptions like `IOException`, and using `ArrayList` to store dynamic data.
Most importantly, I saw how thread synchronization is critical when sharing data between threads, as improper timing could lead to incorrect or inconsistent results.
