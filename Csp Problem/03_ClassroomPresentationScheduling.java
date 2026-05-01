/*3. Classroom Presentation Scheduling
Five students present in 5 time slots.
Students:
A, B, C, D, E
Constraints:
a. All students present at different times → allDifferent
b. A must present before B → A < B
c. C cannot present in slot 2 → C ≠ 2
d. D must present immediately after C → D = C + 1
e. E must be in slot 5 → E = 5
f. B and D cannot be consecutive → |B - D| ≠ 1*/


package org.example;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solver;
import org.chocosolver.solver.variables.IntVar;

public class ClassroomPresentationScheduling {
    public static void main(String[] args) {

        Model model = new Model("Classroom Presentation Scheduling");

        IntVar A = model.intVar("A", 1, 5);
        IntVar B = model.intVar("B", 1, 5);
        IntVar C = model.intVar("C", 1, 5);
        IntVar D = model.intVar("D", 1, 5);
        IntVar E = model.intVar("E", 1, 5);

        model.allDifferent(A, B, C, D, E).post();

        model.arithm(A, "<", B).post();

        model.arithm(C, "!=", 2).post();

        model.arithm(D, "=", C, "+", 1).post();

        model.arithm(E, "=", 5).post();

        model.arithm(B, "-", D, "!=", 1).post();
        model.arithm(D, "-", B, "!=", 1).post();

        Solver solver = model.getSolver();

        if (solver.solve()) {
            System.out.println("A = " + A.getValue());
            System.out.println("B = " + B.getValue());
            System.out.println("C = " + C.getValue());
            System.out.println("D = " + D.getValue());
            System.out.println("E = " + E.getValue());
        } else {
            System.out.println("No solution found.");
        }
    }
}