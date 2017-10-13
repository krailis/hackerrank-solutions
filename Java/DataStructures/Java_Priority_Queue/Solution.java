// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.util.Comparator;
import java.util.Collections;
/*
 * Create the Student and Priorities classes here.
 */
class Student {
    private int id;
    private String name;
    private double cgpa;

    public Student(int sId, String sName, double sCgpa) {
        id = sId;
        name = sName;
        cgpa = sCgpa;
    }

    public int getID () {
        return this.id;
    }

    public String getName () {
        return this.name;
    }

    public double getCGPA () {
        return this.cgpa;
    }
}

class PriorityChecker implements Comparator<Student> {
    @Override
    public int compare (Student a, Student b) {
        if (a.getCGPA() > b.getCGPA()) return -1;
        else if (a.getCGPA() < b.getCGPA()) return 1;
        int c = a.getName().compareTo(b.getName());
        if (c == 0) return a.getID() > b.getID() ? 1 : a.getID() == b.getID() ? 0 : -1;
        else return c;
    }
}

class Priorities {
    List<Student> getStudents (List<String> events) {
        ArrayList<Student> pstudents = new ArrayList<Student>();
        PriorityChecker pc = new PriorityChecker();
        for (String event : events) {
            if (event.compareTo("SERVED") == 0) {
                if (!pstudents.isEmpty())
                    pstudents.remove(0);
                else
                    continue;
            }
            else {
                String[] words = event.split(" ");
                pstudents.add(new Student(Integer.parseInt(words[3]), words[1], Double.parseDouble(words[2])));
                Collections.sort(pstudents, pc);
            }
        }
        return pstudents;
    }
}
