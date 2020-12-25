import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    static final String Special_Character = "!@#$%^&*()-+";
                           
    static int minimumNumber(int n, String password) {
        int addNum = 0;
        if (!password.chars().anyMatch(Character::isDigit)) {
            addNum++;
        }
        if (!password.chars().anyMatch(Character::isLowerCase)) {
            addNum++;
        }
        if (!password.chars().anyMatch(Character::isUpperCase)) {
            addNum++;
        }
        if (!password.chars().anyMatch(ch -> Special_Character.indexOf((char) ch) >= 0)) {
            addNum++;
        }
        addNum = Math.max(addNum, 6 - n);

        return addNum;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String password = scanner.nextLine();

        int answer = minimumNumber(n, password);

        bufferedWriter.write(String.valueOf(answer));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
