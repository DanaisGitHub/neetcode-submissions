public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
                    int ROWS, COLS, l, r, m, foundRow = -1, lRowValue, rRowValue;
            COLS = matrix[0].Length;
            ROWS = matrix.Length;
            l = 0;
            r = ROWS - 1;

            while (l <= r) {
                m = (l + r) / 2;
                lRowValue = matrix[m][0]; // don't think m ever goes to 0
                rRowValue = matrix[m][COLS - 1];

                if (target >= lRowValue && target <= rRowValue) { foundRow = m; break; }

                if (target > lRowValue && target > rRowValue) l = m + 1;

                if (target < lRowValue && target < rRowValue) r = m - 1;

            }

            if (foundRow == -1) return false;

            

            // Now just normal binary search with foundRow
            l = 0;
            r = COLS - 1;

            while (l <= r) {
                m = (l + r) / 2;

                if (target == matrix[foundRow][m]) return true;

                if (target > matrix[foundRow][m]) l = m + 1; // shorten the window//never null out

                if (target < matrix[foundRow][m]) r = m - 1;

            }

            return false;

    }
}
