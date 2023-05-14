import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static double koinzidenz (String msg) {
        msg = msg.toUpperCase();
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        ArrayList<Integer> letterCount = new ArrayList<Integer>();
        double koinzidenzIndex = 0.0;
        for (char letter: alphabet.toCharArray()) {
            int count = 0;
            for (char ch: msg.toCharArray()) {
                if (ch == letter) {
                    count++;
                }
            }
            if (count != 0) 
                System.out.println("Häufigkeit von " + letter + ": " + (double) count/msg.length()*100 + "%");
            letterCount.add((count));
        }
        for (int num: letterCount) {
            double index =  (double) num/msg.length();
            koinzidenzIndex += (index * index);
        }
        return koinzidenzIndex;
    }
    public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Geben sie ihren Text ein: ");
        System.out.println("Kooinzidenz Index: " + koinzidenz(inputScanner.nextLine()));
        inputScanner.close();
    }
}