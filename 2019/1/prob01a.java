import java.io.*;

public class prob01a {
  public int fuel(int m) {
    return m / 3 - 2;
  }

  public static void main(String[] args) {
    try {
      FileReader in = new FileReader("input.txt");

      int sum = 0;
      String buffer = "";
      int c;
      while (true) {
        c = in.read();
        if (((char) c) == '\n' || c == -1) {
          sum += fuel(Integer.parseInt(buffer.trim()));
          buffer = "";
        } else {
          buffer += (char) c;
        }

        if (c == -1)
          break;
      }

      System.out.println(sum);
      in.close();
    } catch (IOException fe) {
      System.out.println("File not found!");
    }
  }
}
