/*2. Traffic Light Coordination
Five intersections must be assigned different signal phases (1–5) to avoid congestion.
Intersections:
I1, I2, I3, I4, I5
Constraints:
a. Adjacent intersections must have different phases.
b. I1 must be before I3
c. I5 cannot be phase 1:
d. I2 and I4 cannot differ by more than 2 |I2 - I4| ≤ 2
e. I3 must be phase 3 → I3 = 3.*/


package org.example;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solver;
import org.chocosolver.solver.variables.IntVar;

public class TrafficLightCoordination {
    public static void main(String[] args) {

        Model model = new Model("Traffic Light Coordination");

        IntVar I1 = model.intVar("I1", 1, 5);
        IntVar I2 = model.intVar("I2", 1, 5);
        IntVar I3 = model.intVar("I3", 1, 5);
        IntVar I4 = model.intVar("I4", 1, 5);
        IntVar I5 = model.intVar("I5", 1, 5);

        model.allDifferent(I1, I2, I3, I4, I5).post();

        model.arithm(I1, "<", I3).post();

        model.arithm(I5, "!=", 1).post();

        model.arithm(I2, "-", I4, "<=", 2).post();
        model.arithm(I4, "-", I2, "<=", 2).post();

        model.arithm(I3, "=", 3).post();

        Solver solver = model.getSolver();

        if (solver.solve()) {
            System.out.println("Solution:");
            System.out.println("I1 = " + I1.getValue());
            System.out.println("I2 = " + I2.getValue());
            System.out.println("I3 = " + I3.getValue());
            System.out.println("I4 = " + I4.getValue());
            System.out.println("I5 = " + I5.getValue());
        } else {
            System.out.println("No solution found.");
        }
    }
}