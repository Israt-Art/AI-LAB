/*4. Warehouse Shelf Assignment
Five products must be placed on 5 shelves.
Products:
P1, P2, P3, P4, P5
Constraints:
a. All products on different shelves → allDifferent
b. P1 must be left of P3 → P1 < P3
c. P2 cannot be on shelf 1 → P2 ≠ 1
d. P4 must be adjacent to P5 → |P4 - P5| = 1
e. P3 must be on shelf 4 → P3 = 4
f. P1 and P2 cannot be adjacent → |P1 - P2| ≠ 1*/

package org.example;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solver;
import org.chocosolver.solver.variables.IntVar;

public class WarehouseShelfAssignment {
    public static void main(String[] args) {

        Model model = new Model("Warehouse Shelf Assignment");

        IntVar P1 = model.intVar("P1", 1, 5);
        IntVar P2 = model.intVar("P2", 1, 5);
        IntVar P3 = model.intVar("P3", 1, 5);
        IntVar P4 = model.intVar("P4", 1, 5);
        IntVar P5 = model.intVar("P5", 1, 5);

        model.allDifferent(P1, P2, P3, P4, P5).post();

        model.arithm(P1, "<", P3).post();

        model.arithm(P2, "!=", 1).post();

        model.arithm(P3, "=", 4).post();

        model.distance(P4, P5, "=", 1).post();

        model.arithm(P1, "-", P2, "!=", 1).post();
        model.arithm(P2, "-", P1, "!=", 1).post();

        Solver solver = model.getSolver();

        if (solver.solve()) {
            System.out.println("Solution:");
            System.out.println("P1 = " + P1.getValue());
            System.out.println("P2 = " + P2.getValue());
            System.out.println("P3 = " + P3.getValue());
            System.out.println("P4 = " + P4.getValue());
            System.out.println("P5 = " + P5.getValue());
        } else {
            System.out.println("No solution found.");
        }
    }
}