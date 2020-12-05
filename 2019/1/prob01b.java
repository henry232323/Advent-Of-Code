import java.io.*;

public class prob01b {
  public static int fuel(int m) {
    int s = m / 3 - 2;
    if (s > 0) {
      s += fuel(s);
      return s;
    } else {
      return 0;
    }
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
