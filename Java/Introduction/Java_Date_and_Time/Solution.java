// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.util.Scanner;
import java.util.Calendar;

public class Solution {
    public static String getDay(String day, String month, String year) {
        /*
        * Write your code here.
        */
        Calendar someDay = Calendar.getInstance();
        someDay.set(Integer.parseInt(year), Integer.parseInt(month)-1, Integer.parseInt(day));
        int dayOfWeek = someDay.get(Calendar.DAY_OF_WEEK);
        if (dayOfWeek == 2) return "MONDAY";
        if (dayOfWeek == 3) return "TUESDAY";
        if (dayOfWeek == 4) return "WEDNESDAY";
        if (dayOfWeek == 5) return "THURSDAY";
        if (dayOfWeek == 6) return "FRIDAY";
        if (dayOfWeek == 7) return "SATURDAY";
        if (dayOfWeek == 1) return "SUNDAY";
        return "";
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();

        System.out.println(getDay(day, month, year));
    }
}
