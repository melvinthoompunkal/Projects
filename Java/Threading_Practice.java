import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOError;
import java.io.IOException;
import java.lang.reflect.Array;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<Integer> num = new ArrayList<>();
        final int[] sum = {0};

        Thread t1 = new Thread("Thread1"){
            public void run() {
                try {
                    FileReader fileReader = new FileReader("/Users/melvinthoompunkal/Downloads/integers.txt");
                    Scanner scanner = new Scanner(fileReader);
                    while (scanner.hasNext()) {
                        if (scanner.hasNextInt()) {
                            num.add(scanner.nextInt());
                        } else {
                            scanner.next();
                        }
                      //Going through your downloads folder to find integers.txt and copying it down
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        };

        Thread t2 = new Thread("Thread2"){
          public void run(){
              for(int i = 0; i<num.size(); i++)
              {
                  sum[0] += num.get(i);
              }
              System.out.println(sum[0]);
          }
        };

        t1.start(); //start() will actually run it as a thread
        try{
            t1.join(); // Main thread will wait till t1 is finished before beginning the next set of instructions
        }catch(Exception e){
            e.printStackTrace();
        }
        t2.start();

        


    }
}
