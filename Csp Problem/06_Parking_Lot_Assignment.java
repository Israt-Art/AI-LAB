/*6. Parking Lot Assignment
Five cars must be parked in 5 spots.
Cars:
C1, C2, C3, C4, C5
Constraints:
● Each car occupies a different spot → allDifferent
● C1 must be parked before C4 → C1 < C4
● C2 cannot park in spot 3 → C2 ≠ 3
● C3 must be adjacent to C5 → |C3 - C5| = 1
● C4 must be in spot 5 → C4 = 5
● C1 and C2 cannot be adjacent → |C1 - C2| ≠ 1*/
package org.example;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solver;
import org.chocosolver.solver.variables.IntVar;

public class ParkingLotAssignment {
    public static void main(String[] args) {

        Model model = new Model("Parking Lot Assignment");

        IntVar C1 = model.intVar("C1", 1, 5);
        IntVar C2 = model.intVar("C2", 1, 5);
        IntVar C3 = model.intVar("C3", 1, 5);
        IntVar C4 = model.intVar("C4", 1, 5);
        IntVar C5 = model.intVar("C5", 1, 5);

        model.allDifferent(C1, C2, C3, C4, C5).post();

        model.arithm(C1, "<", C4).post();

        model.arithm(C2, "!=", 3).post();

        model.distance(C3, C5, "=", 1).post();

        model.arithm(C4, "=", 5).post();

        model.arithm(C1, "-", C2, "!=", 1).post();
        model.arithm(C2, "-", C1, "!=", 1).post();

        Solver solver = model.getSolver();

        if (solver.solve()) {
            System.out.println("C1 = " + C1.getValue());
            System.out.println("C2 = " + C2.getValue());
            System.out.println("C3 = " + C3.getValue());
            System.out.println("C4 = " + C4.getValue());
            System.out.println("C5 = " + C5.getValue());
        } else {
            System.out.println("No solution found.");
        }
    }
}