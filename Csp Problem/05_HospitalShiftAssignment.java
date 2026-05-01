/*5. Hospital Shift Assignment
Five doctors are assigned to 5 shifts.
Doctors:
D1, D2, D3, D4, D5
Constraints:
a. Each doctor works a different shift → allDifferent
b. D1 must work before D3 → D1 < D3
c. D2 cannot work shift 4 → D2 ≠ 4
d. D4 must work immediately before D5 → D4 + 1 = D5
e. D3 must be in shift 2 or 3 → D3 ∈ {2,3}
f. D1 and D5 cannot be adjacent shifts → |D1 - D5| ≠ 1*/

package org.example;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solver;
import org.chocosolver.solver.variables.IntVar;

public class HospitalShiftAssignment {
    public static void main(String[] args) {

        Model model = new Model("Hospital Shift Assignment");

        IntVar D1 = model.intVar("D1", 1, 5);
        IntVar D2 = model.intVar("D2", 1, 5);
        IntVar D3 = model.intVar("D3", 1, 5);
        IntVar D4 = model.intVar("D4", 1, 5);
        IntVar D5 = model.intVar("D5", 1, 5);

        model.allDifferent(D1, D2, D3, D4, D5).post();

        model.arithm(D1, "<", D3).post();

        model.arithm(D2, "!=", 4).post();

        model.arithm(D5, "-", D4, "=", 1).post();

        model.member(D3, new int[]{2, 3}).post();

        model.arithm(D1, "-", D5, "!=", 1).post();
        model.arithm(D5, "-", D1, "!=", 1).post();

        Solver solver = model.getSolver();

        if (solver.solve()) {
            System.out.println("D1 = " + D1.getValue());
            System.out.println("D2 = " + D2.getValue());
            System.out.println("D3 = " + D3.getValue());
            System.out.println("D4 = " + D4.getValue());
            System.out.println("D5 = " + D5.getValue());
        } else {
            System.out.println("No solution found.");
        }
    }
}